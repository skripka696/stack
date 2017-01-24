from django.db import models
from django.contrib.auth.models import User
from tag.models import Tag


class MyUser(models.Model):
    user = models.OneToOneField(User)
    firstname = models.CharField(blank=True, null=True)
    lastname = models.CharField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True, upload_to="user/avatar", default="user/avatar/photo.jpg")
    ACTIVITY_CHOICES = (
        ('W', 'work'),
        ('S', 'study'),
    )
    place_of_activity = models.CharField()
    form = models.CharField(max_length=255, choices=ACTIVITY_CHOICES, default='S')
    rating = models.IntegerField()
    skill = models.ManyToManyField(Tag)
