from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

class InfoSaude(models.Model):
    id_infosaude = models.AutoField(primary_key=True)
    altura = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=3, null=True)
    glicemia = models.IntegerField(validators=[MaxValueValidator(500)], null=True)
    pressao_arterial = models.CharField(max_length=7, default='', null=True)
    pressao_sistolica = models.IntegerField(validators=[MaxValueValidator(200)], null=True)
    pressao_diastolica = models.IntegerField(validators=[MaxValueValidator(150)], null=True)
    nivel_oxigenio_sangue = models.IntegerField(validators=[MaxValueValidator(99)], null=True)
    temperatura = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    frequencia_cardiaca = models.IntegerField(validators=[MaxValueValidator(500)], null=True)
    frequencia_respiratoria = models.IntegerField(validators=[MaxValueValidator(99)], null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
