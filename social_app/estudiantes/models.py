
from django.db import models

# Create your models here.
class Estudiante(models.Model):
    codigo_estudiante=models.IntegerField()
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=100)
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
    fecha_nacimiento=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    def __str__(self):
        return str(self.codigo_estudiante)
