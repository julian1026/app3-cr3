
from django.db import models
from estudiantes.models import Estudiante

# Create your models here.
class nivelFormacion (models.Model):
    cod_formacion = models.IntegerField()
    nombre_formacion = models.CharField(max_length= 100)
    codigo_estudiante= models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cod_formacion)