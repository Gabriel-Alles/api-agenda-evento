from django.test import Client


def test_deve_criar_evento():
    client = Client()
    dados_requisicao = {
        "titulo": "Call de Alinhamento",
        "data": "2025-02-20T13:30:00Z",
        "horario_inicio": "14:00:00",
        "horario_fim": "15:00:00",
        "convidados": "gabriel.alles@hotmail.com",
        "local": "https://meet.google.com/rbr-hhfr-mnt",
        "descricao": "Call para teste"
    }

    response = client.post(path='/api/v1/eventos/', data=dados_requisicao, content_type='application/json')

    assert response.status_code == 200
    mensagem_response = response.json()['mensagem']
    assert mensagem_response == 'Dados recebidos com sucesso'

    dados_response = response.json()['dados']
    assert dados_response['titulo'] == 'Call de Alinhamento'
    assert dados_response['data'] == "2025-02-20T13:30:00Z"
    assert dados_response['horario_inicio'] == "14:00:00"
    assert dados_response['horario_fim'] == "15:00:00"
    assert dados_response['convidados'] == "gabriel.alles@hotmail.com"
    assert dados_response['local'] == "https://meet.google.com/rbr-hhfr-mnt"
    assert dados_response['descricao'] == "Call para teste"


def test_deve_listar_eventos():
    client = Client()
    response = client.get('/api/v1/eventos/')

    assert response.status_code == 200

    dados_response = response.json()[0]
    assert dados_response['titulo'] == 'Call de Alinhamento'
    assert dados_response['data'] == "2025-02-20T13:30:00Z"
    assert dados_response['horario_inicio'] == "14:00:00"
    assert dados_response['horario_fim'] == "15:00:00"
    assert dados_response['convidados'] == "gabriel.alles@hotmail.com"
    assert dados_response['local'] == "https://meet.google.com/rbr-hhfr-mnt"
    assert dados_response['descricao'] == "Call para teste"
