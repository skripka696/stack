from django.db import models
from django.contrib.auth.models import User
from tag.models import Tag


class MyUser(models.Model):
    ACTIVITY_CHOICES = (
        ('W', 'work'),
        ('S', 'study'),
    )

    user = models.OneToOneField(User)
    date_of_birth = models.DateField(blank=True, null=True)
    avatar = models.ImageField(
        blank=True,
        null=True,
        upload_to="user/avatar",
        default="user/avatar/photo.jpg"
    )
    place_of_activity = models.CharField(max_length=100)
    form = models.CharField(max_length=255, choices=ACTIVITY_CHOICES, default='S')
    rating = models.IntegerField()
    skill = models.ManyToManyField(Tag)
