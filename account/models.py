from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class UserType(object):
    REGULAR_USER = "Regular User"
    ADMIN = "Admin"
    SUPER_ADMIN = "Super Admin"


class User(AbstractUser):
    """
    username, email, password
    [first_name, last_name, is_active, is_staff, is_active]
    """
    username = models.TextField(unique=True)
    email = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    # One of UserType
    admin_type = models.TextField(default=UserType.REGULAR_USER)

    # emmail
    is_email_verify = models.BooleanField(default=False)
    verify_email_token = models.TextField(null=True)
    verify_email_token_expire_time = models.DateTimeField(null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    grass = ArrayField(models.DateTimeField(), blank=True, default=list)

    last_activity = models.DateTimeField(null=True)

    def is_admin(self):
        return self.admin_type == UserType.ADMIN

    def is_super_admin(self):
        return self.admin_type == UserType.SUPER_ADMIN

    def is_admin_role(self):
        return self.admin_type in [UserType.ADMIN, UserType.SUPER_ADMIN]

    class Meta:
        db_table = "user"
        ordering = ['id']


class UserProfile(models.Model):
    """
    입력 : user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_uniq')
    avatar = models.TextField(default=f"{settings.AVATAR_UPLOAD_DIR}/default-avatar.png")

    # 필수 입력
    real_name = models.TextField(default='anonymous',null=True)                         # 실명
    gender = models.CharField(default='None', max_length=256, blank=False, null=False)  # 성별
    age = models.PositiveSmallIntegerField(default=0, blank=False, null=False)          # 나이
    height = models.PositiveSmallIntegerField(default=0, blank=False, null=False)       # 신장
    weight = models.PositiveSmallIntegerField(default=0, blank=False, null=False)       # 체중
    
    ##### +@입력
    # 개인 환경
    disease = ArrayField(models.CharField(max_length=256), blank=True, default=list)    # 질환 정보
    allergy = ArrayField(models.CharField(max_length=256), blank=True, default=list)    # 알러지 정보
    medicine = ArrayField(models.CharField(max_length=256), blank=True, default=list)   # 섭취중인 약 정보
    
    # 개인 설정 목표
    goals_calories = models.PositiveIntegerField(default=2500)
    goals_carb = models.PositiveIntegerField(default=0)     # 탄수화물
    goals_protein = models.PositiveIntegerField(default=0)  # 단백질
    goals_fat = models.PositiveIntegerField(default=0)      # 지방
    # goals_natrium  = models.PositiveIntegerField(default=0) # 나트륨
    
    class Meta:
        db_table = "user_profile"
        ordering = ['id']
