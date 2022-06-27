# Generated by Django 4.0.4 on 2022-06-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_alter_order_citi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='citi',
            field=models.CharField(choices=[('cherkasy', 'Черкаська'), ('transcarpathian', 'Закарпатська'), ('odesa', 'Одеська'), ('khmelnytsky', 'Хмельницька'), ('poltava', 'Полтавська'), ('lviv', 'Львівська'), ('zhytomyr', 'Житомирська'), ('dnipropetrovsk', 'Дніпропетровська'), ('chernihiv', 'Чернігівська'), ('kharkiv', 'Харківська'), ('luhansk', 'Луганська'), ('sumy', 'Сумська'), ('kirovohrad', 'Кіровоградська'), ('crimea', 'АР Крим'), ('mykolayiv', 'Миколаївська'), ('kherson', 'Херсонська'), ('ternopil', 'Тернопільська'), ('chernivtsi', 'Чернівецька'), ('ivano-frankivsk', 'Івано-Франківська'), ('volyn', 'Волинська'), ('rivne', 'Рівненська'), ('kyiv', 'Київська'), ('vinnytsia', 'Вінницька'), ('zaporizhzhia', 'Запорізька'), ('donetsk', 'Донецька')], max_length=40, verbose_name='Область'),
        ),
    ]