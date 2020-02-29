from django.db import models
from django.contrib.auth.models import User

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
    data_cricao = models.DateTimeField(auto_now=True,
                                       verbose_name='Data da criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')
