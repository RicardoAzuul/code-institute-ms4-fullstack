from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Product_Category, ShopAlert
from django.contrib.auth.decorators import login_required

from .forms import ProductForm


# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    # Retrieve just textfields, convert to string and append to list so we can use Django's random template variable
    shop_alerts_textfields = ShopAlert.objects.all().values_list('text')
    shop_alerts_textstrings = []
    for x in shop_alerts_textfields:
        shop_alerts_textstrings.append(''.join(x))

    # set to None in case of no search term or category
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Product_Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search terms entered.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    selected_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'shop_alerts_textstrings': shop_alerts_textstrings,
        'search_term': query,
        'selected_categories': categories,
        'selected_sorting': selected_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product-detail.html', context)


@login_required
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Super User permissions required')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure form is valid.')
    else:
        form = ProductForm()

    template = 'products/add-product.html'
    context = {
        'form': form,
        'disable_add_to_bag': True,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Update a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Super User permissions required')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. \
                    Please ensure form is valid.')
    else:
        form = ProductForm(instance=product)
    messages.info(request, f'Editing {product.name}')

    template = 'products/edit-product.html'
    context = {
        'form': form,
        'product': product,
        'disable_add_to_bag': True,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Super User permissions required')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('products'))
