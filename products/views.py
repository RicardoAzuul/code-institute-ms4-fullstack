from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from .models import Product 
from django.conf import settings

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

def product_detail(request, product_id):
    """ A view to show product details """

    # Get a product model, identified by primary key = product_id
    product = get_object_or_404(Product, pk=product_id)

    # Pass product to the context. This becomes available as a template variable.
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)