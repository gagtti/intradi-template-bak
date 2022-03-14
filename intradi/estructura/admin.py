from django.contrib import admin
""" from .models import Area, Departamento

class AreaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    list_display = ('numero', 'nombre', 'telefono_ext', 'departamento')
    ordering = ['numero']

admin.site.register(Area, AreaAdmin)


class DepartamentoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    ordering = ['nombre']
    search_fields = ['nombre']


admin.site.register(Departamento, DepartamentoAdmin) """