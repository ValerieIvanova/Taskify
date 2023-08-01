from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from taskify.remindersApp.forms import ReminderAddForm
from taskify.remindersApp.models import Reminder
from taskify.tasksApp.models import Task


class AddReminderView(CreateView):
    model = Reminder
    form_class = ReminderAddForm
    template_name = 'reminders/add_reminder.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=self.kwargs['pk'])
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        kwargs['task'] = task
        return kwargs

    def form_valid(self, form):
        task = form.task
        reminder = form.save()
        task.reminder = reminder
        task.save()
        return super().form_valid(form)

    def get_success_url(self):
        task_id = self.kwargs['pk']
        return reverse_lazy('details_task', kwargs={'pk': task_id})


class DeleteReminderView(DeleteView):
    model = Reminder
    template_name = 'reminders/delete_reminder.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'reminder'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, reminder=self.object)
        return context
