from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
# pyrefly: ignore [missing-import]
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import User
from accounts.serializers import (
    UserSerializer,
    RegisterSerializer,
    CustomTokenObtainPairSerializer
)
from accounts.permissions import IsHRManager

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsHRManager]  # Only HR and Admins can create users manually

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
