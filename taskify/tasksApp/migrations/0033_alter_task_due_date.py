# Generated by Django 4.2.3 on 2023-07-26 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasksApp', '0032_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, default=datetime.date(2023, 7, 26), null=True),
        ),
    ]
