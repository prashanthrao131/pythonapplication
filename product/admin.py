from django.contrib import admin
from .models import Product


#inherit from  ModelAdmin class in admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')


admin.site.register(Product, ProductAdmin)
