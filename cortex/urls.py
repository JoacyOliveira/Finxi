from django.contrib import admin
from django.urls import path, include
from anuncios import urls as anuncios_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(anuncios_urls)),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]
