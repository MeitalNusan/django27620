from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import datetime
from django.template import Template, Context, loader
from .models import *

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

