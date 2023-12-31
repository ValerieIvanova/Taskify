# Generated by Django 4.2.3 on 2023-07-26 09:49

import datetime
from django.db import migrations, models
import taskify.tasksApp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tasksApp', '0029_alter_task_due_date_alter_task_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, default=models.DateField(default=datetime.date(2023, 7, 26), validators=[taskify.tasksApp.validators.date_in_the_past]), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(default=datetime.date(2023, 7, 26), validators=[taskify.tasksApp.validators.date_in_the_past]),
        ),
    ]
