from django.contrib import admin
from django.urls import path

from.import views
urlpatterns = [
    path('addNivelFormacion', views.AgregarFormacion.as_view()),
]
