# Generated by Django 4.2.3 on 2023-07-30 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remindersApp', '0003_remove_reminder_is_completed_remove_reminder_task'),
        ('tasksApp', '0037_delete_reminder'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='reminder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='remindersApp.reminder'),
        ),
    ]
