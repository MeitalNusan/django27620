from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User

class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    fecha=models.DateField("%y,%d,%m")


class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()

    def __str__(self):
     return self.nombre + " " + str(self.comision)

class Estudiante(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
     return self.nombre + " " + self.apellido

class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    profesion=models.CharField(max_length=50)

    def __str__(self):
     return self.nombre + " " + str(self.apellido)

class Entreglable(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_entrega=models.DateField()
    entregado=models.BooleanField()


class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    avatar= models.ImageField(upload_to='avatar', blank=True, null=True)