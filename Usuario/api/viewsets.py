from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import RegistroSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from Usuario.models import Nome, CPF, RG, DataNascimento, Telefone


class RegistroViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistroSerializer

    def create(self, request, *args, **kwargs):
        nome = request.POST.get('Nome')
        print(nome)
        username = request.POST.get('Username')
        print(username)
        password = request.POST.get('Senha')
        hashed_password = make_password(password)
        print(password)
        email = request.POST.get('Email')
        print(email)
        cpf = request.POST.get('CPF')
        print(cpf)
        rg = request.POST.get('RG')
        print(rg)
        datanascimento = request.POST.get('Data de Nascimento')
        print(datanascimento)
        telefone = request.POST.get('Telefone')
        print(telefone)
        if nome and username and password and email and cpf and rg and datanascimento and telefone:
            usuario = User.objects.create(username=username, password=hashed_password, email=email)
            usuario.save()
            nomesalvar = Nome.objects.create(nome=nome, usuario=usuario)
            nomesalvar.save()
            cpfsalvar = CPF.objects.create(cpf=cpf, usuario=usuario)
            cpfsalvar.save()
            rgsalvar = RG.objects.create(rg=rg, usuario=usuario)
            rgsalvar.save()
            datanascimentosalvar = DataNascimento.objects.create(datanascimento=datanascimento, usuario=usuario)
            datanascimentosalvar.save()
            telefonesalvar = Telefone.objects.create(num_telefone=telefone, usuario=usuario)
            telefonesalvar.save()
            return Response({'msg':f'{usuario} foi cadastrado com sucesso!'})
        return Response({'msg':f'Não foi possivel realizar o cadastrado!'})


    def patch(self, request):
        usuario = request.user
        usuario.email = request.POST.get('Email')
        usuario.username = request.POST.get('Username')
        usuario.save()
        nomeatualizar = Nome.objects.get(usuario=usuario.id)
        nome = request.POST.get('Nome')
        nomeatualizar.save(nome=nome)
        cpfatualizar = CPF.objects.get(usuario=usuario.id)
        cpf = request.POST.get('CPF')
        cpfatualizar.save(cpf=cpf)
        rgatualizar = RG.objects.get(usuario=usuario.id)
        rg = request.POST.get('RG')
        rgatualizar.save(rg=rg)
        datanascimentoatualizar = DataNascimento.objects.get(usuario=usuario.id)
        datanascimento = request.POST.get('Data de Nascimento')
        datanascimentoatualizar.save(datanascimento=datanascimento)
        telefoneatualizar = Telefone.objects.get(usuario=usuario.id)
        telefone = request.POST.get('Telefone')
        telefoneatualizar.save(num_telefone=telefone)
        return Response({'Usuario Atualizado!'})

