from rest_framework import viewsets
from question.models import Question, Answer, Comment
from rest_framework import permissions
from question import serializers


class QuestonView(viewsets.ModelViewSet):
    """
    Returns a list of questions.
    Edit, delete and add new ones.
    """
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AnswerView(viewsets.ModelViewSet):
    """
    Returns a list of answers.
    Edit, delete and add new ones.
    """
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentView(viewsets.ModelViewSet):
    """
    Returns a list of comments.
    Edit, delete and add new ones.
    """
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

