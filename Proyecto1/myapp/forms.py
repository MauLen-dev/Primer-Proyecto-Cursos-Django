from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    camada= forms.IntegerField()

class ProfesorFormulario(forms.Form):
   nombre = forms.CharField(max_length=10, label="Nombre")
   apellido = forms.CharField(max_length=100, label="Apellido")
   email = forms.EmailField(label="Correo electrónico")
   profesion = forms.CharField(max_length=100, label="Profesion")
        