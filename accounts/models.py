import json

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import validate_email
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class FitUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, validators=[validate_email])
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Required for admin access
    date_joined = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    Lifestyle_Habits = models.TextField(blank=True)
    Additional_Notes = models.TextField(blank=True)
    fit_points = models.PositiveIntegerField(default=0)
    id = models.AutoField(primary_key=True)
    friends = models.TextField(blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  # Specify fields required for createsuperuser

    def __str__(self):
        return self.username

