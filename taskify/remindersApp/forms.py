from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from taskify.remindersApp.models import Reminder


class ReminderAddForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['reminder_datetime', 'message']
        widgets = {
            'reminder_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        task = kwargs.pop('task', None)
        super().__init__(*args, **kwargs)
        self.task = task

    def clean(self):
        cleaned_data = super().clean()
        reminder_date = cleaned_data.get('reminder_datetime')
        task_due_date = self.task.due_date

        if reminder_date < timezone.now():
            raise ValidationError('Reminder date and time cannot be in the past.')

        if reminder_date and task_due_date and reminder_date.date() > task_due_date:
            raise ValidationError('Reminder date must be before the due date of the task.')

        return cleaned_data
