from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from demandas import urls as demandas_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(demandas_urls)),
]

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')
]
