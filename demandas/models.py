from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from model_utils import Choices

#Modelos

class Demanda_de_peça(models.Model):
    descrição = models.TextField()
    rua = models.TextField()
    cidade = models.TextField()
    estado = models.TextField()
    cep = models.IntegerField()
    telefone = PhoneNumberField()
    anunciante = models.ForeignKey('auth.user', related_name='demandas', on_delete=models.CASCADE)
    STATUS = Choices('Aberta', 'Finalizada')
    status = models.CharField(choices=STATUS, default=STATUS.Aberta, max_length=20)


    def __str__(self):
        return str(self.id)


