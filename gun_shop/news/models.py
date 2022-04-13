from django.db import models


class Articles(models.Model):
    title = models.CharField('Заголовок', max_length=50, default='Заголовок')
    anons = models.CharField('Анонс', max_length=255)
    full_text = models.TextField('Текст поста')
    date = models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
