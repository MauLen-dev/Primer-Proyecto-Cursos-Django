from django import forms
from .models import Profesor, Estudiante, Curso, Entregable

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre del Curso")
    camada = forms.IntegerField(label="Camada")

class CursoModelForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada']

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    apellido = forms.CharField(max_length=100, label="Apellido")
    email = forms.EmailField(label="Correo electrónico")
    profesion = forms.CharField(max_length=100, label="Profesión")

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'profesion']

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']

class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'fecha_de_entrega', 'entregado']
        widgets = {
            'fecha_de_entrega': forms.DateInput(attrs={'type': 'date'}),
        }