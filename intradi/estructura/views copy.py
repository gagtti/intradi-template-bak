from django.shortcuts import render
from .models import Area

# Create your views here.
def estructura(request):
    lista_areas = Area.objects.all()
    cantidad_areas = Area.objects.count()
    return render(request, "estructura/estructura.html", {'cantidad_areas':cantidad_areas, 'lista_areas':lista_areas})