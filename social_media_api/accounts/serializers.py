from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token

User = get_user_model()


# -----------------------------
# User Serializer (Read Only)
# -----------------------------
class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'bio', 'profile_picture',
            'followers_count', 'following_count'
        ]
        read_only_fields = [
            'id', 'username', 'email', 'followers_count',
            'following_count', 'profile_picture'
        ]

    def get_followers_count(self, obj):
        return obj.followers.count() if hasattr(obj, "followers") else 0

    def get_following_count(self, obj):
        return obj.following.count() if hasattr(obj, "following") else 0


# -----------------------------
# Register Serializer
# -----------------------------
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def validate_email(self, value):
        """Ensure email is unique."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already taken.")
        return value

    def create(self, validated_data):
        # Create user securely
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        # Generate auth token
        Token.objects.get_or_create(user=user)
        return user


# -----------------------------
# Login Serializer
# -----------------------------
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError("Both username and password are required.")

        token, _ = Token.objects.get_or_create(user=user)
        data["user"] = user
        data["token"] = token.key
        return data


# -----------------------------
# Profile Update Serializer
# -----------------------------
class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['bio', 'profile_picture']
        extra_kwargs = {
            'bio': {'required': False},
            'profile_picture': {'required': False},
        }
