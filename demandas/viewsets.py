from rest_framework.response import Response
from .models import Demanda_de_peça
from .serializers import Demanda_de_peça_Serializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Cotações': reverse('demanda-list', request=request, format=format)
    })

class DemandaList(generics.ListCreateAPIView):
    serializer_class = Demanda_de_peça_Serializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(anunciante=self.request.user)

    def get_queryset(self, *args, **kwargs):
        return Demanda_de_peça.objects.all().filter(anunciante=self.request.user)

class DemandaDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = Demanda_de_peça_Serializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self, *args, **kwargs):
        return Demanda_de_peça.objects.all().filter(anunciante=self.request.user)

@api_view(['POST'])
def demandaUpdate(request, pk):
	demanda = Demanda_de_peça.objects.get(id=pk)
	serializer = Demanda_de_peça_Serializer(instance=demanda, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def demandaDelete(request, pk):
	demanda = Demanda_de_peça.objects.get(id=pk)
	demanda.delete()

	return Response('Demanda foi deletada com sucesso!')

