# Generated by Django 4.2.3 on 2023-07-30 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasksApp', '0036_alter_task_due_date_alter_task_start_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reminder',
        ),
    ]