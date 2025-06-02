from django.db import models

# Create your models here.
class Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)
    efecto = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Movimiento(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    poder = models.IntegerField()
    precision = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Pokemon(models.Model):
    nombre = models.CharField(max_length=100)
    tipos = models.ManyToManyField(Tipo)
    descripcion = models.TextField()
    habilidades = models.ManyToManyField(Habilidad)
    movimientos = models.ManyToManyField(Movimiento)
    created_at = models.DateTimeField(auto_now_add=True)
