from django.db import models

# Create your models here.
class Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)
    efecto = models.TextField()

class Movimiento(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    poder = models.IntegerField()
    precision = models.IntegerField()

class Pokemon(models.Model):
    nombre = models.CharField(max_length=100)
    tipos = models.ManyToManyField(Tipo)
    habilidades = models.ManyToManyField(Habilidad)
    movimientos = models.ManyToManyField(Movimiento)
    evolucion = models.OneToOneField('self', null=True, blank=True, on_delete=models.SET_NULL)
