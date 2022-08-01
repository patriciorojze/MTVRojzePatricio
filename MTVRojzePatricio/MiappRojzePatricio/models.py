from django.db import models

# Create your models here.

class Familiar(models.Model):
    Nombre = models.CharField(max_length=35)
    Apellido = models.CharField(max_length=35)
    Edad = models.IntegerField()
    FechaNacimiento = models.DateTimeField() 

class Domicilios(models.Model):
    Direccion = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=45)
    Provincia = models.CharField(max_length=30)
    NroAmbientes = models.IntegerField()