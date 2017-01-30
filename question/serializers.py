from rest_framework import serializers
from question.models import Question, Answer, Comment


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

    class Meta:
        model = Question
        fields = '__all__'


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