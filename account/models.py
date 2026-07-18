from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from shared.models import TimestampMixins
from django.conf import settings



class User_Profile(TimestampMixins):

    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=17, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user_id}: {self.full_name}"



class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, password2=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        
        # Create user
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        # Create user profile
        User_Profile.objects.create(user_id=user)

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'a')
        
        return self.create_user(email, password, **extra_fields)



class User(AbstractUser, TimestampMixins):

    ROLES = [
        ('a', 'Admin'),
        ('d', 'Doctor'),
        ('p', 'Patient')
    ]

    username = None
    role = models.CharField(max_length=1, choices=ROLES, default='p')
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email