# Generated by Django 4.0.4 on 2022-06-26 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0039_alter_order_citi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='citi',
            field=models.CharField(choices=[('rivne', 'Рівненська'), ('lviv', 'Львівська'), ('kyiv', 'Київська'), ('cherkasy', 'Черкаська'), ('zhytomyr', 'Житомирська'), ('ivano-frankivsk', 'Івано-Франківська'), ('volyn', 'Волинська'), ('crimea', 'АР Крим'), ('zaporizhzhia', 'Запорізька'), ('luhansk', 'Луганська'), ('donetsk', 'Донецька'), ('kirovohrad', 'Кіровоградська'), ('sumy', 'Сумська'), ('odesa', 'Одеська'), ('chernihiv', 'Чернігівська'), ('transcarpathian', 'Закарпатська'), ('chernivtsi', 'Чернівецька'), ('khmelnytsky', 'Хмельницька'), ('ternopil', 'Тернопільська'), ('kharkiv', 'Харківська'), ('kherson', 'Херсонська'), ('dnipropetrovsk', 'Дніпропетровська'), ('mykolayiv', 'Миколаївська'), ('poltava', 'Полтавська'), ('vinnytsia', 'Вінницька')], max_length=40, verbose_name='Область'),
        ),
    ]