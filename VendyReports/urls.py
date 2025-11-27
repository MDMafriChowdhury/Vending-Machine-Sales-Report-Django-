# VendyReports/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line sends all requests starting with '/reports/' to the reports app's urls.py
    path('reports/', include('reports.urls')), 
    
]