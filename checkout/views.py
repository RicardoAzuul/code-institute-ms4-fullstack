from django.shortcuts import redirect, render, reverse

from checkout.forms import OrderForm
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    cart =  request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KkuhiBJzeXq1XU5sEXIBWCGvyVamO8fZLqItjzlEqCJQL7P2zQGQIAEQvH6EiRMnP7GpFg6DICehDSqvmUpd1qH00aBmy7eKl',
        'client-secret': 'test client secret',
    }

    return render(request, template, context)