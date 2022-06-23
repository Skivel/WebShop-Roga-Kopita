from django.shortcuts import render
from .models import Products, Cart
from .forms import PostCart


def shop(request):
    products = Products.objects.all()
    cart = Cart.objects.all()
    if request.method == 'POST':
        form = PostCart(request.POST)
        form.save()
    else:
        form = PostCart()
    return render(request, 'shop/shop.html', {'products': products, 'form': form, 'cart': cart})
