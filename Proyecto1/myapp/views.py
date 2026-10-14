from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Estudiante, Profesor, Curso, Entregable, Avatar
from .forms import (
    CursoForm, CursoModelForm,
    ProfesorFormulario, ProfesorForm,
    EstudianteForm, EntregableForm,
    RegistroUsuarioForm, EditarPerfilForm, AvatarForm
)

# ================= ACCESO PÚBLICO (PORTAL DE LOGIN Y REGISTRO) =================
def index(request):
    if request.user.is_authenticated:
        return redirect('cursos')
    
    login_form = AuthenticationForm()
    registro_form = RegistroUsuarioForm()
    return render(request, 'myapp/index.html', {
        'login_form': login_form,
        'registro_form': registro_form,
        'active_tab': 'login'
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('cursos')

    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            usuario = login_form.get_user()
            login(request, usuario)
            return redirect('cursos')
    else:
        login_form = AuthenticationForm()

    registro_form = RegistroUsuarioForm()
    return render(request, 'myapp/index.html', {
        'login_form': login_form,
        'registro_form': registro_form,
        'active_tab': 'login'
    })

def registro_view(request):
    if request.user.is_authenticated:
        return redirect('cursos')

    if request.method == 'POST':
        registro_form = RegistroUsuarioForm(request.POST)
        if registro_form.is_valid():
            usuario = registro_form.save()
            login(request, usuario)
            return redirect('cursos')
    else:
        registro_form = RegistroUsuarioForm()

    login_form = AuthenticationForm()
    return render(request, 'myapp/index.html', {
        'login_form': login_form,
        'registro_form': registro_form,
        'active_tab': 'registro'
    })

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')


# ================= PERFIL Y AVATAR =================
@login_required
def editar_perfil(request):
    avatar, _ = Avatar.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = EditarPerfilForm(request.POST, instance=request.user)
        avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)

        if user_form.is_valid() and avatar_form.is_valid():
            user_form.save()
            avatar_form.save()
            return redirect('cursos')
    else:
        user_form = EditarPerfilForm(instance=request.user)
        avatar_form = AvatarForm(instance=avatar)

    return render(request, 'myapp/editar_perfil.html', {
        'user_form': user_form,
        'avatar_form': avatar_form
    })


# ================= CURSOS =================
@login_required
def cursos(request):
    query = request.GET.get('q')
    if query:
        cursos = Curso.objects.filter(
            models.Q(nombre__icontains=query) | models.Q(camada__icontains=query)
        )
    else:
        cursos = Curso.objects.all()
    return render(request, 'myapp/cursos.html', {'cursos': cursos, 'query': query})

@login_required
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

@login_required
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

@login_required
def curso_eliminar(request, id):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()
    return redirect('cursos')


# ================= PROFESORES =================
@login_required
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

@login_required
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

@login_required
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

@login_required
def profesor_eliminar(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    if request.method == 'POST':
        profesor.delete()
        return redirect('profesores')
    return render(request, 'myapp/profesor_confirm_delete.html', {'profesor': profesor})


# ================= ESTUDIANTES =================
@login_required
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

@login_required
def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'myapp/detalle_estudiante.html', {'estudiante': estudiante})

@login_required
def estudianteFormulario(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'myapp/estudiante_formulario.html', {'form': form})

@login_required
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

@login_required
def estudiante_eliminar(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()
    return redirect('lista_estudiantes')


# ================= ENTREGABLES =================
@login_required
def entregables(request):
    query = request.GET.get('q')
    curso_id = request.GET.get('curso_id')
    curso_seleccionado = None

    entregables_qs = Entregable.objects.select_related('curso').all()

    if curso_id:
        curso_seleccionado = get_object_or_404(Curso, id=curso_id)
        entregables_qs = entregables_qs.filter(curso_id=curso_id)

    if query:
        entregables_qs = entregables_qs.filter(
            models.Q(nombre__icontains=query) |
            models.Q(curso__nombre__icontains=query)
        )

    return render(request, 'myapp/entregables.html', {
        'entregables': entregables_qs,
        'query': query,
        'curso_seleccionado': curso_seleccionado
    })

@login_required
def entregableFormulario(request):
    curso_id = request.GET.get('curso_id')
    if request.method == 'POST':
        form = EntregableForm(request.POST)
        if form.is_valid():
            entregable = form.save()
            if entregable.curso:
                return redirect(f"/entregables/?curso_id={entregable.curso.id}")
            return redirect('entregables')
    else:
        initial_data = {'curso': curso_id} if curso_id else {}
        form = EntregableForm(initial=initial_data)
    return render(request, 'myapp/entregable_formulario.html', {'form': form})

@login_required
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

@login_required
def entregable_eliminar(request, id):
    entregable = get_object_or_404(Entregable, id=id)
    entregable.delete()
    return redirect('entregables')