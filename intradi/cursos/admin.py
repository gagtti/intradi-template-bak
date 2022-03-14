from django.contrib import admin
from .models import TipoCurso, Curso

# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

admin.site.register(TipoCurso)
admin.site.register(Curso, CursoAdmin)