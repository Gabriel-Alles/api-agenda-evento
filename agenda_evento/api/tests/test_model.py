import pytest
from agenda_evento.api.models import Evento

@pytest.mark.django_db
def test_deve_criar_evento_na_base(evento_factory):
    assert evento_factory.titulo == 'Teste teste'
    assert str(evento_factory.data) == '2025-05-20'  # garante que o DateField seja comparado corretamente
    assert str(evento_factory.horario_inicio) == '13:00:00'
    assert str(evento_factory.horario_fim) == '15:30:00'
    assert evento_factory.convidados == ['gabriel.teste@teste.com', 'teste.teste@gpa.com']
    assert evento_factory.local == 'Google Meet'
    assert evento_factory.descricao == 'Testando modulo'

    assert Evento.objects.count() == 1