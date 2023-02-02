from django.shortcuts import render, HttpResponse
from .models import Programacion, Programa, Noticia
from django.shortcuts import get_object_or_404


# Create your views here.

def index(request):
    sociedad = Noticia.objects.filter(subcategoria=1).order_by('-fecha')[:3]
    accidentes = Noticia.objects.filter(subcategoria=2)
    seguridad = Noticia.objects.filter(subcategoria=3)
    deportes = Noticia.objects.filter(subcategoria=4)
    politica = Noticia.objects.filter(subcategoria=5)
    entretenimiento = Noticia.objects.filter(subcategoria=6)

    return render(request, "ctv/index.html", {'sociedad':sociedad, 'accidentes':accidentes, 'seguridad':seguridad, 'deportes':deportes, 'politica':politica, 'entretenimiento':entretenimiento})

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


def detallenoticia(request,  slug_text):
    noticia = get_object_or_404(Noticia, slug=slug_text)
    titulares = Noticia.objects.order_by('-fecha')[:6]
    return render(request, "ctv/detallenoticia.html", {'noticia':noticia, 'titulares':titulares})

