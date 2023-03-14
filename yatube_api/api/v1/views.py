from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Comment, Follow, Group, Post

from .permissions import OwnerOrReadOnly
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.select_related("author")
    permission_classes = (OwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        queryset = Comment.objects.filter(post=post_id).select_related(
            "author"
        )
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, post_id=self.kwargs.get("post_id")
        )


class FollowViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("following__username",)
    serializer_class = FollowSerializer

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
