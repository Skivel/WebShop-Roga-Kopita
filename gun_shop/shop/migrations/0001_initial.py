# Generated by Django 4.0.4 on 2022-05-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Назва товару')),
                ('description', models.TextField(verbose_name='Опис')),
                ('price', models.IntegerField(verbose_name='Ціна')),
                ('vanish', models.BooleanField(default=False)),
                ('img', models.ImageField(upload_to='products')),
                ('group', models.CharField(choices=[('tourism', 'Туризм'), ('hunt', 'Полювання')], default='Other', max_length=20)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
            },
        ),
    ]