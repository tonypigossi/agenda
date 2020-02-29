from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from core.models import Evento

# def index(request):
#     return redirect('agenteste')
#
# def login_user(request):
#     return render(request, 'login.html')

def GetEventoLocal(request, titulo_evento):
    evento = Evento.objects.get(titulo = titulo_evento)
    return HttpResponse('<h1>Local do evento: {0}</h1>'.
                        format(evento.local_evento))


@login_required()
def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    data = {'eventos': eventos}
    return render(request, 'agenda.html', data)
