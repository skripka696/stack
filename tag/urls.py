from tag.views import TagView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tag', TagView)
urlpatterns = router.urls
