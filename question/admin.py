from django.contrib import admin
from question.models import Question
from question.models import Answer
from question.models import Comment
from question.models import Void


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Void)
