from pickle import TRUE
from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Area
from planta_docente.models import Personal, Departamento

class EstructuraPageView(TemplateView):

    template_name = "estructura/estructura.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_areas'] = Area.objects.all()
        context['cantidad_areas'] = Area.objects.count()
        context['director_decano'] = Departamento.objects.all()
        return context