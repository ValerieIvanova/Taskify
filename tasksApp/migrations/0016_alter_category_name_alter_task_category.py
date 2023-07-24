# Generated by Django 4.2.2 on 2023-06-28 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasksApp', '0015_category_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(limit_choices_to={'category__isnull': False}, on_delete=django.db.models.deletion.CASCADE, to='tasksApp.category'),
        ),
    ]
