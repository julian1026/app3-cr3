from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView,CreateView,UpdateView
from .models import nivelFormacion

# Create your views here.

class AgregarFormacion(CreateView):
    template_name = "addFormacion.html"
    model=nivelFormacion
    fields=('__all__')
    success_url= '.'
