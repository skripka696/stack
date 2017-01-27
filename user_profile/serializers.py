from rest_framework import serializers
from user_profile.models import User


class UserSerializer(serializers.ModelSerializer):

    skill = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
        required=False)

    class Meta:
        model = User
        fields = '__all__'