from django.db import models
from datetime import datetime 

class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    fecha=models.DateField("%y,%d,%m")

    def __str__(self):
        return self.nombre+ " " + str(self.edad) + str(self.fecha)

class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()

class Estudiante(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    profesion=models.CharField(max_length=50)

class Entreglable(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_entrega=models.DateField()
    entregado=models.BooleanField()

