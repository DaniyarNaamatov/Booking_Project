from django.contrib import admin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def _creat_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Неправильный логин")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.create_activation_code()
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        return self._creat_user(email, password, **extra_fields)


    def create_superuser(self, email, password, **extra_fileds):
        extra_fileds.setdefault('is_active', True)
        extra_fileds.setdefault('is_staff', True)
        extra_fileds.setdefault('is_superuser', True)


        if extra_fileds.get('is_active') is not True:
            raise ValueError('is_active must be True')
        if extra_fileds.get('is_staff') is not True:
            raise ValueError('is_staff must be True')
        return self._creat_user(email, password, **extra_fileds)


class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    username = None
    is_active = models.BooleanField(default=True)
    activation_code = models.CharField(max_length=100, blank=True)
    objects = UserManager()


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code