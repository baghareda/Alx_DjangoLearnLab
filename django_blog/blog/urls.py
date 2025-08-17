from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("", views.home, name="home"),

    # Auth (built-in views)
    path("login/",  auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logout.html"), name="logout"),

    # Custom
    path("register/", views.register, name="register"),
    path("profile/",  views.profile,  name="profile"),

    # Blog posts
    path("posts/", PostListView.as_view(), name="post-list"),          # /posts/
    path("posts/new/", PostCreateView.as_view(), name="post-create"),  # /posts/new/
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),        # /posts/1/
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"),   # /posts/1/edit/
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"), # /posts/1/delete/
]
