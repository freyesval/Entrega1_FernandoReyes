from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    
    def __str__(self) -> str:
        return f"{self.nombre}"
    
class Paquete(models.Model):
    nombre = models.CharField(max_length=50)
    peso = models.IntegerField()
    remitente = models.CharField(max_length=50)
    destinatario = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.nombre}"
    
class Celular(models.Model):
    nombre = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField()
    def __str__(self) -> str:
        return f"{self.nombre}"
