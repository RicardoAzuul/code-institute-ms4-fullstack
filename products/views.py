from multiprocessing import context
from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    # Get all products and store in products
    products = Product.objects.all()

    # Pass products to the context. This becomes available as a template variable.
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)