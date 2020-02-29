from django.forms import ModelForm
from core import models


class EventoForm(ModelForm):
    class Meta:
        model = models.Evento
        fields = '__all__'
