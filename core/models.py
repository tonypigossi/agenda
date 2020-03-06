from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descricao = models.TextField(
                                blank=True,
                                null=True,
                                verbose_name='Descrição',
                                )
    local_evento = models.CharField(
                                    max_length=50,
                                    blank=True,
                                    null=True,
                                    verbose_name='Local do evento'
                                    )
    data_evento = models.DateTimeField(verbose_name='Data do eventos')
    data_create = models.DateTimeField(auto_now=True,
                                       verbose_name='Data da criação')
    cor = models.CharField(max_length=7, default='#3788d8')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')

    def get_data_evento_input(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_data_evento_atrasado(self):
        return self.data_evento < datetime.now()
