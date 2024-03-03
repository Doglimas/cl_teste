from django.contrib import admin
from django.urls import path,include
from aplicacao.views import PostagensViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Postagens', PostagensViewSet, basename='Postagens')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) )
]
