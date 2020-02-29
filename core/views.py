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
    mensagem = ''
    id_evento = request.GET.get('id_evento')
    print(id_evento)
    if id_evento is not None and request.method != 'POST':
        data = {}
        data['evento'] = models.Evento.objects.get(id=id_evento)
        return render(request, 'evento.html', data)
    elif request.method == 'POST':
        try:
            titulo = request.POST.get('titulo_evento')
            descricao = request.POST.get('descricao_evento')
            local_evento= request.POST.get('local_evento')
            data_evento = request.POST.get('data_evento')
            usuario = request.user
            if id_evento is not None:
                if models.Evento.objects.get(id=id_evento).usuario == usuario:
                    models.Evento.objects.filter(id=id_evento).update(
                                                 titulo=titulo,
                                                 descricao=descricao,
                                                 data_evento=data_evento,
                                                 local_evento=local_evento,
                                                 usuario=usuario
                                                 )
            else:
                models.Evento.objects.create(titulo=titulo,
                                             descricao=descricao,
                                             data_evento=data_evento,
                                             local_evento=local_evento,
                                             usuario=usuario
                                             )
        except Exception as e:
            mensagem = str(e)
            # return render(request, 'evento.html', {'mensagem': mensagem})
        else:
            # mensagem = 'Salvo com sucesso'
            return redirect('agenda')

    return render(request, 'evento.html')


@login_required()
def delete_evento(request, id_evento):
    usuario = request.user
    evento = models.Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        models.Evento.objects.filter(id=id_evento).delete()

    return redirect('agenda')
