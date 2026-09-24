from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    camada= forms.IntegerField()
    