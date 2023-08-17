from django.db import models
from django.template.defaultfilters import first

RATE_CHOICES = [
    (1, 'красный'),
    (2, 'зеленый'),
    (3, 'синий'),
    (4, 'белый'),
    (5, 'черный'),
    (6, 'серая'),
]
korobka = [
    (1, '1 - Автоматическая'),
    (2, '2 - Механическая')
]

privod = [
    (1, '1 - Передний'),
    (2, '2 - задний'),
    (3, '3 - полный')
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
    car = models.ForeignKey(Car, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name






class Slide(models.Model):
   image = models.ImageField(default='slide.jpg')
