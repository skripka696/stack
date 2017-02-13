from rest_framework import viewsets
from question.models import Question, Answer, Comment, Vote
from rest_framework import permissions
from question import serializers
from rest_framework.response import Response
from rest_framework import status
from django.contrib.contenttypes.models import ContentType
import datetime


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


class VoteView(viewsets.ModelViewSet):
    """
    Returns a list of views.
    """
    queryset = Vote.objects.all()
    serializer_class = serializers.VoteSerializer

    def create(self, request, *args, **kwargs):
        change_model = ContentType.objects.get(id=request.data['content_type'])
        data = change_model.model_class().objects.get(id=request.data['object_id']).create_date
        diff_date = datetime.datetime.now() - data
        if diff_date.days > 30:
            return Response({'error': 'EXPIRED FOR VOTING'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        change_model = ContentType.objects.get(id=request.data['content_type'])
        data = change_model.model_class().objects.get(id=request.data['object_id']).create_date
        diff_date = datetime.datetime.now() - data
        if diff_date.hour > 3:
            return Response({'error': 'EXPIRED FOR UPDATE VOTING'}, status=status.HTTP_400_BAD_REQUEST)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # refresh the instance from the database.
            instance = self.get_object()
            serializer = self.get_serializer(instance)

        return Response(serializer.data)


