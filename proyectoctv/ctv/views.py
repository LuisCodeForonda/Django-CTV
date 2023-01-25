from django.shortcuts import render, HttpResponse
from .models import Programacion, Programa

# Create your views here.

def index(request):
    return render(request, "ctv/index.html", {})

def quienes_somos(request):
    return render(request, "ctv/quienessomos.html", {'navbar':'1'})

def programacion(request):
    lunes_viernes = Programacion.objects.filter(dias="1").order_by("hora_emision")
    sabados =  Programacion.objects.filter(dias="2").order_by("hora_emision")
    domingos =  Programacion.objects.filter(dias="3").order_by("hora_emision")

    return render(request, "ctv/programacion.html", {'navbar':'2', 'lunes_viernes': lunes_viernes, 'sabados': sabados, 'domingos':domingos})

def programas(request):
    noticieros = Programa.objects.filter(categoria="2").order_by("nombre")

    return render(request, "ctv/programas.html", {'navbar':'3', 'noticieros': noticieros})

def contactos(request):
    return render(request, "ctv/contactos.html", {'navbar':'4'})

