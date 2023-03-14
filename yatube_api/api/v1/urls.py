from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = "api"

router = DefaultRouter()
router.register(
    r"posts",
    PostViewSet,
)
router.register(
    r"groups",
    GroupViewSet,
)
router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)
router.register(r"follow", FollowViewSet, basename="following")

urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
]
