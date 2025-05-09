from django.db import models
import json


class Evento(models.Model):
    titulo = models.CharField(max_length=200, default="Sem título")
    data = models.DateTimeField(null=True, blank=True)
    horario_inicio = models.TimeField(null=True, blank=True)
    horario_fim = models.TimeField(null=True, blank=True)
    convidados = models.TextField(null=True, blank=True)  # Usando TextField
    local = models.URLField(default="https://")
    descricao = models.TextField(default="")

    def save(self, *args, **kwargs):
        # Se convidados não for None ou vazio, converte para uma string JSON
        if self.convidados:
            try:
                # Converte a lista de convidados para uma string JSON
                self.convidados = json.dumps(self.convidados)
            except Exception as e:
                print(f"Erro ao salvar convidados: {e}")
        super().save(*args, **kwargs)

    def get_convidados(self):
        # Converte de volta para a lista de convidados, se necessário
        if self.convidados:
            try:
                return json.loads(self.convidados)
            except Exception as e:
                print(f"Erro ao carregar convidados: {e}")
                return []
        return []

    def __str__(self):
        return self.titulo
