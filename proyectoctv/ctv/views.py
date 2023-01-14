from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "ctv/index.html", {})

def quienes_somos(request):
    return render(request, "ctv/quienessomos.html", {'navbar':'1'})

def programacion(request):
    return render(request, "ctv/programacion.html", {'navbar':'2'})

def programas(request):
    return render(request, "ctv/programas.html", {'navbar':'3'})

def contactos(request):
    return render(request, "ctv/contactos.html", {'navbar':'4'})

