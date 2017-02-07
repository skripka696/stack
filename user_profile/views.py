from rest_framework import viewsets
from user_profile.models import User
from user_profile import serializers


class UserProfile(viewsets.ModelViewSet):
    """
    Returns a list of users.
    Edit, delete and add new ones.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_serializer(self, *args, **kwargs):
        serializers_map = {
            'create': serializers.UserPostSerializer,
                            }
        serializer_class = serializers_map.get(self.action,
                                               self.serializer_class)
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

