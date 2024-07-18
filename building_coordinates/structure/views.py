from django.shortcuts import render, redirect, HttpResponse
from .models import Structure, Entrance
from .forms import StructureForm
from rest_framework import generics, response
from rest_framework.views import APIView
from .serializers import StructureSerializer
import requests


class StructureAllViewAPI(generics.ListAPIView):
    """API представление для всех адрессов."""
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer


class StructureAdressViewAPI(APIView):
    """API представление для одного адресса."""

    def get(self, request, address):
        adress_data = Structure.objects.filter(address=address).values()
        return response.Response({'adress': list(adress_data)})


def index(request) -> HttpResponse:
    """Главная страница."""
    template_name = 'structure/index.html'
    context = {
        'structures': Structure.objects.all(),
    }
    return render(request, template_name, context)


def info(request) -> HttpResponse:
    """Страница с информацией о сайте."""
    template_name = 'structure/info.html'
    return render(request, template_name)


def get_coordinates(address: str) -> tuple:
    """Получает широту и долготу для данного адреса, использую API Nominatim."""
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': address,
        'format': 'json'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data and len(data) > 0:
            return float(data[0]['lat']), float(data[0]['lon'])
    return None, None


def structure_create(request) -> HttpResponse:
    """Проверка данных на валидность и добавление данных в БД."""
    if request.method == 'POST':
        form = StructureForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            latitude, longitude = get_coordinates(address)
            if latitude is not None and longitude is not None:
                structure = Structure.objects.create(
                    address=address,
                    latitude=latitude,
                    longitude=longitude
                )
                Entrance.objects.create(
                    structure=structure,
                    latitude=latitude,
                    longitude=longitude
                )
                return redirect('structure:index')
    else:
        form = StructureForm()
    return render(request, 'structure/create.html', {'form': form})
