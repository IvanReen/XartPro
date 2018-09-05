from rest_framework import routers

from api_.tag import TagViewSet
from api_.art import ArtViewSet

api_router = routers.DefaultRouter()

# 注册api资源
api_router.register('tag', TagViewSet)
api_router.register('art', ArtViewSet)