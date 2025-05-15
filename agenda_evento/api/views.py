from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Evento  # Seu modelo
from agenda_evento.api.serializers import EventoSerializer  # Seu serializer
from rest_framework import status
from rest_framework.generics import get_object_or_404

class EventoViews(ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    # Método CREATE com retorno personalizado de ID e título
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # json > objeto
        serializer.is_valid(raise_exception=True)
        serializer.save()

        dados_response = {
            "evento_id": serializer.data["id"],
            "mensagem": f'Evento {serializer.data["titulo"]} criado com sucesso.'
        }
        return Response(dados_response, status.HTTP_201_CREATED)

    # Método LIST corrigido para retornar os dados serializados em JSON
    def list(self, request, *args, **kwargs):
        queryset = Evento.objects.all()
        serializer = self.get_serializer(queryset, many=True)  # objeto > json
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk):
        evento = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(evento)  
        return Response(serializer.data)
    
    def update(self, request, pk):
        evento = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(evento, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        evento = get_object_or_404(self.queryset, pk=pk)
        evento.delete()
        return Response(
            {
                'id': pk, 'mensagem': 'Evento removido com sucesso.'
            }
        )