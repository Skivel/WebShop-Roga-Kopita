# Generated by Django 4.0.4 on 2022-06-26 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0041_alter_order_citi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='citi',
            field=models.CharField(choices=[('rivne', 'Рівненська'), ('dnipropetrovsk', 'Дніпропетровська'), ('chernivtsi', 'Чернівецька'), ('chernihiv', 'Чернігівська'), ('kirovohrad', 'Кіровоградська'), ('khmelnytsky', 'Хмельницька'), ('mykolayiv', 'Миколаївська'), ('odesa', 'Одеська'), ('zaporizhzhia', 'Запорізька'), ('cherkasy', 'Черкаська'), ('poltava', 'Полтавська'), ('ivano-frankivsk', 'Івано-Франківська'), ('luhansk', 'Луганська'), ('lviv', 'Львівська'), ('sumy', 'Сумська'), ('kherson', 'Херсонська'), ('donetsk', 'Донецька'), ('zhytomyr', 'Житомирська'), ('volyn', 'Волинська'), ('vinnytsia', 'Вінницька'), ('transcarpathian', 'Закарпатська'), ('ternopil', 'Тернопільська'), ('kharkiv', 'Харківська'), ('kyiv', 'Київська'), ('crimea', 'АР Крим')], max_length=40, verbose_name='Область'),
        ),
    ]