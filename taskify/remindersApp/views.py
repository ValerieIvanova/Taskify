from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from taskify import settings
from taskify.remindersApp.forms import ReminderAddForm
from taskify.remindersApp.models import Reminder
from taskify.tasksApp.models import Task
from taskify.remindersApp.tasks import send_email_reminder


class ReminderAdd(LoginRequiredMixin, CreateView):
    model = Reminder
    form_class = ReminderAddForm
    template_name = 'reminders/add_reminder.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=self.kwargs['pk'])
        if context['task'].user != self.request.user:
            raise Http404
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

        send_date = reminder.reminder_datetime
        subject = f"Gentle Nudge: Don't Forget About Your Super Important Task!"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [self.request.user.email]

        send_email_reminder.apply_async(
            args=[task.title, task.due_date, task.user.username, reminder.message, subject, from_email, recipient_list],
            eta=send_date
        )

        return super().form_valid(form)

    def get_success_url(self):
        task_id = self.kwargs['pk']
        return reverse_lazy('details_task', kwargs={'pk': task_id})


class ReminderDelete(LoginRequiredMixin, DeleteView):
    model = Reminder
    template_name = 'reminders/delete_reminder.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'reminder'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, reminder=self.object)
        if context['task'].user != self.request.user:
            raise Http404
        return context
