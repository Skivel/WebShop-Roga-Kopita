# Generated by Django 4.0.4 on 2022-06-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_products_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='group',
            field=models.CharField(choices=[('hunt', 'Полювання'), ('closes', 'Одяг'), ('shoes', 'Взуття'), ('tourism', 'Туризм')], default='Other', max_length=20, verbose_name='Категорія'),
        ),
    ]
