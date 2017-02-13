from rest_framework import viewsets
from question.models import Question, Answer, Comment, Vote
from rest_framework import permissions
from question import serializers
from rest_framework.response import Response
from rest_framework import status
from django.contrib.contenttypes.models import ContentType
from datetime import datetime, timezone


class QuestonView(viewsets.ModelViewSet):
    """
    Returns a list of questions.
    Edit, delete and add new ones.
    """
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer

    def get_serializer(self, *args, **kwargs):
        serializers_map = {
            'create': serializers.QuestionPostSerializer,
                            }
        serializer_class = serializers_map.get(self.action,
                                               self.serializer_class)
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class AnswerView(viewsets.ModelViewSet):
    """
    Returns a list of answers.
    Edit, delete and add new ones.
    """
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer


class CommentView(viewsets.ModelViewSet):
    """
    Returns a list of comments.
    Edit, delete and add new ones.
    """
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class VoteView(viewsets.ModelViewSet):
    """
    Returns a list of views.
    """
    queryset = Vote.objects.all()
    serializer_class = serializers.VoteSerializer

    def create(self, request, *args, **kwargs):
        self.check_expired_for_voting(request, 730, 'EXPIRED FOR VOTING')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        self.check_expired_for_voting(request, 3, 'EXPIRED FOR UPDATE VOTING')
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

    def check_expired_for_voting(self, request, hour_expire, message):
        change_model = ContentType.objects.get(id=request.data['content_type'])
        data = change_model.model_class().objects.get(id=request.data['object_id']).create_date
        diff_date = datetime.now(timezone.utc) - data
        if diff_date.seconds > hour_expire*3600:
            return Response({'error': '{}'.format(message)}, status=status.HTTP_400_BAD_REQUEST)

    def check_of_correct_vote(self, request):
        vote = Vote.objects.get(user=request.data['user'])
        if request.data['choice'] == vote.choice:
            return Response({'error': 'You can only change your vote'}, status=status.HTTP_400_BAD_REQUEST)
        # if vote.choice == 'U' and request.data['choice'] == 'D' \
        #         or vote.choice == 'D' and request.data['choice'] == 'U':
        #     request.data['zeroing'] = True


