from django.db import models

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

    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
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
    