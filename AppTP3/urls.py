from django.urls import path
from AppTP3.views import *

urlpatterns = [

    path("crear_build/", crear_build, name="Build"),
    path("crear_armaduras/", crear_armaduras,name="Armaduras" ),
    path("crear_personaje/", crear_personaje, name="Personaje"),
    path("buscar_personaje/", buscar_personaje,),
    path("", inicio, name="Home"),
]