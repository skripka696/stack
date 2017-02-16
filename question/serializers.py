from rest_framework import serializers
from question.models import Question, Answer, Comment, Vote
from django.conf import settings
from tag.models import Tag
from user_profile.models import User
from django.contrib.auth import get_user_model


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
        required=False)

    question = serializers.SlugRelatedField(
         read_only=True,
         slug_field="title",
         required=False
    )

    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
         read_only=True,
         slug_field="username",
         required=False)

    tag = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
        required=False)
    answers = AnswerSerializer(required=False, many=True)

    class Meta:
        model = Question
        fields = ('id', 'user', 'tag', 'create_date', 'title', 'content', 'vote', 'answers', 'slug')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }




class QuestionPostSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username")

    tag = serializers.SlugRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        slug_field='name')

    class Meta:
        model = Question
        fields = ('user', 'tag', 'title', 'content')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
        required=False)

    content_object = serializers.SlugRelatedField(
        read_only=True,
        slug_field="title",
        required=False
    )

    class Meta:
        model = Comment
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):



    class Meta:
        model = Vote
        fields = '__all__'