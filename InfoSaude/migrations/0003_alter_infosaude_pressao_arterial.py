# Generated by Django 4.2 on 2023-04-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoSaude', '0002_alter_infosaude_frequencia_cardiaca_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infosaude',
            name='pressao_arterial',
            field=models.CharField(default='', max_length=7),
        ),
    ]
