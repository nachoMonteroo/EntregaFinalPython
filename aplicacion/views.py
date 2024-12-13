from django.shortcuts import render,redirect
from django.http import HttpResponse
from aplicacion.forms import estudiantesFormulario,profesoresFormulario
from aplicacion.models import *
from django.contrib.auth.decorators import login_required



#------------------------------------------------------INICIO--------------------------------------------------------
def inicio(req):
    return render(req, "aplicacion/index.html")


#------------------------------------------------------ESTUDIANTES---------------------------------------------------

def estudiantes(req):
    estudiantes = Estudiantes.objects.all()
    directivos = Directivo.objects.all()
    contexto = {"estudiantes":estudiantes,"directivos":directivos}

    return render(req, "aplicacion/estudiantes.html",contexto)

def infoalumnos(req,nombre_alumno):
    alumno=Estudiantes.objects.get(nombre=nombre_alumno)
    return render(req, "aplicacion/infoalumnos.html",{
        "nombre":alumno.nombre,
        "apellido":alumno.apellido,
        "ano":alumno.ano,
        "division":alumno.division,
        "inasistencias":alumno.inasistencias,
        "fecha_de_nacimiento":alumno.fecha_de_nacimiento,
        "email":alumno.email,
})

def agregaralumnos(req):
    
    if req.method == "POST":
        miFormulario = estudiantesFormulario(req.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            estudiante = Estudiantes(nombre=info["nombre"],
                                    apellido=info["apellido"],
                                    ano=info["ano"],
                                    division=info["division"],
                                    inasistencias=info["inasistencias"],
                                    fecha_de_nacimiento=info["fecha_de_nacimiento"],
                                    email=info["email"])
            estudiante.save()
        
            return redirect("estudiantes")
    else:
        miFormulario = estudiantesFormulario()

    return render(req, "aplicacion/agregaralumnos.html",{"miFormulario":miFormulario})
    
def eliminaralumnos(req,nombre_alumno):
    alumno= Estudiantes.objects.get(nombre=nombre_alumno)
    alumno.delete()
    return redirect("estudiantes")

def editaralumnos(req, nombre_alumno):
    alumno = Estudiantes.objects.get(nombre=nombre_alumno)
    if req.method=="POST":
        miFormulario = estudiantesFormulario(req.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            alumno.nombre = info["nombre"]
            alumno.apellido = info["apellido"]
            alumno.ano = info["ano"]
            alumno.division = info["division"]
            alumno.inasistencias = info["inasistencias"]
            alumno.fecha_de_nacimiento = info["fecha_de_nacimiento"]
            alumno.email = info["email"]
            alumno.save()
        
            return redirect("estudiantes")
    else:
        miFormulario = estudiantesFormulario(initial={"nombre":alumno.nombre,"apellido":alumno.apellido,"ano":alumno.ano,"division":alumno.division,"inasistencias":alumno.inasistencias,"fecha_de_nacimiento":alumno.fecha_de_nacimiento,"email":alumno.email})

    return render(req, "aplicacion/editaralumnos.html",{"miFormulario":miFormulario, "nombre_alumno":nombre_alumno})


#------------------------------------------------------PROFESORES----------------------------------------------------

def profesores(req):
    profesores = Profesores.objects.all()
    contexto = {"profesores":profesores}

    return render(req, "aplicacion/profesores.html",contexto)

def infoprofesores(req,nombre_profesor):
    profesor=Profesores.objects.get(nombre=nombre_profesor)
    return render(req, "aplicacion/infoprofesores.html",{
        "nombre":profesor.nombre,
        "apellido":profesor.apellido,
        "inasistencias":profesor.inasistencias,
        "fecha_de_nacimiento":profesor.fecha_de_nacimiento,
        "email":profesor.email,
})

def agregarprofesores(req):
    if req.method == "POST":
        miFormulario = profesoresFormulario(req.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            profesor = Profesores(nombre=info["nombre"],
                                    apellido=info["apellido"],
                                    inasistencias=info["inasistencias"],
                                    fecha_de_nacimiento=info["fecha_de_nacimiento"],
                                    email=info["email"])
            profesor.save()
        
            return redirect("profesores")
    else:
        miFormulario = profesoresFormulario()

    return render(req, "aplicacion/agregarprofesores.html",{"miFormulario":miFormulario})
    

def eliminarprofesores(req,nombre_profesor):
    profesor= Profesores.objects.get(nombre=nombre_profesor)
    profesor.delete()
    return redirect("profesores")

def editarprofesores(req,nombre_profesor):
    profesor = Profesores.objects.get(nombre=nombre_profesor)
    if req.method=="POST":
        miFormulario = profesoresFormulario(req.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            profesor.nombre = info["nombre"]
            profesor.apellido = info["apellido"]
            profesor.email = info["email"]
            profesor.save()
        
            return redirect("profesores")
    else:
        miFormulario = profesoresFormulario(initial={"nombre":profesor.nombre,"apellido":profesor.apellido,"inasistencias":profesor.inasistencias,"fecha_de_nacimiento":profesor.fecha_de_nacimiento,"email":profesor.email})

    return render(req, "aplicacion/editarprofesores.html",{"miFormulario":miFormulario, "nombre_profesor":nombre_profesor})


