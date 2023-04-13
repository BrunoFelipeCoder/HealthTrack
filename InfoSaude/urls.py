from rest_framework import routers
from .api.viewsets import InfoSaudeViewSet

infosaudepath = routers.DefaultRouter()
infosaudepath.register('registro', InfoSaudeViewSet, basename='registro')
