# Generated by Django 4.0.4 on 2022-06-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_alter_order_citi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='citi',
            field=models.CharField(choices=[('cherkasy', 'Черкаська'), ('vinnytsia', 'Вінницька'), ('kharkiv', 'Харківська'), ('zaporizhzhia', 'Запорізька'), ('lviv', 'Львівська'), ('poltava', 'Полтавська'), ('khmelnytsky', 'Хмельницька'), ('kirovohrad', 'Кіровоградська'), ('donetsk', 'Донецька'), ('odesa', 'Одеська'), ('luhansk', 'Луганська'), ('crimea', 'АР Крим'), ('ternopil', 'Тернопільська'), ('kyiv', 'Київська'), ('chernihiv', 'Чернігівська'), ('kherson', 'Херсонська'), ('mykolayiv', 'Миколаївська'), ('volyn', 'Волинська'), ('rivne', 'Рівненська'), ('chernivtsi', 'Чернівецька'), ('zhytomyr', 'Житомирська'), ('ivano-frankivsk', 'Івано-Франківська'), ('sumy', 'Сумська'), ('transcarpathian', 'Закарпатська'), ('dnipropetrovsk', 'Дніпропетровська')], max_length=40, verbose_name='Область'),
        ),
    ]
