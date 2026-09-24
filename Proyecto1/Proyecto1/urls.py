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

app_name = "myapp"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('cursos/', views.cursos, name="cursos"),
    path('profesores/', views.profesores, name="profesores"),
    path('entregables/', views.entregables, name="entregables"),
    path('lista_estudiantes/', views.lista_estudiantes, name="lista_estudiantes"),
    path('detalle_estudiante/<int:pk>/', views.detalle_estudiante, name="detalle_estudiante"),
    path('cursoform/', views.cursoform, name="cursoform"),
    path('profesorFormulario/', views.profesorFormulario, name="profesorFormulario"),
    path('profesor/editar/<int:id>', views.profesor_editar, name="profesor_editar"),
]
