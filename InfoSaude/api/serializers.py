from rest_framework.serializers import ModelSerializer
from InfoSaude.models import InfoSaude


class InfoSaudeSerializer(ModelSerializer):
    class Meta:
        model = InfoSaude
        fields = ['altura', 'peso', 'glicemia', 'pressao_arterial', 'pressao_sistolica', 'pressao_diastolica', 'nivel_oxigenio_sangue', 'temperatura', 'frequencia_cardiaca', 'frequencia_respiratoria', 'usuario']