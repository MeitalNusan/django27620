from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import datetime
from django.template import Template, Context, loader
from .models import *
from AppAfter.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




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

# CREATE 
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

#READ
def leerProfes(request):
    profesores=Profesor.objects.all()
    contexto={'profesores': profesores}
    return render(request, "AppAfter/profesores.html", contexto )

#DELETE
@login_required
def eliminarProfe(request, nombre):
    profesor=Profesor.objects.get(nombre=nombre)
    profesor.delete()

    profesores=Profesor.objects.all()
    contexto={'profesores': profesores}

    return render(request, "AppAfter/profesores.html", contexto)

#UPDATE
def editarProfesor(request, nombre):
    profesor=Profesor.objects.get(nombre=nombre)
    if request.method == 'POST':
        formulario=ProfeFormulario(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            profesor.nombre=informacion['nombre']
            profesor.apellido=informacion['apellido']
            profesor.email=informacion['email']
            profesor.profesion=informacion['profesion']
            profesor.save()
            profesores=Profesor.objects.all()
            contexto={'profesores': profesores}

            return render(request,"AppAfter/profesores.html", contexto)
    else:
        formulario=ProfeFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email, 'profesion':profesor.profesion})
    return render(request,"AppAfter/editarProfesor.html", {'formulario':formulario, 'nombre':nombre})

#-------------------------------------------------------------------------------------------------------------
class EstudiantesList(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name= "AppAfter/estudiante_list.html"

class EstudiantesDetalle(LoginRequiredMixin, DetailView):
    model = Estudiante
    template_name= "AppAfter/estudiante_detail.html"


class EstudiantesCreacion(CreateView):
    model = Estudiante
    success_url=reverse_lazy("estudiante_listar")
    fields=['nombre','apellido', 'email']

class EstudiantesEdicion(UpdateView):
    model = Estudiante
    success_url = reverse_lazy("estudiante_listar")
    fields=['nombre','apellido', 'email']


class EstudiantesEliminacion(DeleteView):
    model = Estudiante
    success_url = reverse_lazy("estudiante_listar")
    fields=['nombre','apellido', 'email']


def login_request(request):
    if request.method == "POST":
        formulario1=AuthenticationForm(request=request, data=request.POST)
        if formulario1.is_valid():
            usuario=formulario1.cleaned_data.get('username')
            clave=formulario1.cleaned_data.get('password')

            user=authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request,"AppAfter/inicio.html", {'usuario': usuario, 'mensaje': "Bienvenido al sistema"})

            else:
                return render(request, "AppAfter/inicio.html", {'mensaje': 'usuario incorrecto, vuelva a logearse'})
        else:
            return render(request, "AppAfter/inicio.html",{'mensaje': 'Error, formulario invalido, vuelva a logearse'})
    else:
        formulario1=AuthenticationForm()
        return render(request,"AppAfter/login.html", {'formulario1': formulario1})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,"AppAfter/inicio.html", {'mensaje': f"usuario {username} creado"})
        else:
            return render(request, "AppAfter/inicio.html",{'mensaje':'formulario incorrecto'})

    else:
        form = UserRegistrationForm()
        return render(request, "AppAfter/register.html", {'form':form})

def editarPerfil(request):
    return render(request, "AppAfter/editarPerfil.html")

@login_required
def editarPerfil(request):
    usuario=request.user
    
    if request.method == "POST":
        formulario=UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()
            return render(request,"AppAfter/inicio.html", {'usuario': usuario, 'mensaje':'Usuario Modificado'})

    else:
        formulario=UserEditForm(instance=usuario)
        return render(request,"AppAfter/editarPerfil.html",{'formulario':formulario, 'usuario':usuario.username})


    