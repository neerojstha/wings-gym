from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """A view to renders the cart contents"""
    
    return render(request, 'cart/cart.html')
