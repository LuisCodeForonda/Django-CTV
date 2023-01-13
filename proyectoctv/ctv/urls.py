from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('quienessomos/', views.quienes_somos, name="quienessomos"),
    path('programacion/', views.programacion, name="programacion"),
    path('programas/', views.programas, name="programas"),
    path("contactos/", views.contactos, name="contactos"),
]