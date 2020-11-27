from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView,CreateView,UpdateView
from .models import Programas

# Create your views here.

class AgregarProgramas(CreateView):
    template_name = "addPrograma.html"
    model=Programas
    fields=('__all__')
    success_url= '.'
