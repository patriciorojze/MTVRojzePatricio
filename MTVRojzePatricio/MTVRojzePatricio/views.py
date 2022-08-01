
from pydoc import plain
from django.http import HttpResponse
from django.template import Template, Context, loader
from MiappRojzePatricio.models import Familiar, Domicilios
import datetime


def vista_principal(request):
    
    familiares = Familiar.objects.all()
    
    domicilios = Domicilios.objects.all()
    
    domicilios_diccionario = {"domicilios": [], "familiares": []}
    
    for domicilio in domicilios:
        nuevo_domicilio = (domicilio.Direccion, domicilio.Ciudad, domicilio.Provincia, domicilio.NroAmbientes)
        domicilios_diccionario["domicilios"].append(nuevo_domicilio)

    for familiar in familiares:
        nuevo_familiar = (familiar.Nombre, familiar.Apellido, familiar.Edad, familiar.FechaNacimiento.year, familiar.FechaNacimiento.month, familiar.FechaNacimiento.day)
        domicilios_diccionario["familiares"].append(nuevo_familiar)

    contenido = loader.get_template("vista.html")

    archivo_renderizado = contenido.render(domicilios_diccionario)

    return HttpResponse(archivo_renderizado)