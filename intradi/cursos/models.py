from django.db import models


# Create your models here.
class TipoCurso(models.Model):
    tipo_curso = models.CharField(max_length=100, verbose_name="Nombre Tipo Curso")
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "Tipo Curso"
        verbose_name_plural = "Tipo Curso"
        ordering = ['-tipo_curso']

    def __str__(self):
        return self.tipo_curso


class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100, verbose_name="Nombre Curso")
    descripcion = models.TextField(verbose_name="Descripción", blank=True)
    fecha_inicio = models.DateField(auto_now=False, verbose_name = "Fecha de Inicio", help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    fecha_finalizacion = models.DateField(auto_now=False, verbose_name = "Fecha de Finalización")
    año = models.IntegerField()
    cuatrimestre = models.IntegerField()
    cantidad_horas_catedra = models.IntegerField(default=0)
    arancelado = models.BooleanField(default=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio", default= 0.00)
    
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateField(auto_now=True, verbose_name="Fecha de Modificación")
    tipo_curso = models.ForeignKey(TipoCurso, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre_curso