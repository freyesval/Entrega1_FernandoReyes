from django.shortcuts import render
from .models import Persona, Paquete, Celular
from django.http import HttpResponse
from django.template import Template, Context, loader
from familiares.forms import PersonaForm, PaqueteForm, CelularForm

# Create your views here.
def inicio(request):
    return render (request, "familiares/inicio.html")



def persona_form(request):
    
    if request.method=="POST":
        form=PersonaForm(request.POST)
        print("-------------------------------")
        print(form)
        print("-------------------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)            
            nombre = informacion["nombre"]
            edad = informacion["edad"]
            fecha_nacimiento = informacion["fecha_nacimiento"]
            persona = Persona(nombre=nombre,edad=edad, fecha_nacimiento= fecha_nacimiento)
            persona.save()
            return render (request, "familiares/inicio.html")
    else:
        formulario=PersonaForm()


    return render(request, "familiares/personaForm.html", {"form":formulario})


def paquete_form(request):
    
    if request.method=="POST":
        form=PaqueteForm(request.POST)
        print("-------------------------------")
        print(form)
        print("-------------------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre = informacion["nombre"]
            peso = informacion["peso"]
            remitente = informacion["remitente"]
            destinatario = informacion["destinatario"]
            paquete = Paquete(nombre=nombre, peso=peso, remitente=remitente, destinatario=destinatario)
            paquete.save()
            return render (request, "familiares/inicio.html")
    else:
        formulario=PaqueteForm()


    return render(request, "familiares/paqueteForm.html", {"form":formulario})


def celular_form(request):
    
    if request.method=="POST":
        form=CelularForm(request.POST)
        print("-------------------------------")
        print(form)
        print("-------------------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)

            
            nombre = informacion["nombre"]
            modelo = informacion["modelo"]
            marca = informacion["marca"]
            fecha_lanzamiento = informacion["fecha_lanzamiento"]
            celular = Celular(nombre=nombre, modelo=modelo, marca=marca, fecha_lanzamiento=fecha_lanzamiento)
            celular.save()
            return render (request, "familiares/inicio.html")
    else:
        formulario=CelularForm()


    return render(request, "familiares/celularForm.html", {"form":formulario})


def personas(request):
    return render (request, "familiares/personas.html")


def paquetes(request):
    return render (request, "familiares/paquetes.html")


def celulares(request):
    return render (request, "familiares/celulares.html")


def busqueda_paquete(request):
    return render(request, "familiares/busquedaPaquete.html")


def buscar(request):
    
    if request.GET["nombre"]:

        nombre=request.GET["nombre"]

        paquete=Paquete.objects.filter(nombre__icontains=nombre)
        print(paquete)
        return render(request,"familiares/resultadosBusqueda.html", {"paquetes":paquete} )
    else:
        return render(request, "familiares/resultadosBusqueda.html", {"mensaje":"Ingresa el nombre del paquete a encontrar: "})