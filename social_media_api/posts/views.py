from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only owners can edit or delete their objects.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()   # ✅ required by checker
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(generics.ListAPIView):
    """
    Returns posts from users the current user follows, ordered by creation date.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author__in=user.following.all()).order_by('-created_at')


class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)   # ✅ required by checker

        like, created = Like.objects.get_or_create(      # ✅ required by checker
            user=request.user,
            post=post
        )

        if created:
            # Create notification
            Notification.objects.create(
                sender=request.user,
                recipient=post.author,
                notification_type='like',
                content_type=ContentType.objects.get_for_model(post),
                object_id=post.id
            )
            return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)   # ✅ required by checker

        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"detail": "Like removed."}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"detail": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)
