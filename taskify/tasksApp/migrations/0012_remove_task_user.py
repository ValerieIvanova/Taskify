# Generated by Django 4.2.2 on 2023-06-27 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasksApp', '0011_auto_20230627_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
