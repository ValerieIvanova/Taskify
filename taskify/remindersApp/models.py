from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Reminder(models.Model):
    reminder_datetime = models.DateTimeField(
        null=False,
        blank=False,
    )

    message = models.TextField(
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
        return self.reminder_datetime.strftime("%Y-%m-%d %H:%M")
