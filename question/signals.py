from django.db.models.signals import post_save
from django.dispatch import receiver
from question.models import Vote


@receiver(post_save, sender=Vote)
def count_vote(instance, created, **kwargs):
    change_model = instance.content_object
    new_rating = instance.rating
    rating_type = instance.choice
    if rating_type == 'U':
        change_model.vote += new_rating
    elif rating_type == 'D':
        change_model.vote -= new_rating
    change_model.save()
