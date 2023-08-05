from django.db import models

# Create your models here.
class Tarea(models.Model):
  titulo = models.CharField(max_length = 64, blank = False, null = False, default = "---")
  # Estado 0, tarea pendiente
  # Estado 1, tarea completada
  estado = models.BooleanField(default = 0)