from django.contrib import admin
from .models import Product_Category, Product

# Register your models here.
admin.site.register(Product_Category)
admin.site.register(Product)