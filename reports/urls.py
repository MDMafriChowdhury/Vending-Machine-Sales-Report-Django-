# reports/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Changed from '' to 'dashboard/' per your request
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # These remain the same, but now they won't have the /reports/ prefix
    path('stores/', views.stores_view, name='stores'),
    path('customers/', views.customers_view, name='customers'),
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]