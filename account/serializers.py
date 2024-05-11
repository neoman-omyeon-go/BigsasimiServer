from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, UserProfile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data.get('username'),
            email=validated_data.get('email', None),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        UserProfile.objects.create(
            user=user,
            real_name="User Name",
            gender="Other",
            age=25,
            height=180,
            weight=75,
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


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class EditUserProfileSerializer(serializers.Serializer):
    # 필수
    # real_name = serializers.CharField(required=False)
    gender = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    height = serializers.IntegerField(required=True)
    weight = serializers.IntegerField(required=True)

    # 선택
    goals_calories = serializers.IntegerField(required=False)
    goals_carb = serializers.IntegerField(required=False)
    goals_protein = serializers.IntegerField(required=False)
    goals_fat = serializers.IntegerField(required=False)
    goals_natrium = serializers.IntegerField(required=False)
    goals_saccharide = serializers.IntegerField(required=False)

    # +@
    disease = serializers.CharField(required=False)
    allergy = serializers.CharField(required=False)
    avatar = serializers.FileField(required=False)
