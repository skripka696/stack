from question.views import QuestonView, AnswerView, CommentView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'question', QuestonView)
router.register(r'answer', AnswerView)
router.register(r'comment', CommentView)

urlpatterns = router.urls
