from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE
    )

    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Last Name',
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    email = models.EmailField(
        null=True,
        blank=True
    )

    profile_picture = models.ImageField(
        null=True,
        blank=True,
    )
