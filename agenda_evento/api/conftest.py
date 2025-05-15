import pytest
from agenda_evento.api.factories import EventoFactory


@pytest.fixture
def evento_factory():
    return EventoFactory()


@pytest.fixture
def corpo_requisicao():
    return {
        "titulo": "Evento horário inválido",
        "data": "2025-02-20",
        "horario_inicio": "13:00:00",
        "horario_fim": "14:00:00",
        "convidados": ["gabriel.alles@hotmail.com"],
        "local": "https://meet.google.com/rbr-hhfr-mnt",
        "descricao": "Teste de funcionamento"
    }
