from rest_framework import serializers
from .models import Evento


class EventoSerializer(serializers.ModelSerializer):
    # Validação de cada item da lista como um email válido
    convidados = serializers.ListField(
        child=serializers.EmailField(),  # Isso garante a validação correta de cada e-mail
        allow_empty=False
    )

    class Meta:
        model = Evento
        fields = '__all__'
