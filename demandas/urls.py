from django.urls import path
from . import viewsets
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('', viewsets.api_root),
    path('demanda-list/',viewsets.DemandaList.as_view(),name='demanda-list'),
    path('demanda-detail/<int:pk>/',viewsets.DemandaDetail.as_view(),name='demanda-detail'),
	path('demanda-update/<str:pk>/', viewsets.demandaUpdate, name="demanda-update"),
	path('demanda-delete/<str:pk>/', viewsets.demandaDelete, name="demanda-delete"),
])
