# reports/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Maps http://127.0.0.1:8000/reports/ to the dashboard_view function
    path('', views.dashboard_view, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]