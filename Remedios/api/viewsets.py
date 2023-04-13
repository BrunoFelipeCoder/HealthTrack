from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from Remedios.models import Remedio
from .serializers import RemedioSerializer, RemedioUsuarioSerializer


class RemedioUsuarioViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RemedioUsuarioSerializer

    def create(self, request, *args, **kwargs):
        usuario = request.user
        qtd_vezes_dia = request.POST.get('Quantidade de Vezes ao Dia')
        intervalo_tempo = request.POST.get('Intervalo de Tempo')
        data_inicio = request.POST.get('Data de Inicio')
        data_fim = request.POST.get('Data de Fim')


class RemedioViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RemedioSerializer

    def create(self, request, *args, **kwargs):
        # pega o usuário autenticado através do token
        nome = request.POST.get('Nome')
        descricao = request.POST.get('Descricao')
        remedio = Remedio.objects.create(nome=nome, descricao=descricao)
        remedio.save()

        return Response('Foi criado com sucesso')
