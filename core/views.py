from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from core import models
from core import forms


def GetEventoLocal(request, titulo_evento):
    evento = Evento.objects.get(titulo = titulo_evento)
    return HttpResponse('<h1>Local do evento: {0}</h1>'.
                        format(evento.local_evento))


@login_required()
def lista_eventos(request):
    usuario = request.user
    eventos = models.Evento.objects.filter(usuario=usuario)
    data = {'eventos': eventos}
    return render(request, 'agenda.html', data)


@login_required()
def evento(request):
    return render(request, 'evento.html')

def __get_data_evento(request):
    evento = models.Evento()
    evento.titulo = request.POST.get('titulo_evento')
    evento.descricao = request.POST.get('descricao_evento')
    evento.local_evento = request.POST.get('local_evento')
    evento.data_evento = request.POST.get('data_evento')
    evento.usuario = request.user
    return evento

@login_required()
def evento_update(request, id_evento):
    try:
        if request.method == 'POST':
            dadosPOST = __get_data_evento(request)
            dadosPOST.id = id_evento
            evento = models.Evento.objects.filter(id=id_evento)
            evento = dadosPOST
            evento.save()
            return redirect('agenda')
        else:
            data = {}
            data['evento'] = models.Evento.objects.get(id=id_evento)
            return render(request, 'evento.html', data)
    except Exception as e:
        mensagem = str(e)
        print(mensagem)
    else:
        mensagem = 'Salvo som sucesso!'


@login_required()
def evento_create(request):
    try:
        if request.method == 'POST':
            __get_data_evento(request).save()
            return redirect('agenda')
        else:
            return render(request, 'evento.html')
    except Exception as e:
        mensagem = str(e)
    else:
        mensagem = 'Salvo som sucesso!'

@login_required()
def evento_delete(request, id_evento):
    usuario = request.user
    evento = models.Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        models.Evento.objects.filter(id=id_evento).delete()

    return redirect('agenda')
