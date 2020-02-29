from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Evento

# def index(request):
#     return redirect('agenteste')

def GetEventoLocal(request, titulo_evento):
    evento = Evento.objects.get(titulo = titulo_evento)
    return HttpResponse('<h1>Local do evento: {0}</h1>'.
                        format(evento.local_evento))


def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    data = {'eventos': eventos}
    return render(request, 'agenda.html', data)
