from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.exceptions import APIException

from question.models import Question, Answer, Comment, Vote
from question import serializers
from django.contrib.contenttypes.models import ContentType
from user_profile.permissions import IsHaveAccess
from rest_framework.permissions import IsAuthenticated


class MixedPermission(object):
    permission_action_map = {}

    def get_permissions(self):
        try:
            return [permission() for permission in
                    self.permission_action_map[self.action]]

        except KeyError:
            return [permission() for permission in self.permission_classes]


class MixedPermissionAction(MixedPermission):
    permission_action_map = {'create': [IsAuthenticated, IsHaveAccess],
                             'update': [IsHaveAccess]}


class QuestonView(MixedPermissionAction, viewsets.ModelViewSet ):
    """
    Returns a list of questions.
    Edit, delete and add new ones.
    """
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    lookup_field = 'slug'

    def get_serializer(self, *args, **kwargs):
        serializers_map = {
            'create': serializers.QuestionPostSerializer,
                            }
        serializer_class = serializers_map.get(self.action,
                                               self.serializer_class)
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class AnswerView(MixedPermissionAction, viewsets.ModelViewSet):
    """
    Returns a list of answers.
    Edit, delete and add new ones.
    """
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer


class CommentView(MixedPermissionAction, viewsets.ModelViewSet):
    """
    Returns a list of comments.
    Edit, delete and add new ones.
    """
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class VoteView(MixedPermissionAction, viewsets.ModelViewSet):
    """
    Returns a list of views.
    """
    queryset = Vote.objects.all()
    serializer_class = serializers.VoteSerializer

    def update(self, request, *args, **kwargs):
        self.check_of_correct_vote(request)
        return super(VoteView, self).update(request, *args, **kwargs)

    def check_of_correct_vote(self, request):
        change_model = ContentType.objects.get(id=request.data['content_type'])
        vote = Vote.objects.get(user=request.data['user'])
        change_model_vote = change_model.model_class().objects.get(
            id=request.data['object_id']).vote
        if request.data['choice'] == vote.choice:
            raise APIException('You can only change your vote', 400)
        if self.change_up(request, vote):
            change_model_vote += 1
            request.data['type'] = 'N'
        elif self.change_down(request, vote):
            change_model_vote -= 1
            request.data['type'] = 'N'
        elif vote.choice == 'N':
            if self.set_up(request):
                change_model_vote += 1
            elif self.set_down(request):
                change_model_vote -= 1
        change_model.save()

    def change_up(self, request, vote):
        return vote.choice == 'D' and request.data['choice'] == 'U'

    def change_down(self, request, vote):
        return vote.choice == 'U' and request.data['choice'] == 'D'

    def set_up(self, request):
        return request.data['choice'] == 'U'

    def set_down(self, request):
        return request.data['choice'] == 'D'



