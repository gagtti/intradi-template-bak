from django.db import models


# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre Departamento")
    domicilio = models.CharField(max_length=100, verbose_name="Domicilio", blank=True, null=True)
    telefono = models.PositiveIntegerField(verbose_name="Teléfono", blank=True, null=True)
    email = models.EmailField(max_length=100, verbose_name="Email", blank=True, null=True)
    
    
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateField(auto_now=True, verbose_name="Fecha de Modificación")
    

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre


class Area(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=100, verbose_name="Nombre Área")
    nombre_abreviado = models.CharField(max_length=20, verbose_name="Nombre Abreviado", blank=True)
    telefono_ext = models.PositiveIntegerField(default=3201)
    """ departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE) """
    
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateField(auto_now=True, verbose_name="Fecha de Modificación")
    

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre





