from django.shortcuts import render

from .models import Products


def shop(request):
    products = Products.objects.all()
    return render(request, 'shop/shop.html', {'products': products})
