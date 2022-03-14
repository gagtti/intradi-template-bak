
from django.urls import path
from . import views

urlpatterns = [
    path('', views.estructura, name='estructura'),
]
