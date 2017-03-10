from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from user_profile.models import User


class UserSerializer(serializers.ModelSerializer):

    # questions = QuestionSerializer(many=True, required=False)
    # answers = AnswerSerializer(many=True, required=False)

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

    email = serializers.EmailField(validators=
                                   [UniqueValidator(queryset=User.objects.all(),
                                                    message='A user with that email already exists')])

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

    def validate_password(self, value):
        if not value:
            raise serializers.ValidationError("Password cannot be empty!")
        elif len(value) < 8:
            raise serializers.ValidationError("Password should be > 8")
        return value
