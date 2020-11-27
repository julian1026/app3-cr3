from django.shortcuts import render

from django.views.generic import TemplateView, ListView,CreateView,UpdateView
from .models import Estudiante

# Create your views here.

class AgregarEstudiante(CreateView):
    template_name = "formulario.html"
    model=Estudiante
    fields=('__all__')
    success_url= '.'
