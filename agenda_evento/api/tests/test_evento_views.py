import pytest
from django.test import Client
from rest_framework import status

pytestmark = pytest.mark.django_db

PATH = '/api/v1/eventos/'

# Testa criação com campo obrigatório ausente


def test_erro_ao_criar_evento_sem_titulo(corpo_requisicao):
    client = Client()
    corpo_requisicao.pop('titulo')  # Remove o título

    response = client.post(path=PATH, data=corpo_requisicao, content_type='application/json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'titulo' in response.json()


# Testa criação com data em formato inválido
def test_erro_ao_criar_evento_com_data_invalida(corpo_requisicao):
    client = Client()
    corpo_requisicao['data'] = '20-02-2025'  # Formato errado

    response = client.post(path=PATH, data=corpo_requisicao, content_type='application/json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'data' in response.json()


# Testa criação com horário final anterior ao inicial
def test_erro_ao_criar_evento_com_horario_invalido():
    client = Client()
    dados_requisicao = {
        "titulo": "Evento horário inválido",
        "data": "2025-02-20",
        "horario_inicio": "15-30-00",
        "horario_fim": "13-00-00",  # fim antes do início
        "convidados": ["gabriel.alles@hotmail.com"],
        "local": "https://meet.google.com/rbr-hhfr-mnt",
        "descricao": "Horário inválido"
    }

    response = client.post(path=PATH, data=dados_requisicao, content_type='application/json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'horario_fim' in response.json() or 'non_field_errors' in response.json()


# Testa criação com e-mail de convidado inválido
def test_erro_ao_criar_evento_com_email_invalido(corpo_requisicao):
    client = Client()
    corpo_requisicao['convidados'] = 'email_invalido'

    response = client.post(path=PATH, data=corpo_requisicao, content_type='application/json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'convidados' in response.json()
