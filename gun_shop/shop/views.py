from django.shortcuts import render
from .models import Products, Cart
from .forms import PostCart


def shop(request):
    products = Products.objects.all()
    cart = Cart.objects.all()
    initial_data = {
        'name': 'name',
        'price': 5.99,
        'quantity': '1',
        'total_price': 5.99
    }
    if request.method == 'POST':
        form = PostCart(request.POST, initial=initial_data)
        form.save()
    else:
        form = PostCart(initial=initial_data)
    mydict = {
        'products': products, 'form': form, 'cart': cart
    }
    return render(request, 'shop/shop.html', context=mydict)
