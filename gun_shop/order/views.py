from django.shortcuts import render, redirect
from .models import Order
from .forms import PostOrder


def order(request):
    orders = Order.objects.all()
    if request.method == 'POST':
        form = PostOrder(request.POST)
        form.save()
        return redirect('../shop/')
    else:
        form = PostOrder
    return render(request, 'order/index.html', {'order': orders, 'form': form})
