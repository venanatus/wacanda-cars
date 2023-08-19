from django.db import models
from django.template.defaultfilters import first

RATE_CHOICES = [
    ('красный', 'красный'),
    ('зеленый', 'зеленый'),
    ('синий', 'синий'),
    ('белый', 'белый'),
    ('черный', 'черный'),
    ('серая', 'серая'),
]
korobka = [
    ('Автоматическая', '1 - Автоматическая'),
    ('Механическая', '2 - Механическая')
]

privod = [
    ('Передняя', '1 - Передний'),
    ('Задняя', '2 - задний'),
    ('Полная', '3 - полный')
]


class Car(models.Model):
    name = models.CharField('полное название машины', max_length=50)
    description = models.TextField('описание')
    price = models.IntegerField('цена')
    date = models.DateField('дата произдводства')
    image1 = models.ImageField(default='default.png')
    image2 = models.ImageField(default='default.png')
    image3 = models.ImageField(default='default.png')
    brand = models.ForeignKey('cars.Brand', on_delete=models.CASCADE)
    probeg = models.IntegerField('пробег')
    obyomdvigatela = models.IntegerField('обьем двигателя')
    color = models.PositiveSmallIntegerField('цвет', choices=RATE_CHOICES, null=True, )
    korobka = models.PositiveSmallIntegerField('коробка передач', choices=korobka, null=True)
    privod = models.PositiveSmallIntegerField('привод', choices=privod, null=True)
    category = models.ForeignKey('cars.Category', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cars_brands'


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'car_categories'


class TestDrive(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name






class Slide(models.Model):
   image = models.ImageField(default='slide.jpg')
