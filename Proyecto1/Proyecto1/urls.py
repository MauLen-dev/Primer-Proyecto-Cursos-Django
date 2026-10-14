"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),

    # Cursos
    path('cursos/', views.cursos, name="cursos"),
    path('cursoform/', views.cursoform, name="cursoform"),
    path('curso/editar/<int:id>/', views.curso_editar, name="cursoEditar"),
    path('curso/eliminar/<int:id>/', views.curso_eliminar, name="cursoEliminar"),

    # Profesores
    path('profesores/', views.profesores, name="profesores"),
    path('profesorFormulario/', views.profesorFormulario, name="profesorFormulario"),
    path('profesor/editar/<int:id>/', views.profesor_editar, name="profesorEditar"),
    path('profesor/eliminar/<int:id>/', views.profesor_eliminar, name="profesorEliminar"),

    # Estudiantes
    path('lista_estudiantes/', views.lista_estudiantes, name="lista_estudiantes"),
    path('detalle_estudiante/<int:pk>/', views.detalle_estudiante, name="detalle_estudiante"),
    path('estudianteFormulario/', views.estudianteFormulario, name="estudianteFormulario"),
    path('estudiante/editar/<int:id>/', views.estudiante_editar, name="estudianteEditar"),
    path('estudiante/eliminar/<int:id>/', views.estudiante_eliminar, name="estudianteEliminar"),

    # Entregables
    path('entregables/', views.entregables, name="entregables"),
    path('entregableFormulario/', views.entregableFormulario, name="entregableFormulario"),
    path('entregable/editar/<int:id>/', views.entregable_editar, name="entregableEditar"),
    path('entregable/eliminar/<int:id>/', views.entregable_eliminar, name="entregableEliminar"),
    
    # Usuarios (Login / Registro / Logout / Perfil)
    path('login/', views.login_view, name="login"),
    path('registro/', views.registro_view, name="registro"),
    path('logout/', views.logout_view, name="logout"),
    path('perfil/editar/', views.editar_perfil, name="editar_perfil"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)