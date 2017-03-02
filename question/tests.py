from django.test import TestCase
from datetime import datetime
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from user_profile.models import User
from question.models import Question, Answer, Vote
from django.contrib.contenttypes.models import ContentType
import pytz


class BaseAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username="Usera",
                                       email="user@user.com")
        self.user_for_vote = User.objects.create(username="Userq2",
                                                 email="user2@user.com",
                                                 rating=60)
        self.question = Question.objects.create(id=1, user_id=1, title='test',
                                                content='test')
        self.question_content_type = ContentType.objects.get_for_model(
            Question).id
        self.answer_content_type = ContentType.objects.get_for_model(
            Answer).id


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

    def test_create_answer_by_not_authenticated(self):
        data = {
            'title': 'test title',
            'content': 'test content',
            'question': self.question.id
        }
        response = self.client.post(self.answer_url, data, format='json')
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

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

    def test_create_answer_with_nonexistent_question(self):
        self.client.force_authenticate(user=self.user)

        data = {
            'title': 'test title',
            'content': 'test content',
            'question': 245
        }
        response = self.client.post(self.answer_url, data, format='json')
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)


class CommentAPITestCase(BaseAPITestCase):

    def setUp(self):
        super(CommentAPITestCase, self).setUp()
        self.comment_url = '/api/comment/'

    def test_create_comment_by_not_authenticated(self):
        data = {
            'description': 'test description',
            'content_type': self.question_content_type,
            'object_id': self.question.id
        }
        response = self.client.post(self.comment_url, data, format='json')
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

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

    def test_create_comment_with_nonexistent_question(self):
        self.client.force_authenticate(user=self.user)

        data = {
            'description': 'test description',
            'content_type': self.question_content_type,
            'object_id': 457
        }
        response = self.client.post(self.comment_url, data, format='json')
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_comment_with_nonexistent_answer(self):
        self.client.force_authenticate(user=self.user)

        data = {
            'description': 'test description',
            'content_type': self.answer_content_type,
            'object_id': 457
        }
        response = self.client.post(self.comment_url, data, format='json')
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)


class VoteAPITestCase(BaseAPITestCase):

    def setUp(self):
        super(VoteAPITestCase, self).setUp()
        self.vote_url = '/api/vote/'
        self.vote_url_for_retrieve = '/api/vote/1/'
        self.question_after_month = Question.objects.create(id=2, user_id=1, title='test',
                                                            content='test',
                                                            create_date=datetime(2017, 1, 1))
        self.vote_content_type = ContentType.objects.get_for_model(Vote)
        self.question_content_type = ContentType.objects.get_for_model(
            Question).model

        self.vote = Vote.objects.create(id=1, user_id=1, choice='U',
                                        rating=1,
                                        content_type=self.vote_content_type, object_id=2)

        Vote.objects.filter(pk=self.vote.id).update(
            updated_at=datetime(2017, 1, 1, 2, 15).replace(tzinfo=pytz.utc)
        )
        self.vote.refresh_from_db()

    def test_create_vote_by_not_authenticated(self):
        data = {
            'choice': 'U',
            'rating': 1,
            'content_type': self.question_content_type,
            'object_id': self.question.id
        }
        response = self.client.post(self.vote_url, data, format='json')
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_vote(self):
        self.client.force_authenticate(user=self.user_for_vote)

        data = {

            'choice': 'U',
            'rating': 1,
            'content_type': self.question_content_type,
            'object_id': self.question.id
        }
        response = self.client.post(self.vote_url, data, format='json')
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_create_vote_with_small_users_rating(self):
        self.client.force_authenticate(user=self.user)

        data = {

            'choice': 'U',
            'rating': 1,
            'content_type': self.question_content_type,
            'object_id': self.question.id
        }
        response = self.client.post(self.vote_url, data, format='json')
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_vote_after_one_month(self):
        self.client.force_authenticate(user=self.user)

        data = {

            'choice': 'U',
            'rating': 1,
            'content_type': self.question_content_type,
            'object_id': self.question_after_month.id
        }
        response = self.client.post(self.vote_url, data, format='json')
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_vote_after_three_hours(self):
        self.client.force_authenticate(user=self.user)

        data = {
            'choice': 'D',
            'rating': 1,
            'content_type': self.question_content_type,
            'object_id': self.question_after_month.id
        }
        response = self.client.patch(self.vote_url_for_retrieve, data, format='json')
        print(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)