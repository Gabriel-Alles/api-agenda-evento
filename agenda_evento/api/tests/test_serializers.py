import pytest
import datetime
from agenda_evento.api.serializers import EventoSerializer


pytestmark = pytest.mark.django_db



def test_deve_serializar_evento(evento_factory):
    serializer = EventoSerializer(evento_factory)

    assert isinstance(serializer.data, dict)

    assert serializer.data['titulo'] == 'Teste teste'
    assert serializer.data['data'] == '2025-05-20'
    assert serializer.data['horario_inicio'] == '13:00:00'
    assert serializer.data['horario_fim'] == '15:30:00'
    assert serializer.data['convidados'] == ['gabriel.teste@teste.com', 'teste.teste@gpa.com']
    assert serializer.data['local'] == 'Google Meet'
    assert serializer.data['descricao'] == 'Testando modulo'


def test_deve_desserializar_evento():
    evento = {
        "titulo": "teste3",
        "data": "2025-02-20",
        "horario_inicio": "14:00:00",
        "horario_fim": "15:00:00",
        "convidados": ["gabriel.alles@hotmail.com"],
        "local": "https://meet.google.com/rbr-hhfr-mnt",
        "descricao": "Call para teste 221"
    }

    serializar = EventoSerializer(data=evento)

    assert serializar.is_valid(), f"Erro na validação: {serializar.errors}"

    evento_desserializado = serializar.save()

    assert isinstance(evento_desserializado, object)
    assert evento_desserializado.titulo == "teste3"
    assert evento_desserializado.data == datetime.date(2025, 2, 20)
    assert evento_desserializado.horario_inicio == datetime.time(14, 0)
    assert evento_desserializado.horario_fim == datetime.time(15, 0)
    assert evento_desserializado.convidados == ["gabriel.alles@hotmail.com"]
    assert evento_desserializado.local == "https://meet.google.com/rbr-hhfr-mnt"
    assert evento_desserializado.descricao == "Call para teste 221"
