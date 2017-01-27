from user_profile.views import UserProfile
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserProfile)
urlpatterns = router.urls
