# Projeto desenvolvido no curso Desenvolvedor Contratado

### api-agenda-evento
API de Agenda de Evento para criação, listagem, edição e deleção de um evento.


# Passo a passo para rodar a aplicação

Foi utilizado o Python 3.9

### Instalar as dependências
```
pip install -r requirements-dev.txt
```

### Subir a base de dados PostgreSQL
```
docker-compose up -d
```

### Executar Aplicação
```
python manage.py
```

# Documentação da API
A documentação da api está disponível em 'http://127.0.0.8000/swagger/'

# Convenções de código e testes

### Rodar convenção de código
```
flake8
```

### Rodar testes
```
pytest
```

OBS: Ambos foram implementados no CI (Github Actions)