from django.contrib import admin
from .models import Programacion
# Register your models here.

#admin.site.register(Programacion)
@admin.register(Programacion)
class ProgramacionAdmin(admin.ModelAdmin):
    #listar los datos
    list_display = ('hora_emision', 'nombre', 'dias')

    #busqueda por nombre
    search_fields = ('nombre',)
    list_display_links = ('hora_emision', 'nombre')
