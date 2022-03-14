# Generated by Django 4.0.3 on 2022-03-03 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estructura', '0004_alter_departamento_domicilio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='domicilio',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Domicilio'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='telefono',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Teléfono'),
        ),
    ]
