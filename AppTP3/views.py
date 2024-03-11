from django.shortcuts import render
from django.http import HttpResponse
from AppTP3.models import Build, Personajes, Armaduras

# Create your views here.

def inicio (request):
    return render(request, "inicio.html")

def crear_armaduras(request):
    if request.method == "POST": #CUANDO APRIETO EL BOTON ENVIAR 
        build_nuevo = Armaduras(nombre_armadura = request.POST["nombre_armadura"],tipo_armadura=request.POST ["tipo_armadura"],lv_armadura=request.POST ["lv_armadura"] )
        build_nuevo.save()
        return render(request,  "inicio.html")
    return render(request, "crear_armaduras.html")


def crear_personaje(request):

    if request.method == "POST": #CUANDO APRIETO EL BOTON ENVIAR 
        
        build_nuevo = Personajes(nombre = request.POST["nombre"],raza=request.POST ["raza"],averno=request.POST ["averno"] )
        build_nuevo.save()
        return render(request,  "inicio.html")
    return render(request, "crear_personaje.html")

def crear_build(request):

    if request.method == "POST": #CUANDO APRIETO EL BOTON ENVIAR 
        
        build_nuevo = Build(nombre = request.POST["nombre"],tipo_daño=request.POST ["tipo_daño"],Total_daño=request.POST ["Total_daño"]  )
        build_nuevo.save()
        return render(request,  "inicio.html")
    return render(request,  "crear_build.html")


def buscar_personaje (request):

    if request.GET ["nombre"]:

        nombre = request.GET["nombre"]
        personaje = Personajes.objects.filter(nombre__icontains=nombre)

        mensaje = f"estamos buscando al personaje {nombre}"
    
        return render(request, "resultado_personaje.html", {"mensaje":mensaje, "resultados":personaje})
    
    return render(request, "resultado_personaje.html")