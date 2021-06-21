from django.contrib import admin
from Apps.AppSistemas.models import Category, Zonas, Product, Client

# Register your models here.
admin.site.register(Category)
admin.site.register(Zonas)
admin.site.register(Product)
admin.site.register(Client)
