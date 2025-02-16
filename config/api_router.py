from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from rag_pipeline.app.views import FileViewSet
from rag_pipeline.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("files", FileViewSet)


app_name = "api"
urlpatterns = router.urls
