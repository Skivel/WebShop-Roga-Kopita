# Generated by Django 4.0.4 on 2022-06-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0024_alter_order_citi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='citi',
            field=models.CharField(choices=[('cherkasy', 'Черкаська'), ('kherson', 'Херсонська'), ('khmelnytsky', 'Хмельницька'), ('kyiv', 'Київська'), ('dnipropetrovsk', 'Дніпропетровська'), ('luhansk', 'Луганська'), ('zaporizhzhia', 'Запорізька'), ('chernihiv', 'Чернігівська'), ('lviv', 'Львівська'), ('ivano-frankivsk', 'Івано-Франківська'), ('vinnytsia', 'Вінницька'), ('transcarpathian', 'Закарпатська'), ('kharkiv', 'Харківська'), ('kirovohrad', 'Кіровоградська'), ('rivne', 'Рівненська'), ('chernivtsi', 'Чернівецька'), ('donetsk', 'Донецька'), ('odesa', 'Одеська'), ('sumy', 'Сумська'), ('crimea', 'АР Крим'), ('volyn', 'Волинська'), ('ternopil', 'Тернопільська'), ('zhytomyr', 'Житомирська'), ('poltava', 'Полтавська'), ('mykolayiv', 'Миколаївська')], max_length=40, verbose_name='Область'),
        ),
    ]
