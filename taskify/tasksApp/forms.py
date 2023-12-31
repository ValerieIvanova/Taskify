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
            'reminder'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'name': 'title',
                                            'placeholder': 'Task Title'}),
            'origin_url': forms.HiddenInput(),
        }


class TaskAddForm(TaskBaseForm):
    class Meta:
        model = Task
        exclude = ['reminder', 'user', 'enable_reminders']
        widgets = {
            'origin_url': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'name': 'title', 'placeholder': 'Task Title'}),
            'description': forms.Textarea(attrs={'name': 'description', 'placeholder': 'Task Description'}),
            'priority': forms.NumberInput(attrs={'placeholder': 'Priority'}),
        }

    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        if start_date < timezone.now().date():
            raise forms.ValidationError('Start date cannot be in the past.')
        return start_date

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        start_date = self.cleaned_data.get('start_date')
        if due_date < timezone.now().date():
            raise forms.ValidationError('Due date cannot be in the past.')
        elif start_date and due_date < start_date:
            raise forms.ValidationError('Due date cannot be before the start date.')
        return due_date


class TaskEditForm(TaskBaseForm):
    class Meta:
        model = Task
        exclude = ['reminder', 'user', 'origin_url', 'enable_reminders']
        widgets = {
            'title': forms.TextInput(attrs={'name': 'title', 'placeholder': 'Task Title'}),
            'description': forms.Textarea(attrs={'name': 'description', 'placeholder': 'Task Description'}),
            'priority': forms.NumberInput(attrs={'placeholder': 'Priority'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        self.fields['start_date'].disabled = True
