from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def FAQ(request):
    return render(request, 'FAQ/FAQ.html')


def about(request):
    return render(request, 'main/about.html')
