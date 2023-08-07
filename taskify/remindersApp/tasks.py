from __future__ import absolute_import
from celery import shared_task, Celery
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from taskify.remindersApp.models import Reminder

app = Celery('taskify')
app.config_from_object('django.conf:settings', namespace='CELERY')


@shared_task
def send_email_reminder(task_title, task_due_date, username, subject, from_email, recipient_list):
    html_message = render_to_string(
        template_name='reminders/email_reminder.html',
        context={
            'task_title': task_title,
            'task_due_date': task_due_date,
            'username': username,
        }
    )
    plain_message = strip_tags(html_message)

    send_mail(
        subject=subject,
        message=plain_message,
        html_message=html_message,
        from_email=from_email,
        recipient_list=recipient_list
    )

    try:
        reminder = Reminder.objects.get(task__title=task_title)
        reminder.delete()
    except Reminder.DoesNotExist:
        pass

