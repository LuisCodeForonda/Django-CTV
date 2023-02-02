from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from proyectoctv.utils import unique_slug_generator
from ckeditor.fields import RichTextField
# Create your models here.

class Programacion(models.Model):

    DIAS_EN_EMISION = [
        ('1', 'Lunes a Viernes'),
        ('2', 'Sabados'),
        ('3', 'Domingos'),
    ]

    hora_emision = models.TimeField()
    nombre = models.CharField(max_length=100)
    dias = models.CharField(max_length=1, choices=DIAS_EN_EMISION, default='Lunes a Viernes')

    def __str__(self):
        diccionario = {"1":"Lunes a Viernes", "2": "Sabados", "3":"Domingos"}
        return "{} - {} - {}".format(self.hora_emision, self.nombre, diccionario[self.dias])

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self) :
        return self.nombre

class Programa(models.Model):
    LISTA_CATEGORIAS = [
        ('1', 'Religiosos'),
        ('2', 'Noticieros'),
        ('3', 'Analisis'),
        ('4', 'Familiares'),
        ('5', 'Entretenimiento'),
    ]

    categoria = models.CharField(max_length=1, choices=LISTA_CATEGORIAS, null=True, default='Religiosos')
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="programasimg", null=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    
    descripcion = models.TextField(max_length=200, blank=True)

    link_facebook = models.CharField(max_length=100, blank=True)
    link_twitter = models.CharField(max_length=100, blank=True)
    link_instagram = models.CharField(max_length=100, blank=True)
    link_tiktok =  models.CharField(max_length=100, blank=True)
    link_youtube =  models.CharField(max_length=100, blank=True)

    def __str__(self):
        diccionario_categorias = {"1":"Religiosos", "2": "Noticieros", "3":"Analisis", "4":"Familiares", "5":"Entretenimiento"}
        return "{} - {} - {}".format(self.nombre, self.hora_inicio, self.hora_fin)

class Noticia(models.Model):
    NOTICIA_CATEGORIA = [
        ('1', 'Sociedad'),
        ('2', 'Desastres y accidentes'),
        ('3', 'Seguridad'),
        ('4', 'Deportes'),
        ('5', 'Politica'),
        ('6', 'Entretenimiento'),
    ]

    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="noticiasimg", null=True)
    cuerpo = RichTextField()
    subcategoria = models.CharField(max_length=1, choices=NOTICIA_CATEGORIA, default='Sociedad')
    fecha = models.DateTimeField()
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titulo


def slug_generador(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

#antes de guardar genera el link dinamico este metodo presave genera el slug
pre_save.connect(slug_generador, sender=Noticia)