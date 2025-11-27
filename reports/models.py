# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Temptbl4Rf(models.Model):
    rfcodes = models.CharField(
        db_column='rfCodes',
        max_length=100,
        db_collation='utf8mb3_general_ci'
    )
    asl = models.AutoField(
        db_column='aSL',
        primary_key=True
    )

    class Meta:
        managed = False
        db_table = 'TempTbl4RF'



class Temptbl4Rfuser(models.Model):
    user_id = models.CharField(max_length=100, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False
        db_table = 'TempTbl4RFUser'


class AboutUs(models.Model):
    content_id = models.AutoField(primary_key=True)
    position = models.IntegerField()
    language_id = models.CharField(max_length=255)
    headline = models.TextField()
    icon = models.TextField()
    details = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'about_us'


class Accounts(models.Model):
    account_id = models.CharField(max_length=220)
    account_table_name = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accounts'


class Advertisement(models.Model):
    adv_id = models.CharField(primary_key=True, max_length=100)
    add_page = models.CharField(max_length=100, blank=True, null=True)
    adv_position = models.IntegerField()
    adv_code = models.TextField()
    adv_type = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'advertisement'


class BankAdd(models.Model):
    bank_id = models.CharField(primary_key=True, max_length=255)
    bank_name = models.CharField(max_length=255)
    ac_name = models.CharField(max_length=250, blank=True, null=True)
    ac_number = models.CharField(max_length=250, blank=True, null=True)
    branch = models.CharField(max_length=250, blank=True, null=True)
    signature_pic = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    default_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bank_add'


class Block(models.Model):
    block_id = models.CharField(primary_key=True, max_length=100)
    block_cat_id = models.CharField(max_length=100, blank=True, null=True)
    block_css = models.TextField(blank=True, null=True)
    block_position = models.IntegerField(blank=True, null=True)
    block_image = models.CharField(max_length=255, blank=True, null=True)
    block_style = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block'


class Brand(models.Model):
    brand_id = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255)
    brand_image = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'brand'


class Campaigns(models.Model):
    id = models.IntegerField(primary_key=True)
    discount_percentage = models.FloatField(blank=True, null=True)
    discounted_price = models.FloatField(blank=True, null=True)
    vendy_store_ids = models.JSONField()
    max_number_of_sales = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField()
    already_sold = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaigns'


class Cardpayment(models.Model):
    cardpayment_id = models.CharField(max_length=100)
    invoice_id = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    terminal_id = models.CharField(max_length=100)
    card_type = models.CharField(max_length=255)
    card_no = models.CharField(max_length=100)
    amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cardpayment'


class CategoryVariant(models.Model):
    category_id = models.CharField(max_length=255, db_collation='utf8mb3_general_ci')
    variant_id = models.CharField(max_length=255, db_collation='utf8mb3_general_ci')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'category_variant'


class CheckOut(models.Model):
    check_out_id = models.CharField(primary_key=True, max_length=100)
    session_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    variant_id = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    total_price = models.FloatField()
    ip = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'check_out'


class ChequeManger(models.Model):
    cheque_id = models.CharField(primary_key=True, max_length=100)
    transection_id = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    bank_id = models.CharField(max_length=100)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.CharField(max_length=100)
    cheque_no = models.CharField(max_length=100)
    date = models.CharField(max_length=100, blank=True, null=True)
    transection_type = models.CharField(max_length=100)
    cheque_status = models.IntegerField()
    amount = models.FloatField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cheque_manger'


class ColorBackends(models.Model):
    color1 = models.CharField(max_length=20)
    color2 = models.CharField(max_length=20)
    color3 = models.CharField(max_length=20)
    color4 = models.CharField(max_length=20)
    color5 = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'color_backends'


class ColorFrontends(models.Model):
    color1 = models.CharField(max_length=20)
    color2 = models.CharField(max_length=20)
    color3 = models.CharField(max_length=20)
    color4 = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'color_frontends'


class CompanyInformation(models.Model):
    company_id = models.CharField(primary_key=True, max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.TextField()
    mobile = models.CharField(max_length=255)
    website = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_information'


class Contact(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact'


class Countries(models.Model):
    sortname = models.CharField(max_length=3)
    name = models.CharField(max_length=150)
    phonecode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'countries'


class Coupon(models.Model):
    coupon_id = models.CharField(primary_key=True, max_length=100)
    coupon_name = models.CharField(max_length=100)
    coupon_discount_code = models.CharField(max_length=100)
    discount_amount = models.FloatField(blank=True, null=True)
    discount_percentage = models.CharField(max_length=20, blank=True, null=True)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    discount_type = models.IntegerField(blank=True, null=True, db_comment='1=Taka,2=Percentage')
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coupon'


class CouponInvoice(models.Model):
    coupon_invoice_id = models.CharField(primary_key=True, max_length=100)
    invoice_id = models.CharField(max_length=100)
    coupon_code = models.CharField(max_length=100)
    date_of_apply = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'coupon_invoice'


class CryptoPayments(models.Model):
    paymentid = models.AutoField(db_column='paymentID', primary_key=True)  # Field name made lowercase.
    boxid = models.PositiveIntegerField(db_column='boxID')  # Field name made lowercase.
    boxtype = models.CharField(db_column='boxType', max_length=10)  # Field name made lowercase.
    orderid = models.CharField(db_column='orderID', max_length=50)  # Field name made lowercase.
    userid = models.CharField(db_column='userID', max_length=50)  # Field name made lowercase.
    countryid = models.CharField(db_column='countryID', max_length=3)  # Field name made lowercase.
    coinlabel = models.CharField(db_column='coinLabel', max_length=6)  # Field name made lowercase.
    amount = models.FloatField()
    amountusd = models.FloatField(db_column='amountUSD')  # Field name made lowercase.
    unrecognised = models.PositiveIntegerField()
    addr = models.CharField(max_length=34)
    txid = models.CharField(db_column='txID', max_length=64)  # Field name made lowercase.
    txdate = models.DateTimeField(db_column='txDate', blank=True, null=True)  # Field name made lowercase.
    txconfirmed = models.PositiveIntegerField(db_column='txConfirmed')  # Field name made lowercase.
    txcheckdate = models.DateTimeField(db_column='txCheckDate', blank=True, null=True)  # Field name made lowercase.
    processed = models.PositiveIntegerField()
    processeddate = models.DateTimeField(db_column='processedDate', blank=True, null=True)  # Field name made lowercase.
    recordcreated = models.DateTimeField(db_column='recordCreated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crypto_payments'
        unique_together = (('boxid', 'orderid', 'userid', 'txid', 'amount', 'addr'),)


class CurrencyInfo(models.Model):
    currency_id = models.CharField(primary_key=True, max_length=255)
    currency_name = models.CharField(max_length=255)
    currency_icon = models.TextField()
    currency_position = models.IntegerField()
    convertion_rate = models.FloatField()
    default_status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'currency_info'


class CustomerInformation(models.Model):
    customer_id = models.CharField(max_length=250)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    customer_short_address = models.TextField(blank=True, null=True)
    customer_address_1 = models.TextField(blank=True, null=True)
    customer_address_2 = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    customer_mobile = models.CharField(max_length=100, blank=True, null=True)
    customer_email = models.CharField(max_length=255, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, db_comment='1=paid,2=credit')
    user_id = models.CharField(max_length=255, blank=True, null=True)
    created_from = models.IntegerField(blank=True, null=True)
    is_customer_golobal = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    customer_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_information'


class CustomerLedger(models.Model):
    transaction_id = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    invoice_no = models.CharField(max_length=100, blank=True, null=True)
    quotation_no = models.CharField(max_length=100, blank=True, null=True)
    order_no = models.CharField(max_length=100, blank=True, null=True)
    receipt_no = models.CharField(max_length=100, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    payment_type = models.CharField(max_length=255, blank=True, null=True)
    cheque_no = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_ledger'


class CustomerOrder(models.Model):
    customer_order_id = models.CharField(primary_key=True, max_length=100)
    customer_id = models.CharField(max_length=100)
    shiping_id = models.CharField(max_length=100)
    order_date = models.DateTimeField()
    payment_method = models.CharField(max_length=100)
    total_bill = models.FloatField()
    order_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer_order'


class CustomerOrderDetails(models.Model):
    c_o_d_id = models.CharField(max_length=100)
    customer_order_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    variant_id = models.CharField(max_length=100)
    quantity = models.IntegerField()
    discount = models.FloatField()
    tax = models.FloatField()
    vat = models.FloatField()
    sell_price = models.FloatField()
    supplier_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'customer_order_details'


class DailyClosing(models.Model):
    closing_id = models.CharField(max_length=255)
    store_id = models.CharField(max_length=255)
    last_day_closing = models.FloatField()
    cash_in = models.FloatField()
    cash_out = models.FloatField()
    date = models.CharField(primary_key=True, max_length=250)
    amount = models.FloatField()
    adjustment = models.FloatField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'daily_closing'


class EmailConfiguration(models.Model):
    email_id = models.CharField(primary_key=True, max_length=100)
    protocol = models.CharField(max_length=100, blank=True, null=True)
    mailtype = models.CharField(max_length=100)
    smtp_host = models.CharField(max_length=100, blank=True, null=True)
    smtp_port = models.IntegerField()
    sender_email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'email_configuration'


class ImageGallery(models.Model):
    image_gallery_id = models.CharField(primary_key=True, max_length=100)
    product_id = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)
    img_thumb = models.TextField()

    class Meta:
        managed = False
        db_table = 'image_gallery'


class Invoice(models.Model):
    invoice_id = models.CharField(max_length=100)
    quotation_id = models.CharField(max_length=100, blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    customer_id = models.CharField(max_length=100)
    store_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=100)
    total_amount = models.FloatField()
    invoice = models.CharField(max_length=255)
    total_discount = models.FloatField(blank=True, null=True)
    invoice_discount = models.FloatField(blank=True, null=True, db_comment='total_discount + invoice_discount')
    service_charge = models.FloatField(blank=True, null=True)
    shipping_charge = models.IntegerField(blank=True, null=True)
    shipping_method = models.CharField(max_length=255, blank=True, null=True)
    paid_amount = models.FloatField(blank=True, null=True)
    due_amount = models.FloatField(blank=True, null=True)
    invoice_details = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    invoice_status = models.IntegerField(db_comment='1=shipped,2=cancel,3=pending,4=complete,5=processing,6=return')
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice'


class InvoiceDetails(models.Model):
    invoice_details_id = models.CharField(primary_key=True, max_length=100)
    invoice_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    variant_id = models.CharField(max_length=100)
    store_id = models.CharField(max_length=100)
    quantity = models.IntegerField()
    rate = models.FloatField()
    supplier_rate = models.FloatField(blank=True, null=True)
    total_price = models.FloatField()
    discount = models.FloatField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_details'


class Language(models.Model):
    phrase = models.TextField()
    english = models.TextField(blank=True, null=True)
    bangla = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'language'


class LinkPage(models.Model):
    link_page_id = models.CharField(primary_key=True, max_length=100)
    page_id = models.CharField(max_length=255)
    language_id = models.CharField(max_length=255)
    headlines = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    details = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'link_page'


class Order(models.Model):
    order_id = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    store_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=100)
    total_amount = models.FloatField(blank=True, null=True)
    order = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    total_discount = models.FloatField(blank=True, null=True)
    order_discount = models.FloatField(blank=True, null=True, db_comment='total_discount + order_discount')
    service_charge = models.FloatField(blank=True, null=True)
    paid_amount = models.FloatField(blank=True, null=True)
    due_amount = models.FloatField(blank=True, null=True)
    file_path = models.TextField(blank=True, null=True)
    coupon = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    trxid = models.CharField(max_length=128, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class OrderDelivery(models.Model):
    order_delivery_id = models.CharField(max_length=255)
    delivery_id = models.CharField(max_length=255)
    order_id = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_delivery'


class OrderDetails(models.Model):
    order_details_id = models.CharField(primary_key=True, max_length=100)
    order_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    variant_id = models.CharField(max_length=100)
    store_id = models.CharField(max_length=255)
    quantity = models.IntegerField()
    rate = models.FloatField()
    supplier_rate = models.FloatField(blank=True, null=True)
    total_price = models.FloatField()
    discount = models.FloatField(blank=True, null=True, db_comment='discount_total_per_product')
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_details'


class OrderPayment(models.Model):
    order_payment_id = models.CharField(max_length=255)
    payment_id = models.CharField(max_length=255)
    order_id = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_payment'


class OrderTaxColDetails(models.Model):
    order_tax_col_de_id = models.CharField(primary_key=True, max_length=100)
    order_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    variant_id = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'order_tax_col_details'


class OrderTaxColSummary(models.Model):
    order_tax_col_id = models.CharField(primary_key=True, max_length=100)
    order_id = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=100)
    tax_amount = models.FloatField()
    date = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'order_tax_col_summary'


class OurLocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    language_id = models.CharField(max_length=255)
    headline = models.TextField()
    details = models.TextField()
    position = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'our_location'


class PayWiths(models.Model):
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pay_withs'


class PayeerPayments(models.Model):
    m_operation_id = models.IntegerField()
    m_operation_ps = models.IntegerField()
    m_operation_date = models.CharField(max_length=100)
    m_operation_pay_date = models.CharField(max_length=100)
    m_shop = models.IntegerField()
    m_orderid = models.CharField(max_length=300)
    m_amount = models.CharField(max_length=100)
    m_curr = models.CharField(max_length=100)
    m_desc = models.CharField(max_length=300)
    m_status = models.CharField(max_length=100)
    m_sign = models.TextField()
    lang = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'payeer_payments'


class Payment(models.Model):
    transection_id = models.CharField(max_length=200)
    tracing_id = models.CharField(max_length=200)
    account_id = models.CharField(max_length=200)
    store_id = models.CharField(max_length=200)
    user_id = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=10)
    date = models.CharField(max_length=100)
    amount = models.FloatField()
    description = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payment'


class PaymentGateway(models.Model):
    agent = models.CharField(max_length=100)
    public_key = models.CharField(max_length=100)
    private_key = models.CharField(max_length=100)
    shop_id = models.CharField(max_length=100)
    secret_key = models.CharField(max_length=100)
    paypal_email = models.CharField(max_length=250, blank=True, null=True)
    paypal_client_id = models.TextField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payment_gateway'


class ProductCategory(models.Model):
    category_id = models.CharField(max_length=255, blank=True, null=True)
    parent_category_id = models.CharField(max_length=255, blank=True, null=True)
    category_name = models.CharField(max_length=255, blank=True, null=True)
    top_menu = models.IntegerField()
    menu_pos = models.IntegerField()
    cat_image = models.TextField()
    cat_favicon = models.TextField(blank=True, null=True)
    cat_type = models.IntegerField(blank=True, null=True, db_comment='1=parent,2=sub caregory')
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductInformation(models.Model):
    product_id = models.CharField( max_length=100)
    supplier_id = models.CharField(max_length=255)
    category_id = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255)
    price = models.FloatField()
    supplier_price = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=100, blank=True, null=True)
    product_model = models.CharField( max_length=100)
    product_details = models.TextField(blank=True, null=True)
    image_thumb = models.TextField(blank=True, null=True)
    brand_id = models.CharField(max_length=255, blank=True, null=True)
    variants = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    best_sale = models.IntegerField()
    onsale = models.IntegerField()
    onsale_price = models.FloatField(blank=True, null=True)
    invoice_details = models.TextField(blank=True, null=True)
    image_large_details = models.TextField()
    review = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True)
    specification = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    product_position = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_information'


class ProductPurchase(models.Model):
    purchase_id = models.CharField(max_length=100)
    invoice_no = models.CharField(max_length=100)
    supplier_id = models.CharField(max_length=100)
    store_id = models.CharField(max_length=255, blank=True, null=True)
    dispencer_id = models.IntegerField(blank=True, null=True)
    wearhouse_id = models.CharField(max_length=255, blank=True, null=True)
    grand_total_amount = models.FloatField()
    purchase_date = models.CharField(max_length=50)
    purchase_details = models.TextField()
    user_id = models.CharField(max_length=100)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_purchase'


class ProductPurchaseDetails(models.Model):
    purchase_detail_id = models.CharField(max_length=100)
    purchase_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    variant_id = models.CharField(max_length=100)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    dispencer_id = models.IntegerField()
    wearhouse_id = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField()
    notification_quantity = models.IntegerField(blank=True, null=True)
    rate = models.FloatField()
    total_amount = models.FloatField()
    status = models.IntegerField()
    purchase_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_purchase_details'


class ProductReview(models.Model):
    product_review_id = models.CharField(primary_key=True, max_length=100)
    product_id = models.IntegerField(blank=True, null=True)
    reviewer_id = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    rate = models.CharField(max_length=100, blank=True, null=True)
    date_time = models.DateTimeField()
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_review'


class Quotation(models.Model):
    quotation_id = models.CharField(primary_key=True, max_length=100)
    customer_id = models.CharField(max_length=100)
    store_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    total_amount = models.FloatField()
    quotation = models.CharField(max_length=255)
    details = models.TextField()
    total_discount = models.FloatField(blank=True, null=True)
    quotation_discount = models.FloatField(db_comment='total_discount + quotation_discount')
    service_charge = models.FloatField(blank=True, null=True)
    paid_amount = models.FloatField()
    due_amount = models.FloatField()
    file_path = models.TextField(blank=True, null=True)
    status = models.IntegerField(db_comment='1=not_invoice,2=invoiced')

    class Meta:
        managed = False
        db_table = 'quotation'


class QuotationDetails(models.Model):
    quotation_details_id = models.CharField(primary_key=True, max_length=100)
    quotation_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    variant_id = models.CharField(max_length=100)
    store_id = models.CharField(max_length=100)
    quantity = models.IntegerField()
    rate = models.FloatField()
    supplier_rate = models.FloatField(blank=True, null=True)
    total_price = models.FloatField()
    discount = models.FloatField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quotation_details'


class QuotationTaxColDetails(models.Model):
    quot_tax_col_de_id = models.CharField(primary_key=True, max_length=100)
    quotation_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    variant_id = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'quotation_tax_col_details'


class QuotationTaxColSummary(models.Model):
    quot_tax_col_id = models.CharField(primary_key=True, max_length=100)
    quotation_id = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=100)
    tax_amount = models.FloatField()
    date = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'quotation_tax_col_summary'


class Received(models.Model):
    transection_id = models.CharField(max_length=200)
    customer_id = models.CharField(max_length=200)
    account_id = models.CharField(max_length=200)
    store_id = models.CharField(max_length=200)
    user_id = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    amount = models.FloatField()
    description = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'received'


class ShippingInfo(models.Model):
    shiping_info_id = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=100)
    order_id = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    customer_short_address = models.TextField()
    customer_address_1 = models.TextField(blank=True, null=True)
    customer_address_2 = models.TextField(blank=True, null=True)
    customer_mobile = models.CharField(max_length=255)
    customer_email = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping_info'


class ShippingMethod(models.Model):
    method_id = models.AutoField(primary_key=True)
    method_name = models.CharField(max_length=255)
    details = models.TextField()
    charge_amount = models.FloatField()
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shipping_method'


class Slider(models.Model):
    slider_id = models.CharField(primary_key=True, max_length=100)
    slider_link = models.CharField(max_length=255)
    slider_image = models.CharField(max_length=255)
    slider_position = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'slider'


class SmsConfiguration(models.Model):
    gateway = models.CharField(max_length=255)
    user_name = models.CharField(max_length=100)
    userid = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    status = models.IntegerField()
    link = models.CharField(max_length=255)
    sms_from = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sms_configuration'


class SmsTemplate(models.Model):
    template_name = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    status = models.IntegerField()
    default_status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sms_template'


class SoftSetting(models.Model):
    setting_id = models.AutoField(primary_key=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    invoice_logo = models.CharField(max_length=255, blank=True, null=True)
    favicon = models.CharField(max_length=255, blank=True, null=True)
    footer_text = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    rtr = models.CharField(max_length=255, blank=True, null=True)
    captcha = models.IntegerField(blank=True, null=True, db_comment='0=active,1=inactive')
    site_key = models.CharField(max_length=250, blank=True, null=True)
    secret_key = models.CharField(max_length=250, blank=True, null=True)
    sms_service = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'soft_setting'


class States(models.Model):
    name = models.CharField(max_length=30)
    country_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'states'


class StoreMerchant(models.Model):
    store_id = models.CharField(primary_key=True, max_length=30)
    merchant_id = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'store_merchant'


class StoreProduct(models.Model):
    store_product_id = models.CharField(primary_key=True, max_length=100)
    store_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    variant_id = models.CharField(max_length=100)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'store_product'


class StoreSet(models.Model):
    pk = models.CompositePrimaryKey('store_id', 'store_code')
    store_id = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
    store_address = models.TextField()
    default_status = models.IntegerField(db_comment='0=inactive,1=active')
    store_code = models.CharField( max_length=100)
    vendy_store_id = models.CharField(max_length=100, blank=True, null=True)
    vendy_store_key = models.CharField(max_length=100, blank=True, null=True)
    protocol_id = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    ssid = models.CharField(max_length=100, blank=True, null=True)
    wifi_password = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    activation_date = models.DateTimeField(blank=True, null=True)
    last_response_time = models.DateTimeField(blank=True, null=True)
    merchant_id = models.CharField(max_length=100, blank=True, null=True)
    machine_type = models.CharField(max_length=100, blank=True, null=True)
    machine_version = models.CharField(max_length=100, blank=True, null=True)
    store_image = models.CharField(max_length=500, blank=True, null=True)
    store_large_image = models.CharField(max_length=500, blank=True, null=True)
    dispencer_amount = models.IntegerField()
    preferred_payment_gateway_ids = models.JSONField(blank=True, null=True)
    notificaitonchannels = models.TextField(db_column='notificaitonChannels', blank=True, null=True)  # Field name made lowercase.
    machine_mac_address = models.CharField(max_length=50, blank=True, null=True)
    machine_setup_info = models.TextField(blank=True, null=True)
    installation_location = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store_set'


class Subscriber(models.Model):
    subscriber_id = models.CharField(primary_key=True, max_length=100)
    apply_ip = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscriber'


class SupplierInformation(models.Model):
    supplier_id = models.CharField(primary_key=True, max_length=100)
    supplier_name = models.CharField(max_length=255)
    address = models.TextField()
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=50, blank=True, null=True)
    details = models.TextField()
    website = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'supplier_information'


class SupplierLedger(models.Model):
    transaction_id = models.CharField(primary_key=True, max_length=100)
    purchase_id = models.CharField(max_length=100, blank=True, null=True)
    supplier_id = models.CharField(max_length=100)
    invoice_no = models.CharField(max_length=100, blank=True, null=True)
    deposit_no = models.CharField(max_length=50, blank=True, null=True)
    amount = models.FloatField()
    description = models.TextField(blank=True, null=True)
    payment_type = models.CharField(max_length=255, blank=True, null=True)
    cheque_no = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=50)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'supplier_ledger'


class SynchronizerSetting(models.Model):
    hostname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    port = models.CharField(max_length=10)
    debug = models.CharField(max_length=10)
    project_root = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'synchronizer_setting'


class Tax(models.Model):
    tax_id = models.CharField(primary_key=True, max_length=100)
    tax_name = models.CharField(max_length=100)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax'


class TaxCollectionDetails(models.Model):
    tax_col_de_id = models.CharField(primary_key=True, max_length=100)
    invoice_id = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=100)
    variant_id = models.CharField(max_length=255)
    amount = models.FloatField()
    date = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tax_collection_details'


class TaxCollectionSummary(models.Model):
    tax_collection_id = models.CharField(primary_key=True, max_length=100)
    invoice_id = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=100)
    tax_amount = models.FloatField()
    date = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tax_collection_summary'


class TaxProductService(models.Model):
    t_p_s_id = models.CharField(primary_key=True, max_length=100)
    product_id = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=100)
    tax_percentage = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tax_product_service'


class TblCreditTransection(models.Model):
    transaction_id = models.CharField(max_length=100)
    credit_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    transaction_amount = models.IntegerField()
    transaction_type = models.CharField(max_length=100)
    transaction_datetime = models.DateTimeField(db_column='transaction_dateTime')  # Field name made lowercase.
    transection_method = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_credit_transection'


class TblDispencer(models.Model):
    dispencer_id = models.AutoField(primary_key=True)
    store_id = models.CharField(max_length=100)
    dispencer_position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_dispencer'


class TblMqttRequestLog(models.Model):
    order_id = models.CharField(max_length=128)
    topic = models.CharField(max_length=128, blank=True, null=True)
    trxid = models.CharField(max_length=128, blank=True, null=True)
    mqtt_response = models.TextField(blank=True, null=True)
    mqtt_request = models.TextField(blank=True, null=True)
    datatime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_mqtt_request_log'


class TblNotification(models.Model):
    from_field = models.CharField(db_column='from', max_length=128, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=128, blank=True, null=True)
    cc = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=128)
    user_instance = models.CharField(max_length=128, blank=True, null=True, db_comment='user instance for push notification. ')
    subject_or_heading = models.CharField(max_length=512, blank=True, null=True)
    body = models.CharField(max_length=1024)
    notification_type = models.IntegerField()
    is_successfull = models.IntegerField(blank=True, null=True)
    secondary_response = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_notification'


class TblPin(models.Model):
    allocated_to_machines = models.JSONField(blank=True, null=True)
    hash_code = models.CharField(max_length=10, db_collation='utf8mb4_unicode_ci')
    serial_number = models.CharField(max_length=20)
    pin_flag = models.IntegerField()
    generate_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    money_value = models.FloatField()
    currency_id = models.CharField(max_length=15, db_collation='utf8mb4_unicode_ci')
    transaction_date = models.DateTimeField(blank=True, null=True)
    is_global = models.IntegerField()
    used_in_machine_id = models.CharField(max_length=10, blank=True, null=True)
    used_in_dispenser_id = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_pin'


class TblPinFlags(models.Model):
    type = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'tbl_pin_flags'


class TblProtocol(models.Model):
    protocol_id = models.AutoField(primary_key=True)
    protocol_name = models.CharField(max_length=100)
    protocol_url = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'tbl_protocol'


class TblSessionData(models.Model):
    session_data = models.TextField(blank=True, null=True)
    trxid = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_session_data'


class TblUserAuthenticationRelation(models.Model):
    authentication_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    authentication_type_id = models.CharField(max_length=100)
    auth_value_hash = models.CharField(max_length=100)
    hash_accuracy_range = models.CharField(max_length=100)
    is_active = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_user_authentication_relation'


class TblUserAuthenticationType(models.Model):
    auth_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user_authentication_type'


class TblUserCredit(models.Model):
    credit_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    credit_type = models.CharField(max_length=100)
    credit = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True)
    debit = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    balance = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True)
    acc_status = models.IntegerField()
    currency_id = models.CharField(max_length=100)
    transaction = models.IntegerField()
    transaction_datetime = models.DateTimeField()
    is_global = models.IntegerField()
    authentication_type = models.IntegerField()
    is_active = models.IntegerField()
    auto_renewal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_user_credit'


class TblUserCreditType(models.Model):
    credit_type = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'tbl_user_credit_type'


class TblUserMarchentStoreRelation(models.Model):
    authentication_id = models.CharField(max_length=100)
    marchent_id = models.CharField(max_length=100, blank=True, null=True)
    store_id = models.CharField(max_length=100)
    is_allow = models.IntegerField()
    is_restricted = models.IntegerField()
    is_global = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_user_marchent_store_relation'


class TblUserStores(models.Model):
    user_id = models.CharField(max_length=255)
    store_id = models.CharField(max_length=255)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_user_stores'


class TerminalPayment(models.Model):
    pay_terminal_id = models.CharField(max_length=100)
    terminal_name = models.CharField(max_length=100)
    terminal_provider_company = models.CharField(max_length=250)
    linked_bank_account_no = models.CharField(max_length=100)
    customer_care_phone_no = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'terminal_payment'


class Themes(models.Model):
    name = models.CharField(max_length=255)
    status = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'themes'


class Transfer(models.Model):
    id = models.AutoField(primary_key=True)  # real DB PK
    transfer_id = models.CharField(max_length=100)
    store_id = models.CharField(max_length=100, blank=True, null=True)
    warehouse_id = models.CharField(max_length=100, blank=True, null=True)
    product_id = models.CharField(max_length=100)
    variant_id = models.CharField(max_length=100)
    quantity = models.FloatField()
    notification_quantity = models.IntegerField(blank=True, null=True)
    t_store_id = models.CharField(max_length=100, blank=True, null=True)
    t_warehouse_id = models.CharField(max_length=100, blank=True, null=True)
    purchase_id = models.CharField(max_length=100, blank=True, null=True)
    date_time = models.CharField(max_length=100)
    transfer_by = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(
        db_comment='1=store to store,2=store to warehouse,3=warehouse to store,4=warehouse to warehouse,5=purchase'
    )

    class Meta:
        managed = False
        db_table = 'transfer'



class Unit(models.Model):
    unit_id = models.CharField(primary_key=True, max_length=100)
    unit_name = models.CharField(max_length=255)
    unit_short_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'unit'


class UserLogin(models.Model):
    user_id = models.CharField(primary_key=True, max_length=100)
    store_id = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    contact_no = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.IntegerField(db_comment='1=admin,2=shop-manager,3=sales man,4=store keeper,5=customer')
    security_code = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    delete_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_login'


class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=100)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    date_of_birth = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class Variant(models.Model):
    variant_id = models.CharField(primary_key=True, max_length=100)
    variant_name = models.CharField(max_length=100)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'variant'


class WearhouseSet(models.Model):
    wearhouse_id = models.CharField(primary_key=True, max_length=100)
    user_id = models.CharField(max_length=100)
    wearhouse_name = models.CharField(max_length=100)
    wearhouse_address = models.TextField()

    class Meta:
        managed = False
        db_table = 'wearhouse_set'


class WebFooter(models.Model):
    footer_section_id = models.CharField(primary_key=True, max_length=100)
    headlines = models.TextField()
    details = models.TextField()
    position = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'web_footer'


class WebSetting(models.Model):
    setting_id = models.AutoField(primary_key=True)
    logo = models.TextField(blank=True, null=True)
    invoice_logo = models.TextField(blank=True, null=True)
    favicon = models.TextField(blank=True, null=True)
    footer_logo = models.TextField(blank=True, null=True)
    footer_text = models.TextField(blank=True, null=True)
    footer_details = models.TextField(blank=True, null=True)
    google_analytics = models.TextField(blank=True, null=True)
    facebook_messenger = models.TextField(blank=True, null=True)
    qr_status = models.IntegerField(db_comment='Active=1, Inactive=0')
    app_link_status = models.IntegerField()
    pay_with_status = models.IntegerField(db_comment='1=active , 0=inactive')
    map_api_key = models.TextField(blank=True, null=True)
    map_latitude = models.TextField(blank=True, null=True)
    map_langitude = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_setting'


class WebsiteContent(models.Model):
    web_content_id = models.AutoField(primary_key=True)
    content_id = models.CharField(max_length=255)
    language_id = models.CharField(max_length=255)
    content_headline = models.TextField()
    content_image = models.TextField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'website_content'


class Wishlist(models.Model):
    wishlist_id = models.CharField(primary_key=True, max_length=100)
    product_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wishlist'
