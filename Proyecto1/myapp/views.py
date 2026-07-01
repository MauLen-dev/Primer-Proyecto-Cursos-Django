from django.shortcuts import render

def index(request):
    context = { "mensaje": "¡Bienvenidos a mi primera app con Django!" }
    return render(request, 'myapp/index.html', context)
# Create your views here.
