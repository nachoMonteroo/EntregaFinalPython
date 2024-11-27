from django.urls import path
from aplicacion import views    

urlpatterns = [
    path("", views.inicio),
    path("profesores/", views.profesores),
    path("estudiantes/",views.estudiantes),
]
