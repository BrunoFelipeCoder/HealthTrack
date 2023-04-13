from rest_framework import routers
from rest_framework.routers import SimpleRouter
from .api.viewsets import RegistroViewSet

usuariospath = routers.DefaultRouter()
usuariospath.register('registro/', RegistroViewSet)
