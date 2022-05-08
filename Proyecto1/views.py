from django.http import HttpResponse
from django.template import Template, Context, loader


def html(request):
    lista_de_nombre=["Pedro", "Ana" , "Dominga"]
    diccionario={"lista":lista_de_nombre}

    plantilla=loader.get_template("template1.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

