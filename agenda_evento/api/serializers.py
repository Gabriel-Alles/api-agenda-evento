from rest_framework import serializers
from agenda_evento.models import Evento

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'  # Ou você pode listar os campos manualmente, se preferir
