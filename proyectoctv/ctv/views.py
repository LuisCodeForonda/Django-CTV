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
    religiosos = Programa.objects.filter(categoria="1")
    noticieros = Programa.objects.filter(categoria="2")
    analisis = Programa.objects.filter(categoria="3")
    familiares = Programa.objects.filter(categoria="4")
    entretenimiento = Programa.objects.filter(categoria="5")

    return render(request, "ctv/programas.html", {'navbar':'3', 'religiosos':religiosos, 'noticieros':noticieros, 'analisis':analisis, 'familiares':familiares, 'entretenimiento':entretenimiento})

def contactos(request):
    return render(request, "ctv/contactos.html", {'navbar':'4'})

