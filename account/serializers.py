from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, UserProfile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data.get('username'),
            email=validated_data.get('email', None)
        )
        user.set_password(validated_data.get('password'))
        user.save()
        profile = UserProfile.objects.create(
            user=user
        )
        
        return user

    class Meta:
        model = User
        fields = '__all__'


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def authenticate_user(self) -> User:
        if self.is_valid():
            username = self.validated_data.get('username')
            password = self.validated_data.get('password')
            print(self.validated_data)
            user = authenticate(username=username, password=password)
            return user
        else:
            return None
