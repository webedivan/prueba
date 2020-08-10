from django.db import models

# Create your models here.
class Distribuidor(models.Model):
    razonSocial = models.CharField('Razon Social',max_length=60)
    ruc = models.CharField(unique=True,max_length=11)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=35)
    def __str__(self):
        return f'{self.razonSocial}'