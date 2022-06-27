# Generated by Django 4.0.4 on 2022-06-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_alter_order_citi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='citi',
            field=models.CharField(choices=[('crimea', 'АР Крим'), ('kharkiv', 'Харківська'), ('chernihiv', 'Чернігівська'), ('transcarpathian', 'Закарпатська'), ('odesa', 'Одеська'), ('kirovohrad', 'Кіровоградська'), ('poltava', 'Полтавська'), ('cherkasy', 'Черкаська'), ('kherson', 'Херсонська'), ('vinnytsia', 'Вінницька'), ('zaporizhzhia', 'Запорізька'), ('ternopil', 'Тернопільська'), ('zhytomyr', 'Житомирська'), ('chernivtsi', 'Чернівецька'), ('mykolayiv', 'Миколаївська'), ('kyiv', 'Київська'), ('dnipropetrovsk', 'Дніпропетровська'), ('rivne', 'Рівненська'), ('volyn', 'Волинська'), ('luhansk', 'Луганська'), ('khmelnytsky', 'Хмельницька'), ('lviv', 'Львівська'), ('sumy', 'Сумська'), ('donetsk', 'Донецька'), ('ivano-frankivsk', 'Івано-Франківська')], max_length=40, verbose_name='Область'),
        ),
    ]
