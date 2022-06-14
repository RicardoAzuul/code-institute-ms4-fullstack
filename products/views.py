from multiprocessing import context
from unicodedata import category
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Product_Category 
from django.conf import settings

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    # Get all products and store in products
    products = Product.objects.all()
    # set to None in case of no search term or category
    query = None
    categories = None

    # Logic to handle search = GET requests
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Product_Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search terms entered.")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    # Pass products to the context. This becomes available as a template variable.
    context = {
        'products': products,
        'search_term': query,
        'selected_categories': categories,
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