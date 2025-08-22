from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import UserSerializer


class UserListView(generics.GenericAPIView):
    """
    List all users
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)


class FollowUserView(generics.GenericAPIView):
    """
    Authenticated user follows another user
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        user_to_follow = get_object_or_404(CustomUser, pk=pk)
        request.user.following.add(user_to_follow)
        return Response(
            {"detail": f"You are now following {user_to_follow.username}"},
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):
    """
    Authenticated user unfollows another user
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        user_to_unfollow = get_object_or_404(CustomUser, pk=pk)
        request.user.following.remove(user_to_unfollow)
        return Response(
            {"detail": f"You have unfollowed {user_to_unfollow.username}"},
            status=status.HTTP_200_OK
        )
