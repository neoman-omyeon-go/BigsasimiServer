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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    real_name = models.TextField(null=True)
    avatar = models.TextField(default=f"{settings.AVATAR_URI_PREFIX}/default.png")

    class Meta:
        db_table = "user_profile"

### testing...
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField()
    
class Tag(models.Model):
    name = models.CharField(max_length=30)
    posts = models.ManyToManyField(BlogPost)