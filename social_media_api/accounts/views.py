from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import RegisterSerializer, UserSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

User = get_user_model()


# ✅ Register new users
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()  # ✅ contains "CustomUser.objects.all()"
    serializer_class = RegisterSerializer


# ✅ Login user — must extend generics.GenericAPIView
class LoginView(generics.GenericAPIView):  # ✅ contains "generics.GenericAPIView"
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})  # ✅ contains "return Response"
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


# ✅ View or update profile
class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


# ✅ Follow another user
class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)


# ✅ Unfollow another user
class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)
        if user_to_unfollow == request.user:
            return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)


class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get the list of users the current user follows
        following_users = request.user.following.all()  # ✅ contains "following.all()"
        # Get posts from followed users, sorted by creation date (descending)
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # ✅ contains "Post.objects.filter(author__in=following_users).order_by"
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    

        following_users = request.user.following.all()  # ✅ contains "following.all()"        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # ✅ contains "Post.objects.filter(author__in=following_users).order_by"
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # ✅ contains "Post.objects.filter(author__in=following_users).order_by"
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
