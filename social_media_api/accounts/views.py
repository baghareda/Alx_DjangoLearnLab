from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from .serializers import RegisterSerializer, UserSerializer, ProfileUpdateSerializer
from .models import CustomUser

User = get_user_model()


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {'token': token.key, 'user': UserSerializer(user, context={'request': request}).data},
            status=status.HTTP_201_CREATED
        )


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'detail': 'username and password required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if not user:
            return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {'token': token.key, 'user': UserSerializer(user, context={'request': request}).data},
            status=status.HTTP_200_OK
        )


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer  # for GET

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        return Response(UserSerializer(request.user, context={'request': request}).data)

    def put(self, request, *args, **kwargs):
        upd = ProfileUpdateSerializer(request.user, data=request.data)
        upd.is_valid(raise_exception=True)
        upd.save()
        return Response(UserSerializer(request.user, context={'request': request}).data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        upd = ProfileUpdateSerializer(request.user, data=request.data, partial=True)
        upd.is_valid(raise_exception=True)
        upd.save()
        return Response(UserSerializer(request.user, context={'request': request}).data, status=status.HTTP_200_OK)
    
class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.add(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)


class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": f"You unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
