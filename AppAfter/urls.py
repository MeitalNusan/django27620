from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name= "inicio"),
    #path('estudiantes/', estudiantes, name= "estudiantes"),
    path('cursos/', cursos, name= "cursos"),
    path('entregables/', entregables, name= "entregables"),
    #path('cursosFormulario/', cursosFormulario, name= "cursosFormulario"),
    path('busquedaComision/', busquedaComision, name= "busquedaComision"),
    path('buscar/', buscar, name= "buscar"),
    path('profesores/', leerProfes, name= "profesores"),
    path('eliminarProfesor/<nombre>', eliminarProfe, name= "eliminarProfesor"),
    path('editarProfesor/<nombre>', editarProfesor, name= "editarProfesor"),

    path('estudiante/list', EstudiantesList.as_view(), name= "estudiante_listar"),
    path('estudiante/<pk>', EstudiantesDetalle.as_view(), name= "estudiante_detail"),
    path('estudiante/nuevo/', EstudiantesCreacion.as_view(), name= "estudiante_crear"),
    path('estudiante/editar/<pk>', EstudiantesEdicion.as_view(), name= "estudiante_editar"),
    path('estudiante/borrar/<pk>', EstudiantesEliminacion.as_view(), name= "estudiante_borrar"),
    
    path('login/', login_request, name= "login"),
    path('register/', register, name= "register"),
    path('logout/', LogoutView.as_view(template_name="AppAfter/logout.html"), name= "logout"),
    path('editarPerfil/', editarPerfil, name= "editarPerfil"),
    

    
]
