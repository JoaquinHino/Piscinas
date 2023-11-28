from django.db import models
from uuid import uuid4

# Create your models here.

class Usuario(models.Model):
    idusuario = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Mensaje(models.Model):
    idmensaje = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    mensaje = models.CharField(max_length=200)



    