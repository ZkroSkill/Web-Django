from django.db import models

# Create your models here.
class producto(models.Model):
    codigo      = models.DecimalField(max_digits=13, decimal_places=0)
    descripcion = models.TextField()
    stock       = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return self.descripcion

class usuario(models.Model):
    #area administrador
    rut         = models.CharField(max_length=9)
    email       = models.EmailField()
    contrseña   = models.CharField(max_length=50)
    nombreC     = models.CharField(max_length=50)
    fechaNac    = models.DateField
    telefono    = models.IntegerField()
    
    def __str__(self):
        return self.nombreC

class categoria(models.Model):
    tipo = models.CharField(max_length=50)
    id = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo




    
