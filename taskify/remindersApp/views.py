from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from taskify import settings
from taskify.mixins import UserOwnershipMixin
from taskify.remindersApp.forms import ReminderAddForm
from taskify.remindersApp.models import Reminder
from taskify.tasksApp.models import Task
from taskify.remindersApp.tasks import send_email_reminder


class ReminderAdd(LoginRequiredMixin, UserOwnershipMixin, CreateView):
    model = Reminder
    form_class = ReminderAddForm
    template_name = 'reminders/add_reminder.html'
    user_obj = 'user'

    def get_context_data(self, **kwargs):
        task = self.get_task_by_pk()
        context = super().get_context_data(**kwargs)
        context['task'] = task
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        task = self.get_task_by_pk()
        kwargs['task'] = task
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
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


class ReminderDelete(LoginRequiredMixin, UserOwnershipMixin, DeleteView):
    model = Reminder
    template_name = 'reminders/delete_reminder.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'reminder'
    user_obj = 'user'

    def get_context_data(self, **kwargs):
        task = self.get_task_by_reminder()
        context = super().get_context_data(**kwargs)
        context['task'] = task
        return context
