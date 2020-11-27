from django.contrib import admin
from django.urls import path

from.import views
urlpatterns = [
    path('AgregarEstudiante', views.AgregarEstudiante.as_view()),
]
    # path('mostrarClientes/', views.MostrarClientes.as_view()),
    # path('addClientes/', views.PruebaCreateView.as_view()),