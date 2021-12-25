from django.contrib import admin
from django.urls import path, include
from droids import urls as droids_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(droids_urls)),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]
