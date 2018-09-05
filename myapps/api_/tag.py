from rest_framework import serializers, viewsets

from art.models import Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Tag
        fields = ('id', 'name', 'describe', 'add_time')


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer