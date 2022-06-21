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
    }

    return render(request, template, context)