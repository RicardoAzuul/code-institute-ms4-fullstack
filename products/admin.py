from django.contrib import admin
from .models import Product_Category, Product, ShopAlert

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)


class Product_CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


class ShopAlertAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'text',
    )

    ordering = ('name',)


admin.site.register(Product_Category, Product_CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ShopAlert, ShopAlertAdmin)
