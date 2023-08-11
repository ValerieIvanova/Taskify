from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone

from taskify.profileApp.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_MAX_LENGTH = 150
    EMAIL_MAX_LENGTH = 254

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        null=False,
        blank=False,
        validators=[UnicodeUsernameValidator()],
    )

    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH,
        unique=True,
        null=False,
        blank=False
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    date_joined = models.DateTimeField(
        default=timezone.now,
    )

    USERNAME_FIELD = 'username'
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    @classmethod
    def get_by_natural_key(cls, username):
        return cls.objects.get(username=username)

    class Meta:
        ordering = ['pk']


UserModel = get_user_model()


class UserProfile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        verbose_name='Last Name',
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures',
        null=True,
        blank=True,
    )

    objects = models.Manager()

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return f'{self.user}'
