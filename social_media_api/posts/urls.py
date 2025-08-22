from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView  # 👈 make sure FeedView exists in views.py

# DRF router for posts and comments
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),  # posts/ and comments/ endpoints
    path('feed/', FeedView.as_view(), name='feed'),  # 👈 feed endpoint
]
