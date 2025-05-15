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
        "horario_fim": "16-00-00",
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
    corpo_requisicao['convidados'] = ["email_invalido"]  # Deve ser lista com string inválida

    response = client.post(path=PATH, data=corpo_requisicao, content_type='application/json')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'convidados' in response.json()


def test_deve_listar_evento_por_id(client: Client, corpo_requisicao):
    corpo_requisicao['titulo'] = 'Teste Evento por id'

    response_post = client.post(PATH, data=corpo_requisicao, content_type='application/json')
    print("Resposta JSON:", response_post.json())

    assert response_post.status_code == status.HTTP_201_CREATED

    evento_id = response_post.json().get('evento_id')  # Aqui mudou para 'evento_id'
    assert evento_id is not None

    response = client.get(f'{PATH}{evento_id}/')
    assert response.status_code == status.HTTP_200_OK

    assert response.json()['id'] == evento_id
    assert response.json()['titulo'] == 'Teste Evento por id'
    assert response.json()['data'] == '2025-02-20'
    assert response.json()['horario_inicio'] == '13:00:00'
    assert response.json()['horario_fim'] == '14:00:00'
    assert response.json()['convidados'] == ["gabriel.alles@hotmail.com"]
    assert response.json()['local'] == 'https://meet.google.com/rbr-hhfr-mnt'
    assert response.json()['descricao'] == 'Teste de funcionamento'


def test_nao_deve_listar_evento_nao_encontrado(client: Client):
    response = client.get(f'{PATH}1000/')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert 'detail' in response.json()
    assert 'No Evento matches the given query.' in response.json()['detail']


def test_deve_editar_evento(client: Client, corpo_requisicao):
    response_post = client.post(PATH, data=corpo_requisicao, content_type='application/json')
    print("RESPONSE POST JSON:", response_post.json())

    assert response_post.status_code == status.HTTP_201_CREATED

    # Use 'evento_id' ou 'id' conforme sua API retornar
    evento_json = response_post.json()
    evento_id = evento_json.get('id') or evento_json.get('evento_id')
    assert evento_id is not None

    dados_requisicao_put = {
        "titulo": "Evento de Testes - Editado",
        "data": "2025-02-20",
        "horario_inicio": "13:30:00",
        "horario_fim": "14:00:00",
        "convidados": ["gabriel.alles@hotmail.com"],
        "local": "https://meet.google.com/rbr-hhfr-mnt",
        "descricao": "Teste de funcionamento 2"
    }

    response = client.put(f'{PATH}{evento_id}/', data=dados_requisicao_put, content_type='application/json')

    assert response.status_code == status.HTTP_200_OK

    response_data = response.json()
    assert response_data['titulo'] == 'Evento de Testes - Editado'
    assert response_data['data'] == '2025-02-20'
    assert response_data['horario_inicio'] == '13:30:00'
    assert response_data['horario_fim'] == '14:00:00'
    assert response_data['convidados'] == ["gabriel.alles@hotmail.com"]
    assert response_data['local'] == 'https://meet.google.com/rbr-hhfr-mnt'
    assert response_data['descricao'] == 'Teste de funcionamento 2'


def test_deve_deletar_evento(client: Client, corpo_requisicao):
    response_post = client.post(PATH, data=corpo_requisicao)
    evento_id = response_post.data['evento_id']

    response_delete = client.delete(f'{PATH}{evento_id}/')

    assert response_delete.status_code == status.HTTP_200_OK
    assert response_delete.data['id'] == str(evento_id)
    assert response_delete.data['mensagem'] == 'Evento removido com sucesso.'

    response_get = client.get(f'{PATH}{evento_id}/')
    assert response_get.status_code == status.HTTP_404_NOT_FOUND
