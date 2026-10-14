from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import Estudiante, Profesor, Curso, Entregable
from .forms import (
    CursoForm, CursoModelForm,
    ProfesorFormulario, ProfesorForm,
    EstudianteForm, EntregableForm
)

def index(request):
    context = {"mensaje": "¡Bienvenidos a mi primera app con Django!"}
    return render(request, 'myapp/index.html', context)

# ================= CURSOS =================
def cursos(request):
    query = request.GET.get('q')
    if query:
        cursos = Curso.objects.filter(
            models.Q(nombre__icontains=query) | models.Q(camada__icontains=query)
        )
    else:
        cursos = Curso.objects.all()
    return render(request, 'myapp/cursos.html', {'cursos': cursos, 'query': query})

def cursoform(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            camada = form.cleaned_data['camada']
            curso = Curso(nombre=nombre, camada=camada)
            curso.save()
            return redirect('cursos')
    else:
        form = CursoForm()
    return render(request, 'myapp/curso_formulario.html', {'form': form})

def curso_editar(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoModelForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursoModelForm(instance=curso)
    return render(request, 'myapp/curso_editar.html', {'form': form, 'curso': curso})

def curso_eliminar(request, id):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()
    return redirect('cursos')


# ================= PROFESORES =================
def profesores(request):
    query = request.GET.get('q')
    if query:
        profesores = Profesor.objects.filter(
            models.Q(nombre__icontains=query) |
            models.Q(apellido__icontains=query) |
            models.Q(profesion__icontains=query)
        )
    else:
        profesores = Profesor.objects.all()
    return render(request, 'myapp/profesores.html', {'profesores': profesores, 'query': query})

def profesorFormulario(request):
    if request.method == 'POST':
        form = ProfesorFormulario(request.POST)
        if form.is_valid():
            Profesor.objects.create(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                profesion=form.cleaned_data['profesion']
            )
            return redirect('profesores')
    else:
        form = ProfesorFormulario()
    return render(request, 'myapp/profesor_formulario.html', {'form': form})

def profesor_editar(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('profesores')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'myapp/profesor_editar.html', {'form': form, 'profesor': profesor})

def profesor_eliminar(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    if request.method == 'POST':
        profesor.delete()
        return redirect('profesores')
    return render(request, 'myapp/profesor_confirm_delete.html', {'profesor': profesor})


# ================= ESTUDIANTES =================
def lista_estudiantes(request):
    query = request.GET.get('q')
    if query:
        estudiantes = Estudiante.objects.filter(
            models.Q(nombre__icontains=query) |
            models.Q(apellido__icontains=query) |
            models.Q(email__icontains=query)
        )
    else:
        estudiantes = Estudiante.objects.all()
    return render(request, 'myapp/lista_estudiantes.html', {'estudiantes': estudiantes, 'query': query})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'myapp/detalle_estudiante.html', {'estudiante': estudiante})

def estudianteFormulario(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'myapp/estudiante_formulario.html', {'form': form})

def estudiante_editar(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'myapp/estudiante_editar.html', {'form': form, 'estudiante': estudiante})

def estudiante_eliminar(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()
    return redirect('lista_estudiantes')


# ================= ENTREGABLES =================
def entregables(request):
    query = request.GET.get('q')
    if query:
        entregables = Entregable.objects.filter(nombre__icontains=query)
    else:
        entregables = Entregable.objects.all()
    return render(request, 'myapp/entregables.html', {'entregables': entregables, 'query': query})

def entregableFormulario(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entregables')
    else:
        form = EntregableForm()
    return render(request, 'myapp/entregable_formulario.html', {'form': form})

def entregable_editar(request, id):
    entregable = get_object_or_404(Entregable, id=id)
    if request.method == 'POST':
        form = EntregableForm(request.POST, instance=entregable)
        if form.is_valid():
            form.save()
            return redirect('entregables')
    else:
        form = EntregableForm(instance=entregable)
    return render(request, 'myapp/entregable_editar.html', {'form': form, 'entregable': entregable})

def entregable_eliminar(request, id):
    entregable = get_object_or_404(Entregable, id=id)
    entregable.delete()
    return redirect('entregables')