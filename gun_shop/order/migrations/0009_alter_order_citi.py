# Generated by Django 4.0.4 on 2022-06-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_order_citi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='citi',
            field=models.CharField(choices=[('zaporizhzhia', 'Запорізька'), ('ivano-frankivsk', 'Івано-Франківська'), ('mykolayiv', 'Миколаївська'), ('kyiv', 'Київська'), ('sumy', 'Сумська'), ('khmelnytsky', 'Хмельницька'), ('volyn', 'Волинська'), ('lviv', 'Львівська'), ('cherkasy', 'Черкаська'), ('rivne', 'Рівненська'), ('kharkiv', 'Харківська'), ('poltava', 'Полтавська'), ('transcarpathian', 'Закарпатська'), ('dnipropetrovsk', 'Дніпропетровська'), ('luhansk', 'Луганська'), ('ternopil', 'Тернопільська'), ('chernihiv', 'Чернігівська'), ('crimea', 'АР Крим'), ('donetsk', 'Донецька'), ('vinnytsia', 'Вінницька'), ('zhytomyr', 'Житомирська'), ('kirovohrad', 'Кіровоградська'), ('chernivtsi', 'Чернівецька'), ('kherson', 'Херсонська'), ('odesa', 'Одеська')], max_length=40, verbose_name='Область'),
        ),
    ]
