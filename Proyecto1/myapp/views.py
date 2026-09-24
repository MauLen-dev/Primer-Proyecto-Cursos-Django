from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable
from .forms import CursoForm, ProfesorFormulario, ProfesorForm
from django.db import models

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

def cursoform(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            camada = form.cleaned_data['camada']
            curso  = Curso(nombre=nombre, camada=camada)
            curso.save()
            return render(request, 'myapp/curso_exito.html')
    else:
        form = CursoForm()
    return render(request, 'myapp/curso_formulario.html', {'form': form})  

def profesorFormulario(request):
   if request.method == 'POST':
     form = ProfesorFormulario(request.POST) 
     if form.is_valid():
      nombre = form.cleaned_data['nombre']
      apellido = form.cleaned_data['apellido']
      email = form.cleaned_data['email']
      profesion = form.cleaned_data['profesion']
      profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
      profesor.save()
      return redirect('profesores')
   else:
    form = ProfesorFormulario() 
   return render(request, 'myapp/profesor_formulario.html', {'form': form})

def profesoresBusqueda(request):
    query = request.GET.get('q')
    if query:
        profesores = Profesor.objects.filter(models.Q(nombre__icontains=query) | models.Q(apellido__icontains=query) | models.Q(profesion__icontains=query))
    else:
        profesores = Profesor.objects.all()
    return render(request, 'myapp/profesores.html', {'profesores': profesores, 'query': query,})        
     
              
# Create your views here.