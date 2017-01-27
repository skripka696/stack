from django.db import models
from django.contrib.auth.models import AbstractUser
from tag.models import Tag


class User(AbstractUser):
    ACTIVITY_CHOICES = (
        ('W', 'work'),
        ('S', 'study'),
    )

    date_of_birth = models.DateField(blank=True, null=True)
    avatar = models.ImageField(
        blank=True,
        null=True,
        upload_to="user/avatar",
        default="user/avatar/photo.jpg"
    )
    place_of_activity = models.CharField(max_length=100)
    form = models.CharField(max_length=255, choices=ACTIVITY_CHOICES, default='S')
    rating = models.IntegerField(default=0)
    skill = models.ManyToManyField(Tag)

    def __str__(self):
        return '{}, {}'.format(self.username, self.date_of_birth)
