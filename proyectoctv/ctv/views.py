from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "ctv/index.html", {})

def quienes_somos(request):
    return render(request, "ctv/quienessomos.html", {})

def programacion(request):
    return render(request, "ctv/programacion.html", {})

def programas(request):
    return render(request, "ctv/programas.html", {})

def contactos(request):
    return render(request, "ctv/contactos.html", {})

