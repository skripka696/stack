from rest_framework import serializers
from question.models import Question, Answer, Comment, Vote
from django.conf import settings
from tag.models import Tag
from user_profile.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone

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


class QuestionPostSerializer(QuestionSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username")

    tag = serializers.SlugRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        slug_field='name')

    class Meta:
        model = Question
        fields = ('id', 'user', 'tag', 'title', 'content')


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
        fields = ('id', 'choice', 'rating', 'object_id', 'user', 'content_type', 'updated_at')

    def validate(self, attrs):
        if self._context['view'].action == 'create':
            change_model = attrs['content_type'].model_class()
            data = change_model.objects.get(
                id=attrs['object_id']).create_date
            diff_date = timezone.now() - data
            if diff_date.seconds > settings.ANSWER_TIMEOUT*3600:
                raise serializers.ValidationError(
                    'EXPIRED FOR VOTING')
        if self._context['view'].action == 'update':
            # diff_date = timezone.now() - attrs['updated_at']
            # if diff_date.seconds > settings.ANSWER_UPDATE:
            if 20*60 > settings.ANSWER_UPDATE*3600:
                raise serializers.ValidationError(
                    'EXPIRED FOR UPDATE VOTING')
        return attrs

    def save(self, **kwargs):
        if self.context['request'].data.get('type') == 'N':
            self.validated_data['choice'] = 'N'
        super(VoteSerializer, self).save(**kwargs)
