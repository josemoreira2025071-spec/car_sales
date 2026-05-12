from django.shortcuts import render, get_object_or_404
from .models import Car


def home(request):
    """Página inicial com carros em destaque"""
    cars = Car.objects.all().order_by('-created_at')[:6]
    return render(request, 'cars/home.html', {'cars': cars})


def car_list(request):
    """Lista de todos os carros à venda"""
    cars = Car.objects.all().order_by('-created_at')
    return render(request, 'cars/car_list.html', {'cars': cars})


def car_detail(request, pk):
    """Detalhe de um carro específico"""
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})


def about(request):
    """Página Sobre Nós"""
    return render(request, 'cars/about.html')


def contact(request):
    """Página de Contactos"""
    return render(request, 'cars/contact.html')