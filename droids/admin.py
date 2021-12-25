from django.contrib import admin
from .models import Demanda_de_peça

# Register your models here.

@admin.register(Demanda_de_peça)
class Demanda_de_peçaaAdmin(admin.ModelAdmin):
    list_display = ('id','status','anunciante','descrição','rua','cidade','estado','cep','telefone')
    search_fields = ('anunciante__username','id')