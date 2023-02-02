from django.contrib import admin
from .models import Programacion, Programa, Noticia
from django.db import models
# Register your models here.

#admin.site.register(Programacion)
@admin.register(Programacion)
class ProgramacionAdmin(admin.ModelAdmin):
    #listar los datos que se muestran
    list_display = ('hora_emision', 'nombre', 'dias')

    #busqueda por nombre
    search_fields = ('nombre',)

    #por que celdas de pueden editar
    list_display_links = ('hora_emision', 'nombre')

#admin.site.register(Programa)
@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'hora_inicio', 'hora_fin')

    search_fields = ('nombre',)

    list_display_links = ('nombre', 'categoria')


#admin.site.register(Noticia)
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subcategoria', 'fecha')

    search_fields = ('titulo',)

    list_display_links = ('titulo', 'subcategoria')

