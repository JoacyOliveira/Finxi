from rest_framework.response import Response
from anuncios.models import Demanda_de_peça
from anuncios.serializers import Demanda_de_peça_Serializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Demandas': reverse('demanda-list', request=request, format=format)
    })

class DemandaList(generics.ListCreateAPIView):
    serializer_class = Demanda_de_peça_Serializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(anunciante=self.request.user)

    def get_queryset(self, *args, **kwargs):
        return Demanda_de_peça.objects.all().filter(anunciante=self.request.user)


class DemandaDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Demanda_de_peça.objects.all()
    serializer_class = Demanda_de_peça_Serializer
    permission_classes = [IsAuthenticated,]