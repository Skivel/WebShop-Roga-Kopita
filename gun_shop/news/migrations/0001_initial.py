# Generated by Django 4.0.4 on 2022-06-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Заголовок', max_length=50, verbose_name='Заголовок')),
                ('anons', models.CharField(max_length=255, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Текст поста')),
                ('date', models.DateTimeField(verbose_name='Дата публікації')),
            ],
            options={
                'verbose_name': 'Новина',
                'verbose_name_plural': 'Новини',
            },
        ),
    ]
