from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()


