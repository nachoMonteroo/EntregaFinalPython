from django.shortcuts import render
from django.http import HttpResponse

def inicio(req):
    return render(req, "aplicacion/index.html")


def estudiantes(req):
    return render(req, "aplicacion/estudiantes.html")


def profesores(req):
    return render(req, "aplicacion/profesores.html")