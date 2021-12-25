from django.urls import path
from droids import viewsets
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('', viewsets.api_root),
    path('demanda/',
         viewsets.DemandaList.as_view(),
         name='demanda-list'),
    path('demanda/<int:pk>/',
         viewsets.DemandaDetail.as_view(),
         name='demanda-detail'),

])
