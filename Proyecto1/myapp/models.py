from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.profesion}"  
    
class Curso(models.Model):    
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField()
    def __str__(self):
        return self.nombre
    
class Entregable(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='entregables', null=True, blank=True)
    nombre = models.CharField(max_length=100) 
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()   

    def __str__(self):
        return f"{self.nombre} ({self.curso.nombre if self.curso else 'Sin curso'})"

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares/', null=True, blank=True)

    def __str__(self):
        return f"Avatar de {self.user.username}"    