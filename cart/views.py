from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse

# Create your views here.

def view_cart(request):
    """ A view to return the cart """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ A view to add items to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
    
    request.session['cart'] = cart

    return redirect(redirect_url)

def update_cart(request, item_id):
    """ A view to update items in the cart """

    print("update_cart")

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)
    
    request.session['cart'] = cart

    return redirect(reverse('view_cart'))

def remove_from_cart(request, item_id):
    """ A view to remove items from the cart """

    try:

        # TODO: if the cart is empty, we need to return the empty cart view
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        
        request.session['cart'] = cart

        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)