from django.shortcuts import render, HttpResponse
from .models import Programacion, Programa, Categoria

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
    lista_categorias = Categoria.objects.all()
    lista_programas = []

    #obteniendo la lista de programas ordenados por categoria
    for i in lista_categorias:
        print(i)
        lista_programas.append(Programa.objects.filter(categoria=i).order_by("nombre"))

    #creando el diccionario de programas
    diccionario_programas = { key:value for (key, value) in zip(lista_categorias, lista_programas) }
    
    print(diccionario_programas)
    return render(request, "ctv/programas.html", {'navbar':'3', 'lista_categorias':lista_categorias, 'diccionario_programas':diccionario_programas})

def contactos(request):
    return render(request, "ctv/contactos.html", {'navbar':'4'})

