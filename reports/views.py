# reports/views.py
from django.shortcuts import render, redirect
from django.db.models import Sum, Q 
import datetime
import json
import hashlib
from .models import (
    Invoice, Order, ProductPurchase,
    StoreProduct, TblUserCredit, StoreSet, InvoiceDetails, OrderDetails,
    UserLogin, Users, CustomerInformation, StoreMerchant
)

# --- AUTHENTICATION VIEWS ---

def login_view(request):
    if request.method == 'POST':
        username_in = request.POST.get('username')
        password_in = request.POST.get('password')
        
        try:
            # 1. Fetch user by username
            user = UserLogin.objects.get(username=username_in)
            
            # 2. Calculate MD5 hash with the required SALT ("gef")
            # PHP Logic: md5("gef".$password)
            salted_password = "gef" + password_in
            calculated_hash = hashlib.md5(salted_password.encode('utf-8')).hexdigest()
            
            # 3. Get stored password from DB
            db_pass = str(user.password).strip()

            # 4. Compare Hash (Case-Insensitive)
            if calculated_hash.lower() == db_pass.lower():
                # Password matches! Now check status.
                if user.status == 1:
                    # Success: Set Session
                    request.session['user_id'] = user.user_id
                    request.session['user_type'] = user.user_type
                    request.session['store_id'] = user.store_id
                    request.session['username'] = user.username
                    return redirect('dashboard')
                else:
                    return render(request, 'reports/login.html', {'error': 'Account is inactive.'})
            
            # 5. Fallback for testing (Plain text match)
            elif password_in == db_pass:
                 if user.status == 1:
                    request.session['user_id'] = user.user_id
                    request.session['user_type'] = user.user_type
                    request.session['store_id'] = user.store_id
                    request.session['username'] = user.username
                    return redirect('dashboard')
                 else:
                    return render(request, 'reports/login.html', {'error': 'Account is inactive.'})

            else:
                # Password Mismatch
                # DEBUGGING: If it fails again, uncomment these lines to see the mismatch
                # error_msg = f"Mismatch! <br>Input: {password_in}<br>Salted Input: {salted_password}<br>Calc: {calculated_hash}<br>DB: {db_pass}"
                # return render(request, 'reports/login.html', {'error': error_msg})
                
                return render(request, 'reports/login.html', {'error': 'Invalid username or password.'})

        except UserLogin.DoesNotExist:
            return render(request, 'reports/login.html', {'error': 'Invalid username or password.'})
            
    return render(request, 'reports/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')


# --- DASHBOARD VIEW ---

def dashboard_view(request):
    # 1. Authentication Guard
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user_type = request.session.get('user_type')
    session_store_id = request.session.get('store_id')
    username = request.session.get('username')

    # 2. RBAC: Determine Allowed Stores
    # user_type: 1=admin, 2=shop-manager/merchant, 4=store keeper
    allowed_store_ids = [] 
    is_admin = False
    
    if user_type == 1:
        is_admin = True
        # Admin sees all, so we leave allowed_store_ids empty to signify "ALL"
    elif user_type == 2: 
        # Merchant: Fetch stores linked to this merchant ID
        # Assuming StoreMerchant links merchant_id to store_id
        allowed_store_ids = list(StoreMerchant.objects.filter(merchant_id=user_id).values_list('store_id', flat=True))
    elif user_type == 4:
        # Store Keeper: Uses the single store assigned in UserLogin
        if session_store_id:
            allowed_store_ids = [session_store_id]
    else:
        # Fallback for other roles (Sales man etc) - restrict to session store or none
        if session_store_id:
            allowed_store_ids = [session_store_id]

    # --- URL PARAMETERS ---
    current_tab = request.GET.get('tab', 'sales')
    
    # Get user input for GLOBAL filters
    end_date_str = request.GET.get('end_date')
    start_date_str = request.GET.get('start_date')
    
    # Get user input for TAB specific filters
    user_id_filter = request.GET.get('user_id_filter', '').strip()
    credit_start_date_str = request.GET.get('credit_start_date') 
    credit_end_date_str = request.GET.get('credit_end_date') 
    store_id_filter = request.GET.get('store_id_filter', '').strip()
    transaction_start_date_str = request.GET.get('transaction_start_date') 
    transaction_end_date_str = request.GET.get('transaction_end_date') 

    today = datetime.date.today()
    
    # --- HELPER FUNCTIONS FOR DATE PARSING ---
    def parse_date_input(date_str):
        if not date_str: return None
        for fmt in ('%Y-%m-%d', '%m/%d/%Y', '%m-%d-%Y'):
            try:
                return datetime.datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        return None

    def parse_db_date(date_str):
        if not date_str: return None
        for fmt in ('%m-%d-%Y', '%m/%d/%Y', '%Y-%m-%d'):
            try:
                return datetime.datetime.strptime(str(date_str).strip(), fmt).date()
            except (ValueError, TypeError):
                continue
        return None

    # Parse inputs
    global_filter_start_date = parse_date_input(start_date_str)
    global_filter_end_date = parse_date_input(end_date_str)
    credit_filter_start_date = parse_date_input(credit_start_date_str)
    credit_filter_end_date = parse_date_input(credit_end_date_str)
    transaction_filter_start_date = parse_date_input(transaction_start_date_str)
    transaction_filter_end_date = parse_date_input(transaction_end_date_str)

    # Display Variables
    filter_start_str = "All Time"
    filter_end_str = ""
    filter_start_date_html = start_date_str
    filter_end_date_html = end_date_str
    credit_start_date_html = credit_start_date_str
    credit_end_date_html = credit_end_date_str
    transaction_start_date_html = transaction_start_date_str
    transaction_end_date_html = transaction_end_date_str


    # --- RBAC FILTER APPLICATION HELPER ---
    def apply_store_permission(queryset):
        if is_admin:
            return queryset
        if not allowed_store_ids:
            return queryset.none() # No stores assigned, show nothing
        return queryset.filter(store_id__in=allowed_store_ids)

    # --- GLOBAL METRICS LOGIC ---
    
    # 1. Base QuerySets (Pre-filtered by Role)
    invoice_qs = apply_store_permission(Invoice.objects.all())
    order_qs = apply_store_permission(Order.objects.all())
    store_set_qs = apply_store_permission(StoreSet.objects.all())
    store_prod_qs = apply_store_permission(StoreProduct.objects.all())
    # Credit is special, usually global. We might hide it for non-admins.
    credit_qs = TblUserCredit.objects.all() 

    # 2. Apply Date Filters to Global Metrics
    global_invoice_filter = Q()
    global_credit_filter = Q() # Credit doesn't filter by store usually
    
    if global_filter_start_date or global_filter_end_date:
        display_start = global_filter_start_date.strftime('%Y-%m-%d') if global_filter_start_date else "Start"
        display_end = global_filter_end_date.strftime('%Y-%m-%d') if global_filter_end_date else "Now"

        if global_filter_start_date and global_filter_end_date:
            filter_start_str = display_start
            filter_end_str = display_end
        elif global_filter_start_date:
            filter_start_str = f"From {display_start}"
        elif global_filter_end_date:
            filter_start_str = f"Up to {display_end}"
        
        if global_filter_start_date:
            global_invoice_filter &= Q(date__gte=global_filter_start_date.strftime('%Y-%m-%d'))
            global_credit_filter &= Q(transaction_datetime__date__gte=global_filter_start_date)

        if global_filter_end_date:
            global_invoice_filter &= Q(date__lte=global_filter_end_date.strftime('%Y-%m-%d'))
            global_credit_filter &= Q(transaction_datetime__date__lte=global_filter_end_date)
            
    # 3. Calculate Metrics
    total_sales = invoice_qs.filter(global_invoice_filter).aggregate(total=Sum('total_amount'))['total'] or 0.0
    total_orders = order_qs.filter(global_invoice_filter).count() # Approximation using same date logic if applicable
    
    # Only Admins see total credit balance usually
    total_credit_balance = 0.0
    if is_admin:
        total_credit_balance = credit_qs.filter(global_credit_filter).aggregate(total=Sum('balance'))['total'] or 0.0
    
    active_machines = store_set_qs.filter(is_active=1).count()
    total_stock_count = store_prod_qs.aggregate(total=Sum('quantity'))['total'] or 0


    # --- TAB-SPECIFIC DATA ---
    tab_data = {}
    
    if current_tab == 'sales':
        # Date filters
        sales_start = global_filter_start_date or (today - datetime.timedelta(days=30))
        sales_end = global_filter_end_date or today
        
        sales_start_str = sales_start.strftime('%Y-%m-%d')
        sales_end_str = sales_end.strftime('%Y-%m-%d')
        
        sales_display_start = f"From {sales_start_str}" if global_filter_start_date else "Last 30 Days"
        sales_display_end = f"to {sales_end_str}" if global_filter_end_date else ""

        # Use the role-filtered invoice_qs
        filtered_invoices = invoice_qs.filter(
            date__gte=sales_start_str,
            date__lte=sales_end_str
        ).order_by('-date')[:100]

        total_filtered_sales = invoice_qs.filter(
            date__gte=sales_start_str, 
            date__lte=sales_end_str
        ).aggregate(Sum('total_amount'))['total_amount__sum'] or 0.0
        
        # Chart Data
        chart_qs = invoice_qs.filter(
            date__gte=sales_start_str,
            date__lte=sales_end_str
        ).values('date').annotate(daily=Sum('total_amount')).order_by('date')
        
        chart_labels = [entry['date'] for entry in chart_qs]
        chart_values = [float(entry['daily']) if entry['daily'] else 0.0 for entry in chart_qs]

        tab_data.update({
            'invoices': filtered_invoices,
            'total_filtered_sales': total_filtered_sales, 
            'chart_labels_json': json.dumps(chart_labels),
            'chart_data_json': json.dumps(chart_values),
            'sales_display_start': sales_display_start,
            'sales_display_end': sales_display_end,
        })

    elif current_tab == 'transactions':
        # Use role-filtered order_qs
        
        # 1. Maps
        # Fetch only relevant stores
        if is_admin:
            stores = StoreSet.objects.all().values('store_id', 'store_name')
        else:
            # Only fetch stores allowed for this user
            stores = StoreSet.objects.filter(store_id__in=allowed_store_ids).values('store_id', 'store_name')
            
        store_map = {s['store_id']: s['store_name'] for s in stores}
        searchable_stores = [{'id': s['store_id'], 'name': s['store_name'] or f"ID: {s['store_id']}"} for s in stores]
        
        # Customers map
        customers = CustomerInformation.objects.all().values('customer_id', 'first_name', 'last_name')
        customer_map = {c['customer_id']: f"{c['first_name'] or ''} {c['last_name'] or ''}".strip() for c in customers}

        tab_data.update({
            'searchable_stores_json': json.dumps(searchable_stores),
            'store_id_filter': store_id_filter,
            'transaction_start_date_html': transaction_start_date_str,
            'transaction_end_date_html': transaction_end_date_str,
        })

        # 2. Filter Logic
        orders_filtered = order_qs # Already restricted by store permissions
        
        display_txt_start = "Recent Records"
        display_txt_end = ""
        
        if store_id_filter:
            # Verify user has permission to search this specific store
            if is_admin or store_id_filter in allowed_store_ids:
                orders_filtered = orders_filtered.filter(store_id=store_id_filter)
                s_name = store_map.get(store_id_filter, f"ID: {store_id_filter}")
                display_txt_start = f"Store: {s_name}"
                tab_data['selected_store_name'] = s_name

        # 3. Processing (Date + Names)
        # We fetch list to process dates in python as before
        orders_list = list(orders_filtered)
        processed = []
        
        for o in orders_list:
            o.store_name = store_map.get(o.store_id, f"ID: {o.store_id}")
            o.customer_name = customer_map.get(o.customer_id, f"ID: {o.customer_id}")
            
            o_date = parse_db_date(o.date)
            o.parsed_date = o_date
            
            if transaction_filter_start_date and (not o_date or o_date < transaction_filter_start_date): continue
            if transaction_filter_end_date and (not o_date or o_date > transaction_filter_end_date): continue
            
            processed.append(o)
            
        # Sort & Limit
        processed.sort(key=lambda x: x.parsed_date or datetime.date.min, reverse=True)
        
        limit = 50 if not (store_id_filter or transaction_filter_start_date or transaction_filter_end_date) else None
        final_orders = processed[:limit] if limit else processed
        
        total_amt = sum(o.total_amount or 0.0 for o in processed)
        
        if transaction_filter_start_date:
            display_txt_start += f" | From: {transaction_filter_start_date}"
            display_txt_end = f"To: {transaction_filter_end_date}" if transaction_filter_end_date else ""

        tab_data.update({
            'orders': final_orders,
            'total_filtered_orders_amount': total_amt,
            'transactions_display_start': display_txt_start,
            'transactions_display_end': display_txt_end
        })

    elif current_tab == 'credit':
        # RESTRICT CREDIT TAB to Admin Only
        if not is_admin:
            tab_data['error_message'] = "Access Denied: Credit Ledger is restricted to Administrators."
        else:
            # Full Credit Logic (Same as before)
            user_logins = UserLogin.objects.all().values('user_id', 'username')
            user_names = Users.objects.all().values('user_id', 'first_name', 'last_name')
            username_map = {u['user_id']: u['username'] for u in user_logins}
            name_map = {u['user_id']: f"{u['first_name']} {u['last_name']}" for u in user_names}
            
            search_users = [{'id': k, 'name': v, 'username': username_map.get(k)} for k,v in name_map.items()]
            
            tab_data.update({
                'searchable_users_json': json.dumps(search_users),
                'user_id_filter': user_id_filter,
                'credit_start_date_html': credit_start_date_str,
                'credit_end_date_html': credit_end_date_str,
            })
            
            c_qs = TblUserCredit.objects.all()
            if user_id_filter: c_qs = c_qs.filter(user_id=user_id_filter)
            
            if credit_filter_start_date: c_qs = c_qs.filter(end_date__date__gte=credit_filter_start_date)
            if credit_filter_end_date: c_qs = c_qs.filter(end_date__date__lte=credit_filter_end_date)
            
            c_list = list(c_qs.order_by('-transaction_datetime')[:1000])
            for c in c_list:
                c.display_name = name_map.get(c.user_id) or username_map.get(c.user_id) or c.user_id
                
            tab_data['credits'] = c_list

    elif current_tab == 'stock':
        # Stock Tab - Role Filtered
        stock_summary = store_prod_qs.values('product_id', 'variant_id').annotate(total_stock=Sum('quantity'))
        tab_data['stock_summary'] = stock_summary


    context = {
        'page_title': 'Vendy Reports Dashboard',
        'current_tab': current_tab,
        'username': username,
        'is_admin': is_admin,
        'filter_start_date': filter_start_str, 
        'filter_end_date': filter_end_str,    
        'filter_start_date_html': filter_start_date_html,
        'filter_end_date_html': filter_end_date_html,
        'total_sales': f"{total_sales:,.2f}",
        'total_orders': f"{total_orders:,}",
        'active_machines': active_machines,
        'total_stock_count': f"{total_stock_count:,}",
        'total_credit_balance': f"{total_credit_balance:,.2f}",
        **tab_data,
    }
    
    return render(request, 'reports/dashboard.html', context)