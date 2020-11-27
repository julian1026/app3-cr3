from django.db import models
from nivelFormacion.models import nivelFormacion

# Create your models here.
class Programas (models.Model):
    cod_programa = models.IntegerField()
    nombre_programa = models.CharField(max_length= 100)
    cod_formacion= models.ForeignKey(nivelFormacion, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cod_programa)