from pickle import FALSE
from tkinter import CASCADE
from django.db import models


# Create your models here.


class Claustro(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre Claustro")

    class Meta:
        verbose_name = "Claustro"
        verbose_name_plural = "Claustros"
        ordering = ['nombre']

    def __str__(self):
        return (self.nombre)



class Personal(models.Model):
    DOCUMENTO = 'DNI'
    LIBRETA_CIVICA = 'LC'
    PASAPORTE = 'PAS'

    TIPO_DOCUMENTO = [
        (DOCUMENTO, 'DNI'),
        (LIBRETA_CIVICA, 'Libreta Cívica'),
        (PASAPORTE, 'Pasaporte'),
    ]

    legajo = models.PositiveIntegerField()
    nombre = models.CharField(max_length=100, verbose_name="Nombres")
    apellido = models.CharField(max_length=100, verbose_name="Apellidos")
    cortesia = models.CharField(max_length=10, verbose_name="Título de Cortesía", default="Sr/Sra")
    domicilio = models.CharField(max_length=100, verbose_name="Domicilio")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    lugar_nacimiento = models.CharField(max_length=100, verbose_name="Lugar de Nacimiento")
    fecha_nacimiento = models.DateField(auto_now_add=False, verbose_name="Fecha de Nacimiento")
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    claustro = models.ForeignKey(Claustro, on_delete=models.CASCADE)

    tipo_documento = models.CharField(
        max_length=3,
        choices=TIPO_DOCUMENTO,
        default=DOCUMENTO,
    )

    numero_documento = models.PositiveIntegerField()
    
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateField(auto_now=True, verbose_name="Fecha de Modificación")


    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personal"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return '%s %s' % (self.apellido, self.nombre)


class PersonalDocente(models.Model):
    DOCUMENTO = 'DNI'
    LIBRETA_CIVICA = 'LC'
    PASAPORTE = 'PAS'

    TIPO_DOCUMENTO = [
        (DOCUMENTO, 'DNI'),
        (LIBRETA_CIVICA, 'Libreta Cívica'),
        (PASAPORTE, 'Pasaporte'),
    ]

    legajo = models.PositiveIntegerField()
    nombre = models.CharField(max_length=100, verbose_name="Nombres")
    apellido = models.CharField(max_length=100, verbose_name="Apellidos")
    domicilio = models.CharField(max_length=100, verbose_name="Domicilio")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    lugar_nacimiento = models.CharField(max_length=100, verbose_name="Lugar de Nacimiento")
    fecha_nacimiento = models.DateField(auto_now_add=False, verbose_name="Fecha de Nacimiento")
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")

    tipo_documento = models.CharField(
        max_length=3,
        choices=TIPO_DOCUMENTO,
        default=DOCUMENTO,
    )

    numero_documento = models.PositiveIntegerField()
    
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateField(auto_now=True, verbose_name="Fecha de Modificación")

    """ area = models.ForeignKey(Area, on_delete=models.CASCADE) """
    

    class Meta:
        verbose_name = "Personal Docente"
        verbose_name_plural = "Personal Docente"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return '%s %s' % (self.apellido, self.nombre)



""" class DirectorDecano(models.Model):
    
    director_decano = models.ForeignKey(Personal, on_delete=models.CASCADE) 
    fecha_alta_cargo = models.DateField(auto_now=False, verbose_name="Fecha que asume el cargo")
    fecha_baja_cargo = models.DateField(auto_now=False, verbose_name="Fecha que deja el cargo", blank=True, null=True)
    
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateField(auto_now=True, verbose_name="Fecha de Modificación")

    es_activo = models.BooleanField()
    

    class Meta:
        verbose_name = "Director Decano"
        verbose_name_plural = "Directores Decanos"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.director_decano.apellido """



class Departamento(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre Departamento")
    domicilio = models.CharField(max_length=100, verbose_name="Domicilio", blank=True, null=True)
    telefono = models.PositiveIntegerField(verbose_name="Teléfono", blank=True, null=True)
    email = models.EmailField(max_length=100, verbose_name="Email", blank=True, null=True)
    director_decano = models.ForeignKey(Personal, on_delete=models.CASCADE)
    
    
    
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
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateField(auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre
