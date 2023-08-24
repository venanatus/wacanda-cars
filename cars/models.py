from django.db import models
from django.template.defaultfilters import first
from django.contrib.auth.models import User

RATE_CHOICES = [
    ('красный', 'красный'),
    ('зеленый', 'зеленый'),
    ('синий', 'синий'),
    ('белый', 'белый'),
    ('черный', 'черный'),
    ('серая', 'серая'),
]
korobka = [
    ('Автоматическая', 'Автоматическая'),
    ('Механическая', 'Механическая')
]

privod = [
    ('Передняя', 'Передний'),
    ('Задняя', 'задний'),
    ('Полная', 'полный')
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
    color = models.CharField(max_length=255, choices=RATE_CHOICES, null=True, )
    korobka = models.CharField(max_length=255, choices=korobka, null=True)
    privod = models.CharField(max_length=255, choices=privod, null=True)
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
    date = models.DateTimeField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.first_name






class Slide(models.Model):
   image = models.ImageField(default='slide.jpg')
