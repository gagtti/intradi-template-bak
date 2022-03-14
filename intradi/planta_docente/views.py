from django.shortcuts import render
from .models import PersonalDocente

# Create your views here.
def planta_docente(request):
    docentes = PersonalDocente.objects.all()
    cantidad = PersonalDocente.objects.count()
    full_path = request.get_full_path()
    currentUrl_prev = full_path[full_path.index('/', 1):]
    currentUrl = currentUrl_prev[2:]
    """ currentUrl = currentUrl_ant.rstrip(currentUrl_ant[-1]) """
    return render(request, "planta_docente/planta_docente.html", {'docentes':docentes, 'cantidad':cantidad, 'currentUrl':currentUrl})

def concursos(request):
    """ docentes = PersonalDocente.objects.all()
    cantidad = PersonalDocente.objects.count()
    return render(request, "planta_docente/planta_docente.html", {'docentes':docentes, 'cantidad':cantidad}) """
    full_path = request.get_full_path()
    currentUrl_prev = full_path[full_path.index('/', 1):]
    currentUrl_ant = currentUrl_prev[2:]
    currentUrl = currentUrl_ant.rstrip(currentUrl_ant[-1])
    return render(request, "planta_docente/concursos.html", {'currentUrl':currentUrl})
