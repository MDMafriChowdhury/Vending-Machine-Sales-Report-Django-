# VendyReports/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Change 'reports/' to '' (empty string)
    path('', include('reports.urls')), 
]