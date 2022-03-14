from django.shortcuts import render
from .models import Curso

# Create your views here.
def cursos(request):
    cursos = Curso.objects.all()
    cantidad = Curso.objects.count()
    return render(request, "cursos/cursos.html", {'cursos':cursos, 'cantidad':cantidad})