from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Remedio(models.Model):
    id_remedio = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False)
    descricao = models.TextField(max_length=1000)

    def __str__(self):
        return self.nome


class RemedioPaciente(models.Model):
    id_remediopaciente = models.AutoField(primary_key=True)
    remedio = models.ForeignKey(Remedio, on_delete=models.CASCADE)
    qtd_vezes_dia = models.IntegerField()
    intervelo_tempo = models.IntegerField()
    data_inicio = models.DateField(null=False)
    data_fim = models.DateField(default=timezone.now)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario
