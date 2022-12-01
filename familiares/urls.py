
from django.urls import path
from familiares.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("personaForm/", persona_form, name="personaForm"),
    path("paqueteForm/", paquete_form, name="paqueteForm"),
    path("celularForm/", celular_form, name="celularForm"),
    path("personas/", personas, name="personas"),
    path("paquetes/", paquetes, name="paquetes"),
    path("celulares/", celulares, name="celulares"),
    path("buscar/", buscar, name="buscar"),
    path("buscarpaquete/", busqueda_paquete, name="buscarpaquete"),  
]