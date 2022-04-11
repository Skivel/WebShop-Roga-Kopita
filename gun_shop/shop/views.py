from django.shortcuts import render


def shop(request):
    return render(request, 'shop/shop.html')


def about(request):
    return render(request, 'main/about.html')
