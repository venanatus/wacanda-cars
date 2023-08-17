from django.contrib import admin
from .models import Car, Brand, Category, Slide,TestDrive

admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Slide)
admin.site.register(TestDrive)

# Register your models here.
