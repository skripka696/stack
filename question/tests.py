from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from user_profile.models import User
from question.models import Question
from django.contrib.contenttypes.models import ContentType


class BaseAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username="User",
                                       email="user@user.com")
        self.question = Question.objects.create(id=1, user_id=1, title='test',
                                                content='test')
        self.question_content_type = ContentType.objects.get_for_model(
            Question).id


class QuestionAPITestCase(BaseAPITestCase):
    
    def setUp(self):
        super(QuestionAPITestCase, self).setUp()
        self.questions_url = '/api/question/'

    def test_get_list_of_questions(self):
        response = self.client.get(self.questions_url)
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_create_question_by_not_authenticated(self):
        data = {
            'tag': 1,
            'title': 'test title',
            'content': 'test content',
        }
        response = self.client.post(self.questions_url, data, format='json')
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_question(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'tag': 1,
            'title': 'test title',
            'content': 'test content',
        }
        response = self.client.post(self.questions_url, data, format='json')
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


class AnswerAPITestCase(BaseAPITestCase):
    def setUp(self):
        super(AnswerAPITestCase, self).setUp()
        self.answer_url = '/api/answer/'

    def test_create_answer(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'test title',
            'content': 'test content',
            'question': self.question.id
        }
        response = self.client.post(self.answer_url, data, format='json')
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


class CommentAPITestCase(BaseAPITestCase):

    def setUp(self):
        super(CommentAPITestCase, self).setUp()
        self.comment_url = '/api/comment/'

    def test_create_comment(self):
        self.client.force_authenticate(user=self.user)

        data = {
            'description': 'test description',
            'content_type': self.question_content_type,
            'object_id': self.question.id
        }
        response = self.client.post(self.comment_url, data, format='json')
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)