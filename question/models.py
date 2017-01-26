from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from tag.models import Tag
from user_profile.models import MyUser


class Question(models.Model):
    user = models.ForeignKey(MyUser)
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        print('{}, {}'.format(self.user, self.title))


class Answer(models.Model):
    user = models.ForeignKey(MyUser)
    question = models.ForeignKey(Question)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        print('{}, {}'.format(self.user, self.title))

class Comment(models.Model):
    user = models.ForeignKey(MyUser)
    like = models.IntegerField()
    description = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        print('{}'.format(self.user))


class Void(models.Model):
    rating = models.IntegerField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        print('{}'.format(self.rating))

