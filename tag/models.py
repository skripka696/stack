from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)