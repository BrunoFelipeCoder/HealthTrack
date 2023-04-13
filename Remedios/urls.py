from rest_framework import routers
from .api.viewsets import RemedioViewSet

remediospath = routers.DefaultRouter()
remediospath.register('registro', RemedioViewSet, basename='registro')
