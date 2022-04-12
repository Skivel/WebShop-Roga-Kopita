from django.db import models


class Categories(models.Model):
    title = models.CharField('Назва категорії', max_length=255)
    slug = models.SlugField(max_length=55)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
