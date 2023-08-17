from django.shortcuts import render
from .models import Car, Slide
from django.db.models import Q
from .forms import TestDriveForm


def cars(request):
    car = Car.objects.all()
    slides = Slide.objects.all()
    brand = request.GET.get('brand')
    search = request.GET.get('search')
    car = car.filter(
        Q(name__icontains=search) | Q(description__icontains=search)) if search else car
    car = car.filter(brand=brand) if brand else car

    return render(request, 'cars.html', {'car': car, 'slides': slides})


def detail(request, slug):
    detail_car = Car.objects.filter(slug=slug)
    form = TestDriveForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = TestDriveForm()
    return render(request, 'detail.html', {'detail_car': detail_car, 'form': form})


