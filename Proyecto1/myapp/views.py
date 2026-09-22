from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable

def index(request):
    context = { "mensaje": "¡Bienvenidos a mi primera app con Django!" }
    estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/index.html', context)

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'myapp/cursos.html', {'cursos': cursos})

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'myapp/profesores.html', {'profesores': profesores})

def entregables(request):
    entregables = Entregable.objects.all()
    return render(request, 'myapp/entregables.html', {'entregables': entregables})

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/lista_estudiantes.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'myapp/detalle_estudiante.html', {'estudiante': estudiante})

# Create your views here.
