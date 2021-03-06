# Generated by Django 4.0.4 on 2022-06-26 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0036_alter_order_citi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='citi',
            field=models.CharField(choices=[('poltava', 'Полтавська'), ('ivano-frankivsk', 'Івано-Франківська'), ('kyiv', 'Київська'), ('volyn', 'Волинська'), ('kharkiv', 'Харківська'), ('luhansk', 'Луганська'), ('sumy', 'Сумська'), ('khmelnytsky', 'Хмельницька'), ('kherson', 'Херсонська'), ('rivne', 'Рівненська'), ('mykolayiv', 'Миколаївська'), ('kirovohrad', 'Кіровоградська'), ('transcarpathian', 'Закарпатська'), ('lviv', 'Львівська'), ('vinnytsia', 'Вінницька'), ('dnipropetrovsk', 'Дніпропетровська'), ('chernivtsi', 'Чернівецька'), ('cherkasy', 'Черкаська'), ('crimea', 'АР Крим'), ('chernihiv', 'Чернігівська'), ('zaporizhzhia', 'Запорізька'), ('zhytomyr', 'Житомирська'), ('donetsk', 'Донецька'), ('ternopil', 'Тернопільська'), ('odesa', 'Одеська')], max_length=40, verbose_name='Область'),
        ),
    ]
