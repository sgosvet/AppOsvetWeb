"""Projecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from Apps.AppSistemas.views.test.views import testView
from Apps.AppSistemas.views.category.views import *
from Apps.AppSistemas.views.zonas.views import *
from Apps.AppSistemas.views.products.views import *
from Apps.AppSistemas.views.client.views import *
from Apps.AppSistemas.views.sale.views import *
from Apps.AppSistemas.formsets import FormsetProduct


urlpatterns = [
    # category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    # client
    path('client/list/', ClientListView.as_view(), name='client_list'),
    path('client/add/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    # product
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    # Test Select anidados    
    path('test/', testView.as_view(), name='test'),
    path('testprod/', FormsetProduct.as_view(), name='prodformset'),
    
    # Sale
    path('sale/add/', SaleCreateView.as_view(), name='sale_create'),
    
    # OSVET - Zonas (Vistas basadas en clases)
    path('zonas/list/', ZonasListView.as_view(), name='zonas_list'),
    path('zonas/add/', ZonasCreateView.as_view(), name='zonas_create'),
    path('zonas/update/<int:pk>/', ZonasUpdateView.as_view(), name='zonas_update'),
    path('zonas/delete/<int:pk>/', ZonasDeleteView.as_view(), name='zonas_delete'),
    path('zonas/form/', ZonasFormView.as_view(), name='zonas_form'),
    
]
