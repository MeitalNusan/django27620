from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import datetime
from django.template import Template, Context, loader
from .models import *
from AppAfter.forms import CursoFormulario

def persona(request):
    dia=datetime.now().year
    edad=50
    edad2=30
    edad3=80
    persona1=Persona(nombre="Mariana", edad= edad, fecha=int(dia)-int(edad))
    persona2=Persona(nombre="Leonel", edad=edad2,fecha=int(dia)-int(edad2))
    persona3=Persona(nombre="Pedro", edad=edad3,fecha=int(dia)-int(edad3))
    diccionario={"persona": persona1, "persona2": persona2, "persona3": persona3}

    plantilla=loader.get_template("index.html")
  
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def inicio(request):
    return render(request, 'AppAfter/inicio.html')

def profesores(request):
    return render(request, "AppAfter/profesores.html")

def estudiantes(request):
    return render(request, "AppAfter/estudiantes.html")


def entregables(request):
     return render(request, "AppAfter/entregables.html")

def cursos(request):
    if request.method =='POST':

        miFormulario=CursoFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            curso=Curso(nombre=informacion['nombre'], comision=informacion['comision'])
            curso.save()
            return render(request,'AppAfter/inicio.html')

    else:
        miFormulario=CursoFormulario()
    return render(request, "AppAfter/cursos.html" , {'formulario':miFormulario})

def busquedaComision(request):
    return render(request,'AppAfter/busquedaComision.html')

def buscar(request):
    if request.GET['comision']:
        comision=request.GET['comision']
        cursos=Curso.objects.filter(comision=comision)
        return render(request, "AppAfter/resultadosBusqueda.html", {'cursos': cursos, 'comision': comision})
    else:
        respuesta="No se ingreso ninguna comision"
        return render(request, "AppAfter/resultadosBusqueda.html", {'respuesta':respuesta})

def leerCursos(request):
    cursos=Curso.objects.all()
    return(request, "AppAfter/cursos.html", {'cursos': cursos} )




    