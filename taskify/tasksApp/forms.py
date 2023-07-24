from django import forms

from taskify.tasksApp.models import Task


class TaskBaseForm(forms.ModelForm):
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
            'start_date': forms.DateTimeInput(attrs={'type': 'date', 'format': 'd-m-Y'}),
            'due_date': forms.DateTimeInput(attrs={'type': 'date', 'format': 'd-m-Y'}),
            'title': forms.TextInput(attrs={'name': 'title',
                                            'placeholder': 'Task Title'}),
            'origin_url': forms.HiddenInput()
        }


class TaskAddForm(TaskBaseForm):
    pass


class TaskEditForm(TaskBaseForm):
    pass
