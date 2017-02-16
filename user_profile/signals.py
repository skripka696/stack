from django.db.models.signals import post_save
from django.dispatch import receiver
from question.models import Question, Answer
from user_profile.models import User
from django.template.defaultfilters import slugify


@receiver(post_save, sender=Question)
@receiver(post_save, sender=Answer)
@receiver(post_save, sender=User)
def count_rating(instance, created, **kwargs):
    if created:
        if User == instance.__class__:
            instance.rating += 10
            instance.save()
        else:
            if Question == instance.__class__:
                slug = '%i-%s' % (
                    instance.pk, slugify(instance.title))
                Question.objects.filter(id=instance.id).update(slug=slug)

                instance.user.rating += 20
            elif Answer == instance.__class__:
                instance.user.rating += 10
            instance.user.save()

