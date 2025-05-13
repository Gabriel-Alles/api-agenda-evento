import factory
from agenda_evento.api.models import Evento



class EventoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Evento

    titulo = 'Teste teste'
    data = '2025-05-20'
    horario_inicio = '13:00:00'
    horario_fim = '15:30:00'
    convidados = ['gabriel.teste@teste.com', 'teste.teste@gpa.com']  
    local = 'Google Meet'
    descricao = 'Testando modulo'
