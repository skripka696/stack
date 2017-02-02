from rest_framework import viewsets
from user_profile.models import User
from rest_framework import permissions
from user_profile import serializers


class UserProfile(viewsets.ModelViewSet):
    """
    Returns a list of users.
    Edit, delete and add new ones.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer(self, *args, **kwargs):
        serializers_map = {
            'list': serializers.UserSerializer,
            'create': serializers.UserPostSerializer,
            'retrieve': serializers.UserSerializer,
            'update': serializers.UserSerializer,
            'metadata': serializers.UserSerializer,
            'destroy': serializers.UserSerializer,
                    }
        serializer_class = serializers_map[self.action]
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

