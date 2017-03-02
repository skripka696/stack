from rest_framework import serializers
from question.models import Question, Answer, Comment, Vote
from django.conf import settings
from generic_relations.relations import GenericRelatedField
from django.contrib.contenttypes.models import ContentType


from django.utils import timezone

from user_profile.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True,
                          default=serializers.CurrentUserDefault())

    def validate(self, attrs):
        change_model = attrs['content_type'].model_class()
        if not change_model.objects.filter(id=attrs['object_id']).exists():
            raise serializers.ValidationError('Object does not exist')
        return attrs

    class Meta:
        model = Comment
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True,
                          default=serializers.CurrentUserDefault())

    # comment = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Answer
        fields = ('user', 'question', 'create_date', 'title', 'content', 'vote')


class QuestionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True,
                          default=serializers.CurrentUserDefault())

    tag = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
        required=False)
    answers = AnswerSerializer(required=False, many=True, read_only=True)
    comment = CommentSerializer(many=True, read_only=True)
    
    # def to_internal_value(self, data):
    #     return super(QuestionSerializer, self).is_valid(self, {'id': data})

    class Meta:
        model = Question
        fields = ('id', 'tag', 'user', 'create_date', 'title', 'content',
                  'vote', 'answers', 'slug', 'comment')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class QuestionPostSerializer(QuestionSerializer):
    user = UserSerializer(read_only=True,
                          default=serializers.CurrentUserDefault())

    class Meta:
        model = Question
        fields = ('id', 'user', 'tag', 'title', 'content')


class VoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True,
                          default=serializers.CurrentUserDefault())
    content_type = serializers.SlugRelatedField(queryset=ContentType.objects.all(),
                                                slug_field='model')

    class Meta:
        model = Vote
        fields = ('id', 'choice', 'rating', 'object_id', 'user', 'content_type', 'updated_at')

    def validate(self, attrs):
        content_type = ContentType.objects.get(model=attrs['content_type'])
        attrs['content_type'] = content_type
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
