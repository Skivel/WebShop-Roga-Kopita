from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def shop(request):
    return render(request, 'main/shop.html')


def about(request):
    return render(request, 'main/about.html')
