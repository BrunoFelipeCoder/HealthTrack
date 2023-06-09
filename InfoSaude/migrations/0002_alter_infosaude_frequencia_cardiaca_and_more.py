# Generated by Django 4.2 on 2023-04-11 21:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoSaude', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infosaude',
            name='frequencia_cardiaca',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(500)]),
        ),
        migrations.AlterField(
            model_name='infosaude',
            name='frequencia_respiratoria',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='infosaude',
            name='nivel_oxigenio_sangue',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='infosaude',
            name='pressao_diastolica',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(150)]),
        ),
        migrations.AlterField(
            model_name='infosaude',
            name='pressao_sistolica',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(200)]),
        ),
    ]
