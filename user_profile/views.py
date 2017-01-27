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
