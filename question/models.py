from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from tag.models import Tag
from django.conf import settings


class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    tag = models.ManyToManyField(Tag)
    create_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    vote = models.IntegerField(default=0)

    def __str__(self):
        return '{}, {}'.format(self.user, self.title)


class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.ForeignKey(Question)
    create_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    vote = models.IntegerField(default=0)

    def __str__(self):
        return '{}, {}'.format(self.user, self.title)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    like = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return '{}'.format(self.user)


class Vote(models.Model):
    ACTIVITY_CHOICES = (
        ('U', 'up'),
        ('D', 'down'),
        ('N', 'null'),
    )
    choice = models.CharField(max_length=5, choices=ACTIVITY_CHOICES, default='N')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    rating = models.IntegerField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return 'rating - {}, user - {}, choice - {}'.format(self.rating, self.user, self.choice)


