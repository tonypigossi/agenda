from django.shortcuts import render
from django.http import HttpResponse
from core.models import Evento


def GetEventoLocal(request, titulo_evento):
    evento = Evento.objects.get(titulo = titulo_evento)
    return HttpResponse('<h1>Local do evento: {0}</h1>'.format(evento.local_evento))
