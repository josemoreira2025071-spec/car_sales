from django.shortcuts import render
from .models import Car

def car_list(request):
    cars = Car.objects.all().order_by('-created_at')
    return render(request, 'cars/car_list.html', {'cars': cars})