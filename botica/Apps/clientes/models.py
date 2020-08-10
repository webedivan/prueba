from django.db import models

# Create your models here.
class cliente(models.Model):
    nombre = models.CharField(max_length=35)
    apellidos = models.CharField(max_length=50)
    dni = models.CharField('DNI',max_length=8)
    SEXOS = (('M', 'Masculino'), ('F', 'Femenino'))
    sexo = models.CharField(max_length=1, choices=SEXOS, default='M')
    celular = models.CharField(max_length=9)
    def __str__(self):
        return f'{self.nombre},{self.apellidos.upper()}'

