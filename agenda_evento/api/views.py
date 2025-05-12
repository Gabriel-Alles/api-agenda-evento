from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Evento  # Seu modelo
from agenda_evento.api.serializers import EventoSerializer  # Seu serializer


class EventoViews(ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    # O método create será sobrescrito para manter sua resposta personalizada
    def create(self, request, *args, **kwargs):
        # Aqui você pode manter a lógica de enviar a mensagem de sucesso
        dados_response = {
            'mensagem': 'Dados recebidos com sucesso',
            'dados': request.data
        }
        return Response(dados_response, status=200)

    def list(self, request):
        response_listagem_evento = [
            {
                "titulo": "Call de Alinhamento",
                "data": "2025-02-20T13:30:00Z",
                "horario_inicio": "14:00:00",
                "horario_fim": "15:00:00",
                "convidados": "gabriel.alles@hotmail.com",
                "local": "https://meet.google.com/rbr-hhfr-mnt",
                "descricao": "Call para teste"
            }
        ]
        return Response(response_listagem_evento, 200)
