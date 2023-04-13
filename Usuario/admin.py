from django.contrib import admin
from .models import Nome, CPF, RG, DataNascimento, Telefone

admin.site.register(Nome)
admin.site.register(CPF)
admin.site.register(RG)
admin.site.register(DataNascimento)
admin.site.register(Telefone)


