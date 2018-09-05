from rest_framework import serializers, viewsets

from art.models import Art
from api_.tag import TagSerializer


class ArtSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Art
        fields = ('id', 'title', 'author', 'tags')


class ArtViewSet(viewsets.ModelViewSet):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer