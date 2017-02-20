from django.db.models.signals import post_save
from django.dispatch import receiver
from question.models import Vote, Question, Answer


@receiver(post_save, sender=Vote)
def count_rating(instance, created, **kwargs):
    if created:
        change_model = instance.content_object.__class__
        if change_model == Question:
            get_vote(instance, change_model, 10)
        if change_model == Answer:
            get_vote(instance, change_model, 5)


def get_vote(instance, change_model, divisible):
    vote = change_model.objects.get(id=instance.object_id).vote
    if vote != 0 and vote % divisible == 0:
        instance.user.rating += 1
        instance.user.save()
