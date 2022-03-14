# Generated by Django 4.0.3 on 2022-03-08 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planta_docente', '0006_personal_es_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre Departamento')),
                ('domicilio', models.CharField(blank=True, max_length=100, null=True, verbose_name='Domicilio')),
                ('telefono', models.PositiveIntegerField(blank=True, null=True, verbose_name='Teléfono')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('director_decano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planta_docente.personal')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'ordering': ['-fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre Área')),
                ('nombre_abreviado', models.CharField(blank=True, max_length=20, verbose_name='Nombre Abreviado')),
                ('telefono_ext', models.PositiveIntegerField(default=3201)),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planta_docente.departamento')),
            ],
            options={
                'verbose_name': 'Área',
                'verbose_name_plural': 'Áreas',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
