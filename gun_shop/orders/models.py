from django.db import models


class Order(models.Model):
    Crimea = "crimea"
    Vinnytsia = "vinnytsia"
    Volyn = "volyn"
    Dnipropetrovsk = "dnipropetrovsk"
    Donetsk = "donetsk"
    Zhytomyr = "zhytomyr"
    Transcarpathian = "transcarpathian"
    Zaporizhzhia = "zaporizhzhia"
    IvanoFrankivsk = "ivano-frankivsk"
    Kyiv = "kyiv"
    Kirovohrad = "kirovohrad"
    Luhansk = "luhansk"
    Lviv = "lviv"
    Mykolayiv = "mykolayiv"
    Odesa = "odesa"
    Poltava = "poltava"
    Rivne = "rivne"
    Sumy = "sumy"
    Ternopil = "ternopil"
    Kharkiv = "kharkiv"
    Kherson = "kherson"
    Khmelnytsky = "khmelnytsky"
    Cherkasy = "cherkasy"
    Chernivtsi = "chernivtsi"
    Chernihiv = "chernihiv"

    CHOICE_CITI = {
        (Crimea, "АР Крим"),
        (Vinnytsia, "Вінницька"),
        (Volyn, "Волинська"),
        (Dnipropetrovsk, "Дніпропетровська"),
        (Donetsk, "Донецька"),
        (Zhytomyr, "Житомирська"),
        (Transcarpathian, "Закарпатська"),
        (Zaporizhzhia, "Запорізька"),
        (IvanoFrankivsk, "Івано-Франківська"),
        (Kyiv, "Київська"),
        (Kirovohrad, "Кіровоградська"),
        (Luhansk, "Луганська"),
        (Lviv, "Львівська"),
        (Mykolayiv, "Миколаївська"),
        (Odesa, "Одеська"),
        (Poltava, "Полтавська"),
        (Rivne, "Рівненська"),
        (Sumy, "Сумська"),
        (Ternopil, "Тернопільська"),
        (Kharkiv, "Харківська"),
        (Kherson, "Херсонська"),
        (Khmelnytsky, "Хмельницька"),
        (Cherkasy, "Черкаська"),
        (Chernivtsi, "Чернівецька"),
        (Chernihiv, "Чернігівська")
    }

    fname = models.CharField("Ім'я", max_length=40)
    sname = models.CharField("Прізвище", max_length=40)
    mail = models.EmailField("E-mail")
    citi = models.CharField("Вкажіть область", max_length=40, choices=CHOICE_CITI)
    address = models.CharField("Адрес", max_length=255)

    def __str__(self):
        return self.fname + " " + self.sname

    class Meta:
        verbose_name = "Ордер"
        verbose_name_plural = "Ордера"
