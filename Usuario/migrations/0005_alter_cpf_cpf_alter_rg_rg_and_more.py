# Generated by Django 4.2 on 2023-04-12 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0004_alter_cpf_cpf_alter_rg_rg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpf',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='rg',
            name='rg',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='num_telefone',
            field=models.CharField(max_length=17, unique=True),
        ),
    ]
