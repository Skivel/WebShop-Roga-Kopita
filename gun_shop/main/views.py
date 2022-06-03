from django.shortcuts import render
from gun_shop.shop.models import Products


def index(request):
    products = Products.objects.all()
    return render(request, 'main/index.html', {'products': products})


def about(request):
    return render(request, 'main/about.html')
