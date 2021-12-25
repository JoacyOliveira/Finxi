from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from droids.models import Demanda_de_peça


class Demanda_de_peça_Serializer(ModelSerializer):
    anunciante = serializers.ReadOnlyField(source='anunciante.username')
    class Meta:
        model = Demanda_de_peça
        fields = ['id','anunciante','descrição','rua','cidade','estado','cep','telefone','status']

