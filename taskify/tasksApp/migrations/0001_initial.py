# Generated by Django 4.2.2 on 2023-06-27 19:12

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('Personal', 'Personal'), ('Work', 'Work'), ('Social', 'Social'), ('Hobbies', 'Hobbies'), ('Education', 'Education'), ('Health', 'Health'), ('Fitness', 'Fitness'), ('Travel', 'Travel'), ('Finance', 'Finance'), ('Other', 'Other')], max_length=100, null=True)),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None)),
            ],
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Not Started', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Task Statuses',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('priority', models.IntegerField(blank=True, default=1, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasksApp.category')),
                ('status', models.ForeignKey(default='Not Started', on_delete=django.db.models.deletion.CASCADE, to='tasksApp.taskstatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['status'],
            },
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
