from django import forms
from django.utils import timezone

from taskify.tasksApp.models import Task


class TaskBaseForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'value': timezone.now().date()}),
    )

    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'value': timezone.now().date()}),
    )

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'start_date',
            'due_date',
            'priority',
            'category',
            'status',
            'origin_url',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'name': 'title',
                                            'placeholder': 'Task Title'}),
            'origin_url': forms.HiddenInput()
        }


class TaskAddForm(TaskBaseForm):
    pass


class TaskEditForm(TaskBaseForm):
    pass
