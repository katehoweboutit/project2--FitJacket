import json

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
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
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Required for admin access
    date_joined = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=20)
    weight = models.PositiveIntegerField(default=160)
    LifestyleHabits = models.TextField(blank=True)
    AdditionalNotes = models.TextField(blank=True)
    fit_points = models.PositiveIntegerField(default=0)
    id = models.AutoField(primary_key=True)
    friends = models.TextField(blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  # Specify fields required for createsuperuser

    def __str__(self):
        return self.username
    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = self.email
        super(FitUser, self).save(*args, **kwargs)

