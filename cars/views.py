from django.shortcuts import render
from .models import Car, Slide, TestDrive
from django.db.models import Q
from .forms import TestDriveForm


def cars(request):
    car = Car.objects.all()
    slides = Slide.objects.all()
    brand = request.GET.get('brand')
    category = request.GET.get('category')
    search = request.GET.get('search')
    car = car.filter(
        Q(name__icontains=search) | Q(description__icontains=search)) if search else car
    car = car.filter(brand=brand) if brand else car
    car = car.filter(category=category) if category else car

    return render(request, 'cars.html', {'car': car, 'slides': slides})


def detail(request, slug):
    car = Car.objects.get(slug=slug)
    form = TestDriveForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.car = car
        instance.save()
        form = TestDriveForm()
    return render(request, 'detail.html', {'car': car, 'form': form})


def test_drive(request):
    test_drive = TestDrive.objects.filter(last_name=request.user.last_name)
    return render(request, 'test_drive.html', {'test_drive': test_drive})
