from django.test import Client


def test_home_status(client: Client):
    response = client.get('/base')
    assert response.status_code == 200


def test_home_2(client: Client):
    response = client.get('/base')
    assert response.content == b'Oi, cliente'
