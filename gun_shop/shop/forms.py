from django import forms
from .models import Cart


class PostCart(forms.ModelForm):
    class Meta:
        model = Cart
        fields = {
            'name',
            'price',
            'img_url',
            'quantity',
            'total_price'
            }

