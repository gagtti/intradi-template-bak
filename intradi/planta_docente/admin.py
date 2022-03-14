from django.contrib import admin
from .models import Claustro, Personal, PersonalDocente, Departamento, Area
from estructura.models import Area
# Register your models here.


class PersonalDocenteAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    list_display = ('apellido', 'nombre', 'domicilio', 'ciudad')
    list_filter = ('apellido', 'domicilio')
    ordering = ['apellido']
    search_fields = ['apellido', 'nombre']

class PersonalAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    list_display = ('apellido', 'nombre', 'claustro', 'domicilio', 'ciudad')
    list_filter = ('claustro', 'domicilio')
    ordering = ['apellido']
    search_fields = ['apellido', 'nombre']


admin.site.register(PersonalDocente, PersonalDocenteAdmin)
admin.site.register(Claustro)
admin.site.register(Departamento)
admin.site.register(Area)
admin.site.register(Personal, PersonalAdmin)