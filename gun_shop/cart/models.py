from django.db import models


class Cart(models.Model):
    products = models.IntegerField("Товари")
    order_price = models.IntegerField("Сумма")

