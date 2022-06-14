from django.shortcuts import render
from .models import Products, Cart


def shop(request):
    products = Products.objects.all()
    cart = Cart.objects.all()
    return render(request, 'shop/shop.html', {'products': products, 'cart': cart})
