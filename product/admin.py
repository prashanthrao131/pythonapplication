from django.contrib import admin
from .models import Product, Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


# inherit from  ModelAdmin class in admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


# register
admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
