from django.db.models.signals import post_save
from django.dispatch import receiver
from question.models import Vote
from question.models import Answer
from question.models import Question


@receiver(post_save, sender=Vote)
def count_vote(instance, **kwargs):
    change_model = instance.content_object.__class__



    # Vote.objects.filter(id=Vote.object_id).update(count_field=F('count_field') + some_val)
    # rate = instance.question
    # rate.rate += 1
    # rate.save()
    print('sdfsf************')