from rest_framework.serializers import ModelSerializer
from Usuario.models import Nome, CPF, RG, DataNascimento
from django.contrib.auth.models import User


class NomeSerializer(ModelSerializer):
    class Meta:
        model = Nome
        fields = ['nome']


class CPFSerializer(ModelSerializer):
    class Meta:
        model = CPF
        fields = ['cpf']


class RGSerializer(ModelSerializer):
    class Meta:
        model = RG
        fields = ['rg']


class DataNascimentoSerializer(ModelSerializer):
    class Meta:
        model = DataNascimento
        fields = ['datanascimento']


class RegistroSerializer(ModelSerializer):

    nome = NomeSerializer()
    cpf = CPFSerializer()
    rg = RGSerializer()
    datanascimento = DataNascimentoSerializer()

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'nome', 'cpf', 'rg', 'datanascimento']


class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class LogoutSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = []

