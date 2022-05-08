from django.db import models
from datetime import datetime 

class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    fecha=models.DateField("%y,%d,%m")

    def __str__(self):
        return self.nombre+ " " + str(self.edad) + str(self.fecha)
