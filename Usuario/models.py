from django.db import models
from django.contrib.auth.models import User

class Nome(models.Model):
    id_nome = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150, null=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

class CPF(models.Model):
    id_cpf = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=14, null=False, unique=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

class RG(models.Model):
    id_rg = models.AutoField(primary_key=True)
    rg = models.CharField(max_length=15, null=False, unique=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

class DataNascimento(models.Model):
    id_datanascimento = models.AutoField(primary_key=True)
    datanascimento = models.DateField(null=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

class Telefone(models.Model):
    id_telefone = models.AutoField(primary_key=True)
    num_telefone = models.CharField(max_length=17, unique=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
