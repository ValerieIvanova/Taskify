# Generated by Django 4.2.2 on 2023-06-27 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasksApp', '0007_alter_task_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(choices=[('Personal', 'Personal'), ('Work', 'Work'), ('Health', 'Health'), ('Fitness', 'Fitness'), ('Education', 'Education'), ('Finance', 'Finance'), ('Social', 'Social'), ('Travel', 'Travel'), ('Hobbies', 'Hobbies'), ('Other', 'Other')], default=1, on_delete=django.db.models.deletion.CASCADE, to='tasksApp.category'),
        ),
    ]
