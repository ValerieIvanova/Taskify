import django
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

from colorfield.fields import ColorField
from django.utils import timezone

from taskify.remindersApp.models import Reminder

UserModel = get_user_model()


class Category(models.Model):
    NAME_MAX_LENGTH = 100

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False,
    )

    color = ColorField(
        default='#FFFFFF',
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class TaskStatus(models.Model):
    STATUS_MAX_LENGTH = 100

    status = models.CharField(
        max_length=STATUS_MAX_LENGTH,
        null=False,
        blank=False,
        default='Not Started'
    )

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = 'Task Statuses'


class Task(models.Model):
    TITLE_MAX_LENGTH = 100
    PRIORITY_MAX_VALUE = 5
    ORIGIN_URL_MAX_LENGTH = 255

    title = models.CharField(
        null=False,
        blank=False,
        max_length=TITLE_MAX_LENGTH,
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created On'
    )

    start_date = models.DateField(
        null=False,
        blank=False,
    )

    due_date = models.DateField(
        null=True,
        blank=True,
        default=django.utils.timezone.now,
    )

    priority = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        default=1,
        validators=[
            MaxValueValidator(PRIORITY_MAX_VALUE, f'Priority must be between 1 and {PRIORITY_MAX_VALUE}')
        ]
    )

    origin_url = models.CharField(
        null=True,
        blank=True,
        max_length=ORIGIN_URL_MAX_LENGTH,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_DEFAULT,
        default=1,
        null=False,
        blank=False,
        limit_choices_to={'name__isnull': False},
    )

    status = models.ForeignKey(
        TaskStatus,
        on_delete=models.SET_DEFAULT,
        default=1,
        limit_choices_to={'status__isnull': False},
        null=True,
        blank=True
    )

    reminder = models.ForeignKey(
        Reminder,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        if self.reminder:
            self.reminder.delete()
        super().delete(*args, **kwargs)

    class Meta:
        ordering = ['status']