# Generated by Django 4.2.4 on 2023-08-07 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasksApp', '0039_alter_task_reminder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='enable_reminders',
        ),
    ]
