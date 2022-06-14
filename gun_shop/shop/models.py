from django.db import models


class Products(models.Model):
    TOURISM = 'tourism'
    HUNT = 'hunt'
    SHOES = 'shoes'
    CLOSES = 'closes'

    CHOICE_GROUP = {
        (TOURISM, 'Туризм'),
        (HUNT, 'Полювання'),
        (SHOES, 'Взуття'),
        (CLOSES, 'Одяг')
    }

    name = models.CharField('Назва товару', max_length=255, db_index=True)
    description = models.TextField('Опис', max_length=1000, blank=True)
    price = models.DecimalField('Ціна', max_digits=10, decimal_places=2)
    vanish = models.BooleanField(default=True, verbose_name="Наявність")
    img = models.ImageField('Зображення', upload_to="static/shop/img/products", blank=True)
    group = models.CharField('Категорія', max_length=20, choices=CHOICE_GROUP, default="Other")
    slug = models.CharField(max_length=150, db_index=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
        index_together = (('id', 'slug'), )


class Cart(models.Model):
    name = models.CharField('Назва товару', max_length=255, db_index=True)
    price = models.DecimalField('Ціна товару', max_digits=10, decimal_places=2)
    img = models.ImageField('Зображення', upload_to="static/shop/img/cart", blank=True)
    quantity = models.IntegerField('Кількість')
    total_price = models.DecimalField('Загальна ціна', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"
