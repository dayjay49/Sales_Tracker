"""LemonadeStand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from salesEntry.views import saleEntry_create_view, load_price, getSalesReport_view, postSalesReport_view
from pages.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls, name="admin_page"),
    path('sales/form/', saleEntry_create_view, name="sales_entry_form"),
    path('', home_view, name="home"),
    path('sales/report/', getSalesReport_view, name="get_sales_report"),
    path('sales/report/<int:staff_id>', postSalesReport_view, name="post_sales_report"),

    path('ajax/load-price/', load_price, name="ajax_load_price")
]
