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


class UserPostSerializer(serializers.ModelSerializer):
    skill = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
        required=False)

    class Meta:
        model = User
        fields = ('username', 'password',
                  'skill', 'first_name',
                  'last_name', 'email')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
