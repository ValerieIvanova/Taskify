# Generated by Django 4.2.3 on 2023-07-30 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remindersApp', '0002_rename_due_date_reminder_reminder_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='is_completed',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='task',
        ),
    ]
