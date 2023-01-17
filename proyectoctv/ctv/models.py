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