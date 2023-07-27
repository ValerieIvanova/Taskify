# Generated by Django 4.2.3 on 2023-07-27 09:44

from django.db import migrations, models
import django.utils.timezone
import taskify.tasksApp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tasksApp', '0034_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, validators=[taskify.tasksApp.validators.date_in_the_past]),
        ),
    ]
