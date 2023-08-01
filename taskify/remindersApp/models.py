from django.db import models


class Reminder(models.Model):
    reminder_datetime = models.DateTimeField(
        null=False,
        blank=False,
    )

    message = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.reminder_datetime.strftime("%Y-%m-%d %H:%M")
