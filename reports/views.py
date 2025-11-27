# reports/views.py
from django.shortcuts import render, redirect
from django.db.models import Sum, Q 
import datetime
import json
import hashlib
from .models import (
    Invoice, Order, ProductPurchase,
    StoreProduct, TblUserCredit, StoreSet, InvoiceDetails, OrderDetails,
    UserLogin, Users, CustomerInformation, StoreMerchant, TblCreditTransection,
    TblUserStores, ProductInformation, Variant, Received, Quotation, CustomerLedger,
    ChequeManger
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
                return render(request, 'reports/login.html', {'error': 'Invalid username or password.'})

        except UserLogin.DoesNotExist:
            return render(request, 'reports/login.html', {'error': 'Invalid username or password.'})
            
    return render(request, 'reports/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')


# --- HELPER: GET ALLOWED STORES ---
def get_user_permissions(request):
    """
    Returns a tuple: (user_id, is_admin, is_merchant, is_store_keeper, allowed_store_ids, username)
    Or None if not logged in.
    """
    user_id = request.session.get('user_id')
    if not user_id:
        return None

    user_type = request.session.get('user_type')
    session_store_id = request.session.get('store_id')
    username = request.session.get('username')

    allowed_store_ids = [] 
    is_admin = False
    is_merchant = False
    is_store_keeper = False
    
    if user_type == 1:
        is_admin = True
    elif user_type == 6: 
        is_merchant = True
        allowed_store_ids = list(StoreMerchant.objects.filter(merchant_id=user_id).values_list('store_id', flat=True))
    elif user_type == 4:
        is_store_keeper = True
        if session_store_id:
            allowed_store_ids = [session_store_id]
    else:
        if session_store_id:
            allowed_store_ids = [session_store_id]
            
    return (user_id, is_admin, is_merchant, is_store_keeper, allowed_store_ids, username)


# --- DASHBOARD VIEW ---

def dashboard_view(request):
    perms = get_user_permissions(request)
    if not perms:
        return redirect('login')
    
    user_id, is_admin, is_merchant, is_store_keeper, allowed_store_ids, username = perms

    # --- URL PARAMETERS ---
    current_tab = request.GET.get('tab', 'sales')
    
    end_date_str = request.GET.get('end_date')
    start_date_str = request.GET.get('start_date')
    
    user_id_filter = request.GET.get('user_id_filter', '').strip()
    
    credit_start_date_str = request.GET.get('credit_start_date') 
    credit_end_date_str = request.GET.get('credit_end_date') 
    
    store_id_filter = request.GET.get('store_id_filter', '').strip()
    transaction_start_date_str = request.GET.get('transaction_start_date') 
    transaction_end_date_str = request.GET.get('transaction_end_date') 
    
    sales_store_id = request.GET.get('sales_store_id', '').strip()
    sales_start_date_str = request.GET.get('sales_start_date')
    sales_end_date_str = request.GET.get('sales_end_date')


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

    global_filter_start_date = parse_date_input(start_date_str)
    global_filter_end_date = parse_date_input(end_date_str)
    
    sales_filter_start_date = parse_date_input(sales_start_date_str)
    sales_filter_end_date = parse_date_input(sales_end_date_str)

    credit_filter_start_date = parse_date_input(credit_start_date_str)
    credit_filter_end_date = parse_date_input(credit_end_date_str)
    transaction_filter_start_date = parse_date_input(transaction_start_date_str)
    transaction_filter_end_date = parse_date_input(transaction_end_date_str)

    filter_start_str = "All Time"
    filter_end_str = ""
    filter_start_date_html = start_date_str
    filter_end_date_html = end_date_str
    
    sales_start_date_html = sales_start_date_str
    sales_end_date_html = sales_end_date_str
    
    credit_start_date_html = credit_start_date_str
    credit_end_date_html = credit_end_date_str
    transaction_start_date_html = transaction_start_date_str
    transaction_end_date_html = transaction_end_date_str


    def apply_store_permission(queryset):
        if is_admin:
            return queryset
        if not allowed_store_ids:
            return queryset.none() 
        return queryset.filter(store_id__in=allowed_store_ids)

    # --- GLOBAL METRICS LOGIC ---
    
    invoice_qs = apply_store_permission(Invoice.objects.all())
    order_qs = apply_store_permission(Order.objects.all())
    store_set_qs = apply_store_permission(StoreSet.objects.all())
    store_prod_qs = apply_store_permission(StoreProduct.objects.all())
    credit_qs = TblUserCredit.objects.all() 

    global_invoice_filter = Q()
    global_credit_filter = Q() 
    
    if global_filter_start_date or global_filter_end_date:
        display_start = global_filter_start_date.strftime('%d %b %Y') if global_filter_start_date else "Start"
        display_end = global_filter_end_date.strftime('%d %b %Y') if global_filter_end_date else "Now"

        if global_filter_start_date and global_filter_end_date:
            filter_start_str = display_start
            filter_end_str = display_end
        elif global_filter_start_date:
            filter_start_str = f"From {display_start}"
        elif global_filter_end_date:
            filter_start_str = f"Up to {display_end}"
        
        if global_filter_start_date:
            global_invoice_filter &= Q(date__gte=global_filter_start_date.strftime('%d %b %Y'))
            global_credit_filter &= Q(transaction_datetime__date__gte=global_filter_start_date)

        if global_filter_end_date:
            global_invoice_filter &= Q(date__lte=global_filter_end_date.strftime('%d %b %Y'))
            global_credit_filter &= Q(transaction_datetime__date__lte=global_filter_end_date)
            
    total_sales = invoice_qs.filter(global_invoice_filter).aggregate(total=Sum('total_amount'))['total'] or 0.0
    total_orders = order_qs.filter(global_invoice_filter).count() 
    
    total_credit_balance = 0.0
    if is_admin:
        total_credit_balance = credit_qs.filter(global_credit_filter).aggregate(total=Sum('balance'))['total'] or 0.0
    elif is_merchant or is_store_keeper:
        relevant_customer_ids = Order.objects.filter(
            store_id__in=allowed_store_ids
        ).values_list('customer_id', flat=True).distinct()
        
        total_credit_balance = credit_qs.filter(
            global_credit_filter,
            user_id__in=relevant_customer_ids
        ).aggregate(total=Sum('balance'))['total'] or 0.0

    active_machines = store_set_qs.filter(is_active=1).count()
    total_stock_count = store_prod_qs.aggregate(total=Sum('quantity'))['total'] or 0


    # --- TAB-SPECIFIC DATA ---
    tab_data = {}
    
    if current_tab == 'sales':
        if is_admin:
            sales_stores = StoreSet.objects.all().values('store_id', 'store_name')
        else:
            sales_stores = StoreSet.objects.filter(store_id__in=allowed_store_ids).values('store_id', 'store_name')
        
        sales_stores_list = [{'id': s['store_id'], 'name': s['store_name'] or f"ID: {s['store_id']}"} for s in sales_stores]
        relevant_stores_map = {s['id']: s['name'] for s in sales_stores_list}

        target_store_ids = []
        selected_store_name = "All Stores"
        
        if sales_store_id:
            if is_admin or sales_store_id in allowed_store_ids:
                target_store_ids = [sales_store_id]
                selected_store_name = relevant_stores_map.get(sales_store_id, "Unknown Store")
        else:
            target_store_ids = [s['id'] for s in sales_stores_list]

        raw_invoice_qs = Invoice.objects.filter(store_id__in=target_store_ids).values('invoice_id', 'store_id', 'date', 'total_amount')

        sales_summary_by_store = {sid: {'store_id': sid, 'name': relevant_stores_map.get(sid, f"ID: {sid}"), 'amount': 0.0, 'count': 0} for sid in target_store_ids}
        store_daily_data = {sid: {} for sid in target_store_ids} 
        all_dates = set()
        
        filtered_total_sales = 0.0
        filtered_invoice_count = 0
        
        for inv in raw_invoice_qs:
            inv_date = parse_db_date(inv['date'])
            if not inv_date: continue
                
            if sales_filter_start_date and inv_date < sales_filter_start_date: continue
            if sales_filter_end_date and inv_date > sales_filter_end_date: continue
            
            sid = inv['store_id']
            amount = float(inv['total_amount'] or 0.0)
            
            if sid in sales_summary_by_store:
                sales_summary_by_store[sid]['amount'] += amount
                sales_summary_by_store[sid]['count'] += 1
                
                all_dates.add(inv_date)
                if inv_date not in store_daily_data[sid]:
                    store_daily_data[sid][inv_date] = 0.0
                store_daily_data[sid][inv_date] += amount
                
                filtered_total_sales += amount
                filtered_invoice_count += 1

        sales_summary_list = list(sales_summary_by_store.values())
        sales_summary_list.sort(key=lambda x: x['amount'], reverse=True)
        
        sorted_dates = sorted(list(all_dates))
        chart_labels = [d.strftime('%d %b %Y') for d in sorted_dates]
        
        datasets = []
        colors = ['#4F46E5', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#EC4899', '#6366F1', '#14B8A6', '#F97316', '#06B6D4']
        
        doughnut_labels = []
        doughnut_data = []
        doughnut_colors = []

        for idx, sid in enumerate(target_store_ids):
            amount = sales_summary_by_store[sid]['amount']
            s_name = sales_summary_by_store[sid]['name']
            color = colors[idx % len(colors)]
            
            if sales_store_id or amount > 0:
                s_data = [store_daily_data[sid].get(d, 0.0) for d in sorted_dates]
                datasets.append({
                    'label': s_name,
                    'data': s_data,
                    'borderColor': color,
                    'backgroundColor': color,
                    'tension': 0.3,
                    'fill': False
                })
            
            if amount > 0:
                doughnut_labels.append(s_name)
                doughnut_data.append(amount)
                doughnut_colors.append(color)

        sales_display_start = f"From {sales_filter_start_date}" if sales_filter_start_date else "All Time"
        sales_display_end = f"to {sales_filter_end_date}" if sales_filter_end_date else ""

        tab_data.update({
            'sales_summary_list': sales_summary_list,
            'total_filtered_sales': filtered_total_sales, 
            'filtered_invoice_count': filtered_invoice_count,
            'chart_labels_json': json.dumps(chart_labels),
            'chart_datasets_json': json.dumps(datasets),
            'doughnut_labels_json': json.dumps(doughnut_labels),
            'doughnut_data_json': json.dumps(doughnut_data),
            'doughnut_colors_json': json.dumps(doughnut_colors),
            
            'sales_display_start': sales_display_start,
            'sales_display_end': sales_display_end,
            'sales_stores': sales_stores_list,
            'sales_store_id': sales_store_id,
            'selected_store_name': selected_store_name,
            'sales_start_date_html': sales_start_date_html,
            'sales_end_date_html': sales_end_date_html
        })

    elif current_tab == 'transactions':
        if is_admin:
            stores = StoreSet.objects.all().values('store_id', 'store_name')
        else:
            stores = StoreSet.objects.filter(store_id__in=allowed_store_ids).values('store_id', 'store_name')
            
        store_map = {s['store_id']: s['store_name'] for s in stores}
        searchable_stores = [{'id': s['store_id'], 'name': s['store_name'] or f"ID: {s['store_id']}"} for s in stores]
        
        customers = CustomerInformation.objects.all().values('customer_id', 'first_name', 'last_name')
        customer_map = {c['customer_id']: f"{c['first_name'] or ''} {c['last_name'] or ''}".strip() for c in customers}

        tab_data.update({
            'searchable_stores_json': json.dumps(searchable_stores),
            'store_id_filter': store_id_filter,
            'transaction_start_date_html': transaction_start_date_str,
            'transaction_end_date_html': transaction_end_date_str,
        })

        orders_filtered = order_qs 
        display_txt_start = "Recent Records"
        display_txt_end = ""
        
        if store_id_filter:
            if is_admin or store_id_filter in allowed_store_ids:
                orders_filtered = orders_filtered.filter(store_id=store_id_filter)
                s_name = store_map.get(store_id_filter, f"ID: {store_id_filter}")
                display_txt_start = f"Store: {s_name}"
                tab_data['selected_store_name'] = s_name
        
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
            
        processed.sort(key=lambda x: x.parsed_date or datetime.date.min, reverse=True)
        limit = 50 if not (store_id_filter or transaction_filter_start_date or transaction_filter_end_date) else None
        final_orders = processed[:limit] if limit else processed
        
        total_amt = sum(float(o.total_amount) if o.total_amount else 0.0 for o in processed)
        
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
        if not (is_admin or is_merchant or is_store_keeper):
            tab_data['error_message'] = "Access Denied."
        else:
            user_logins = UserLogin.objects.all().values('user_id', 'username')
            user_names = Users.objects.all().values('user_id', 'first_name', 'last_name')
            store_sets = StoreSet.objects.all().values('store_id', 'store_name')

            username_map = {u['user_id']: u['username'] for u in user_logins}
            name_map = {u['user_id']: f"{u['first_name']} {u['last_name']}" for u in user_names}
            store_map = {s['store_id']: s['store_name'] for s in store_sets}
            
            search_users = [{'id': k, 'name': v, 'username': username_map.get(k)} for k,v in name_map.items()]
            
            tab_data.update({
                'searchable_users_json': json.dumps(search_users),
                'user_id_filter': user_id_filter,
                'credit_start_date_html': credit_start_date_str,
                'credit_end_date_html': credit_end_date_str,
            })
            
            c_qs = TblUserCredit.objects.all()

            if is_merchant or is_store_keeper:
                # Identify Customers linked to allowed stores via multiple tables
                
                # 1. Orders
                order_users = Order.objects.filter(store_id__in=allowed_store_ids).values_list('customer_id', flat=True)
                
                # 2. Assigned Users (TblUserStores)
                assigned_users = TblUserStores.objects.filter(store_id__in=allowed_store_ids).values_list('user_id', flat=True)
                
                # 3. Received (Includes Bill Acceptor/Payments)
                received_users = Received.objects.filter(store_id__in=allowed_store_ids).values_list('customer_id', flat=True)
                
                # 4. Invoices
                invoice_users = Invoice.objects.filter(store_id__in=allowed_store_ids).values_list('customer_id', flat=True)
                
                # 5. Quotations
                quotation_users = Quotation.objects.filter(store_id__in=allowed_store_ids).values_list('customer_id', flat=True)
                
                # 6. Cheque Transactions
                cheque_users = ChequeManger.objects.filter(store_id__in=allowed_store_ids).values_list('customer_id', flat=True)

                relevant_user_ids = set(order_users) | set(assigned_users) | set(received_users) | set(invoice_users) | set(quotation_users) | set(cheque_users)
                
                if not relevant_user_ids:
                     c_qs = c_qs.none()
                else:
                     c_qs = c_qs.filter(user_id__in=relevant_user_ids)

            if user_id_filter: 
                c_qs = c_qs.filter(user_id=user_id_filter)
            
            if credit_filter_start_date: c_qs = c_qs.filter(end_date__date__gte=credit_filter_start_date)
            if credit_filter_end_date: c_qs = c_qs.filter(end_date__date__lte=credit_filter_end_date)
            
            c_list = list(c_qs.order_by('-transaction_datetime')[:1000])

            displayed_user_ids = [c.user_id for c in c_list]
            ul_map = {}
            if displayed_user_ids:
                ul_data = UserLogin.objects.filter(user_id__in=displayed_user_ids).exclude(store_id__isnull=True).values('user_id', 'store_id')
                for x in ul_data:
                    ul_map[x['user_id']] = x['store_id']
            tus_map = {}
            if displayed_user_ids:
                tus_data = TblUserStores.objects.filter(user_id__in=displayed_user_ids).values('user_id', 'store_id')
                for x in tus_data:
                    tus_map[x['user_id']] = x['store_id']
            order_map = {}
            if displayed_user_ids:
                order_data = Order.objects.filter(customer_id__in=displayed_user_ids).values('customer_id', 'store_id')
                for x in order_data:
                    order_map[x['customer_id']] = x['store_id']

            for c in c_list:
                c.display_name = name_map.get(c.user_id) or username_map.get(c.user_id) or c.user_id
                store_id = ul_map.get(c.user_id)
                if not store_id: store_id = tus_map.get(c.user_id)
                if not store_id: store_id = order_map.get(c.user_id)
                c.store_id = store_id or "N/A"
                c.store_name = store_map.get(store_id, "N/A")
                
            tab_data['credits'] = c_list

    elif current_tab == 'stock':
        stock_data = list(store_prod_qs.values('product_id', 'variant_id', 'quantity'))
        
        product_ids = set(str(item['product_id']).strip() for item in stock_data if item['product_id'])
        variant_ids = set(str(item['variant_id']).strip() for item in stock_data if item['variant_id'])
        
        p_map = {p.product_id: p.product_name for p in ProductInformation.objects.filter(product_id__in=product_ids)}
        v_map = {v.variant_id: v.variant_name for v in Variant.objects.filter(variant_id__in=variant_ids)}
        
        agg_map = {} 
        for item in stock_data:
            pid = str(item['product_id']).strip() if item['product_id'] else "N/A"
            vid = str(item['variant_id']).strip() if item['variant_id'] else "N/A"
            key = (pid, vid)
            
            if key not in agg_map:
                agg_map[key] = 0
            agg_map[key] += (item['quantity'] or 0)
            
        stock_summary = []
        for (pid, vid), qty in agg_map.items():
            stock_summary.append({
                'product_id': pid,
                'product_name': p_map.get(pid, f"Unknown Product ({pid})"),
                'variant_id': vid,
                'variant_name': v_map.get(vid, vid),
                'total_stock': qty
            })
            
        stock_summary.sort(key=lambda x: x['product_name'])
        tab_data['stock_summary'] = stock_summary


    context = {
        'page_title': 'Vendy Reports Dashboard',
        'current_tab': current_tab,
        'username': username,
        'is_admin': is_admin,
        'is_merchant': is_merchant,
        'is_store_keeper': is_store_keeper, 
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


# --- NEW: STORES VIEW ---

def stores_view(request):
    perms = get_user_permissions(request)
    if not perms: return redirect('login')
    user_id, is_admin, is_merchant, is_store_keeper, allowed_store_ids, username = perms

    search_query = request.GET.get('q', '').strip()
    
    # 1. Base Query
    if is_admin:
        stores = StoreSet.objects.all()
    else:
        stores = StoreSet.objects.filter(store_id__in=allowed_store_ids)
        
    # 2. Apply Search
    if search_query:
        stores = stores.filter(
            Q(store_name__icontains=search_query) | 
            Q(store_id__icontains=search_query) |
            Q(store_address__icontains=search_query)
        )
        
    context = {
        'page_title': 'Store Management',
        'username': username,
        'is_admin': is_admin,
        'is_merchant': is_merchant,
        'is_store_keeper': is_store_keeper,
        'stores': stores,
        'search_query': search_query
    }
    return render(request, 'reports/stores.html', context)


# --- NEW: CUSTOMERS VIEW ---

def customers_view(request):
    perms = get_user_permissions(request)
    if not perms: return redirect('login')
    user_id, is_admin, is_merchant, is_store_keeper, allowed_store_ids, username = perms

    search_query = request.GET.get('q', '').strip()
    
    # 1. Base Query
    if is_admin:
        customers = CustomerInformation.objects.all()
    else:
        # Identify Customers linked to allowed stores via multiple tables
        
        # A. Direct Links via Store ID
        # 1. Orders (uses customer_id)
        store_orders = Order.objects.filter(store_id__in=allowed_store_ids)
        order_users = store_orders.values_list('customer_id', flat=True)
        
        # 2. Assigned Users (TblUserStores uses user_id)
        assigned_users = TblUserStores.objects.filter(store_id__in=allowed_store_ids).values_list('user_id', flat=True)
        
        # 3. Received (Includes Bill Acceptor/Payments)
        store_received = Received.objects.filter(store_id__in=allowed_store_ids)
        received_users = store_received.values_list('customer_id', flat=True)
        
        # 4. Invoices
        store_invoices = Invoice.objects.filter(store_id__in=allowed_store_ids)
        invoice_users = store_invoices.values_list('customer_id', flat=True)
        
        # 5. Quotations
        store_quotations = Quotation.objects.filter(store_id__in=allowed_store_ids)
        quotation_users = store_quotations.values_list('customer_id', flat=True)
        
        # 6. Cheque Transactions
        cheque_users = ChequeManger.objects.filter(store_id__in=allowed_store_ids).values_list('customer_id', flat=True)

        # B. Indirect Links via CustomerLedger (The "Credit" search)
        # CustomerLedger doesn't have store_id, so we link via document numbers from tables above.
        
        # Extract Document Numbers
        inv_nums = store_invoices.values_list('invoice', flat=True)
        ord_nums = store_orders.values_list('order', flat=True) # 'order' field in Order model is the order number string
        rec_nums = store_received.values_list('transection_id', flat=True) 
        quot_nums = store_quotations.values_list('quotation', flat=True)

        # Find customers in Ledger referencing these documents
        # We use sets to avoid huge OR queries, searching each type
        ledger_users = set()
        
        if inv_nums:
            ledger_users.update(CustomerLedger.objects.filter(invoice_no__in=inv_nums).values_list('customer_id', flat=True))
        if ord_nums:
            ledger_users.update(CustomerLedger.objects.filter(order_no__in=ord_nums).values_list('customer_id', flat=True))
        if rec_nums:
            # receipt_no in Ledger usually matches transection_id from Received
            ledger_users.update(CustomerLedger.objects.filter(receipt_no__in=rec_nums).values_list('customer_id', flat=True))
        if quot_nums:
            ledger_users.update(CustomerLedger.objects.filter(quotation_no__in=quot_nums).values_list('customer_id', flat=True))

        # Combine all user/customer IDs found
        relevant_ids = set(order_users) | set(assigned_users) | set(received_users) | set(invoice_users) | set(quotation_users) | set(cheque_users) | ledger_users
        
        # IMPORTANT: Filter CustomerInformation by checking BOTH customer_id AND user_id
        # Some tables (like TblUserStores) use user_id, others (Order) use customer_id.
        customers = CustomerInformation.objects.filter(
            Q(customer_id__in=relevant_ids) | Q(user_id__in=relevant_ids)
        )

    # 2. Apply Search
    if search_query:
        customers = customers.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(customer_mobile__icontains=search_query) |
            Q(customer_email__icontains=search_query) |
            Q(customer_id__icontains=search_query)
        )

    # Limit results for performance if no search
    # 3. Calculate "Total Transitioned Amount" for each customer
    # We fetch them as a list to attach custom attributes
    customers_list = list(customers[:50]) 

    for c in customers_list:
        # Build filters based on role
        order_filter = Q(customer_id=c.customer_id)
        received_filter = Q(customer_id=c.customer_id)
        
        # If NOT admin, restrict calculation to allowed stores only
        # If Admin, we do NOT apply store filter, so we see ALL transactions
        if not is_admin:
            order_filter &= Q(store_id__in=allowed_store_ids)
            received_filter &= Q(store_id__in=allowed_store_ids)

        # Total Orders Amount (Sales Activity)
        o_total = Order.objects.filter(order_filter).aggregate(t=Sum('total_amount'))['t'] or 0.0
        
        # Total Received Amount (Bill Acceptor / Payments)
        r_total = Received.objects.filter(received_filter).aggregate(t=Sum('amount'))['t'] or 0.0
        
        c.total_transitioned = o_total + r_total

    context = {
        'page_title': 'Customer Management',
        'username': username,
        'is_admin': is_admin,
        'is_merchant': is_merchant,
        'is_store_keeper': is_store_keeper,
        'customers': customers_list, # Pass the list with attached attributes
        'search_query': search_query
    }
    return render(request, 'reports/customers.html', context)