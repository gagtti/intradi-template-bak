
from django.urls import path
from . import views

urlpatterns = [
    path('', views.planta_docente, name='planta_docente'),
]
