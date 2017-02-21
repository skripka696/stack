from rest_framework import serializers
from question.models import Question, Answer, Comment, Vote
from django.conf import settings
from tag.models import Tag
from user_profile.models import User
from django.utils import timezone


class CommentRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        serializer = CommentSerializer(value.get_queryset()[0])
        return serializer.data


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
    comment = CommentRelatedField(read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'user', 'tag', 'create_date', 'title', 'content',
                  'vote', 'answers', 'comment', 'slug')
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


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ('id', 'choice', 'rating', 'object_id', 'user', 'content_type', 'updated_at')

    def validate(self, attrs):
        if self._context['view'].action == 'create':
            self.check_user_rating(attrs)
            change_model = attrs['content_type'].model_class()
            if change_model == Question:
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

    def check_user_rating(self, data):
        if data['user'].rating < 50:
            raise serializers.ValidationError(
                'For this action, the rating should be greater than 50 ')

    def save(self, **kwargs):
        if self.context['request'].data.get('type') == 'N':
            self.validated_data['choice'] = 'N'
        super(VoteSerializer, self).save(**kwargs)
