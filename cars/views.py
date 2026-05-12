from django.shortcuts import render, get_object_or_404
from .models import Car


def home(request):
    cars = Car.objects.all().order_by('-created_at')[:6]  # Últimos 6 carros
    return render(request, 'cars/home.html', {'cars': cars})


# Página de listagem de todos os carros
def car_list(request):
    cars = Car.objects.all().order_by('-created_at')
    return render(request, 'cars/car_list.html', {'cars': cars})


# Página de detalhe de um carro específico
def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})