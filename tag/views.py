from rest_framework import viewsets
from tag.models import Tag
from rest_framework import permissions
from tag import serializers


class TagView(viewsets.ModelViewSet):
    """
    Returns a list of tag.
    Edit, delete and add new ones.
    """
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
