from django.shortcuts import render
from django.http import HttpResponse

def vista(req):
    return render(req, "aplicacion/index.html")