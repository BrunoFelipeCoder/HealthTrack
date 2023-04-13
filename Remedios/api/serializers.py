from rest_framework.serializers import ModelSerializer
from Remedios.models import Remedio, RemedioPaciente


class RemedioSerializer(ModelSerializer):
    class Meta:
        model = Remedio
        fields = ['nome', 'descricao']


class RemedioUsuarioSerializer(ModelSerializer):
    class Meta:
        model = RemedioSerializer
        fields = ['remedio', 'qtd_vezes_dia', 'intervalo_tempo', 'data_inicio', 'data_fim', 'usuario']