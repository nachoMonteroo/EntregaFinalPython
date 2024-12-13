from django.urls import path
from aplicacion import views    

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("profesores/", views.profesores, name="profesores"),
    path("estudiantes/",views.estudiantes, name="estudiantes"),
    path("infoalumno/<nombre_alumno>/",views.infoalumnos, name="infoalumnos"),
    path("infoprofesor/<nombre_profesor>/",views.infoprofesores,name="infoprofesores"),
    path("agregarestudiante/",views.agregaralumnos, name="agregaralumnos"),
    path("eliminaralumno/<nombre_alumno>/",views.eliminaralumnos, name="eliminaralumnos"),
    path("editaralumno/<nombre_alumno>/",views.editaralumnos, name="editaralumnos"),
    path("agregarprofesores/",views.agregarprofesores,name="agregarprofesores"),
    path("eliminarprofesores/<nombre_profesor>/",views.eliminarprofesores, name="eliminarprofesores"),
    path("editarprofesores/<nombre_profesor>/", views.editarprofesores, name="editarprofesores"),
]
