from django.db import models
import PIL


class Products(models.Model):
    TOURISM = 'tourism'
    HUNT = 'hunt'

    CHOICE_GROUP = {
        (TOURISM, 'Туризм'),
        (HUNT, 'Полювання')
    }

    title = models.CharField('Назва товару', max_length=255)
    description = models.TextField('Опис')
    price = models.IntegerField('Ціна')
    vanish = models.BooleanField(default=False)
    img = models.ImageField(default='{% static "main/img/logo.jpg" %}', upload_to="static/main/img/products")
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default="Other")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
