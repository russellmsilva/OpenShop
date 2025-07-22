from django.shortcuts import render
from .models import CartItem

def display_cart(request):
    if not request.user.is_authenticated:
        return render(request, 'cart.html', {'products_in_cart': []})
    cart_items = CartItem.objects.filter(buyer=request.user)
    return render(request, 'cart.html', {'products_in_cart': cart_items})
