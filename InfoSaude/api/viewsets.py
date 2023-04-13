from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from InfoSaude.models import InfoSaude
from .serializers import InfoSaudeSerializer


class InfoSaudeViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = InfoSaudeSerializer

    def create(self, request, *args, **kwargs):
        # pega o usuário autenticado através do token
        usuario = request.user
        altura = request.POST.get('Altura')
        peso = request.POST.get('Peso')
        glicemia = request.POST.get('Glicemia')
        pressao_arterial = request.POST.get('Pressão Arterial')
        pressao_sistolica = request.POST.get('Pressão Sistólica')
        pressao_diastolica = request.POST.get('Pressão Diastólica')
        nivel_oxigenio_sangue = request.POST.get('Nível de Oxigênio no Sangue')
        temperatura = request.POST.get('Temperatura')
        frequencia_cardiaca = request.POST.get('Frequência Cardiaca')
        frequencia_respiratoria = request.POST.get('Frequência Respiratória')
        infosaude = InfoSaude.objects.create(altura=altura, peso=peso, glicemia=glicemia, pressao_arterial=pressao_arterial,
                                             pressao_diastolica=pressao_diastolica, pressao_sistolica=pressao_sistolica,
                                             nivel_oxigenio_sangue=nivel_oxigenio_sangue, temperatura=temperatura,
                                             frequencia_respiratoria=frequencia_respiratoria, frequencia_cardiaca=frequencia_cardiaca,
                                             usuario=usuario)
        infosaude.save()

        return Response('Foi criado com sucesso')

    def get_queryset(self):
        return InfoSaude.objects.filter(usuario=self.request.user)

    def patch(self, request):
        usuario = request.user
        infosaude = InfoSaude.objects.get(usuario=usuario.id)
        infosaude.altura = request.POST.get('Altura')
        infosaude.peso = request.POST.get('Peso')
        infosaude.glicemia = request.POST.get('Glicemia')
        infosaude.pressao_arterial = request.POST.get('Pressão Arterial')
        infosaude.pressao_sistolica = request.POST.get('Pressão Sistólica')
        infosaude.pressao_diastolica = request.POST.get('Pressão Diastólica')
        infosaude.nivel_oxigenio_sangue = request.POST.get('Nível de Oxigênio no Sangue')
        infosaude.temperatura = request.POST.get('Temperatura')
        infosaude.frequencia_cardiaca = request.POST.get('Frequência Cardiaca')
        infosaude.frequencia_respiratoria = request.POST.get('Frequência Respiratória')
        infosaude.save()
        return Response({'msg':'lote Atualizado!'})

