# Generated by Django 4.0.4 on 2022-06-26 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0037_alter_order_citi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='citi',
            field=models.CharField(choices=[('kirovohrad', 'Кіровоградська'), ('zhytomyr', 'Житомирська'), ('cherkasy', 'Черкаська'), ('sumy', 'Сумська'), ('rivne', 'Рівненська'), ('kherson', 'Херсонська'), ('poltava', 'Полтавська'), ('chernivtsi', 'Чернівецька'), ('khmelnytsky', 'Хмельницька'), ('odesa', 'Одеська'), ('zaporizhzhia', 'Запорізька'), ('dnipropetrovsk', 'Дніпропетровська'), ('kyiv', 'Київська'), ('lviv', 'Львівська'), ('vinnytsia', 'Вінницька'), ('crimea', 'АР Крим'), ('kharkiv', 'Харківська'), ('volyn', 'Волинська'), ('mykolayiv', 'Миколаївська'), ('donetsk', 'Донецька'), ('ivano-frankivsk', 'Івано-Франківська'), ('luhansk', 'Луганська'), ('ternopil', 'Тернопільська'), ('chernihiv', 'Чернігівська'), ('transcarpathian', 'Закарпатська')], max_length=40, verbose_name='Область'),
        ),
    ]
