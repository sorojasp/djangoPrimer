from django.db import models

# Create your models here.
class UsuarioModel(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)