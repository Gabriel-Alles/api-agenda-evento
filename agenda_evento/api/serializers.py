from rest_framework import serializers
from .models import Evento


class EventoSerializer(serializers.ModelSerializer):
    convidados = serializers.ListField(
        child=serializers.EmailField(),
        allow_empty=False
    )

    class Meta:
        model = Evento
        fields = [
            'id',
            'titulo',
            'data',
            'horario_inicio',
            'horario_fim',
            'convidados',  # Aqui colocado depois do horario_fim
            'local',
            'descricao',
        ]
