from django.contrib import admin
from .models import Product_Category, Product, ShopAlert


class ProductAdmin(admin.ModelAdmin):
    """
    Registers the product model to the admin dashboard for CRUD operations
    """
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
    """
    Registers the product_category model to the admin dashboard for CRUD operations
    """
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


class ShopAlertAdmin(admin.ModelAdmin):
    """
    Registers the shop alert model to the admin dashboard for CRUD operations
    """
    list_display = (
        'name',
        'text',
    )

    ordering = ('name',)


admin.site.register(Product_Category, Product_CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ShopAlert, ShopAlertAdmin)
