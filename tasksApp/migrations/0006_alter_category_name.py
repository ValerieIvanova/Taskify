# Generated by Django 4.2.2 on 2023-06-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasksApp', '0005_alter_category_color_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Personal', 'Personal'), ('Work', 'Work'), ('Health', 'Health'), ('Fitness', 'Fitness'), ('Education', 'Education'), ('Finance', 'Finance'), ('Social', 'Social'), ('Travel', 'Travel'), ('Hobbies', 'Hobbies'), ('Other', 'Other')], default='None', max_length=100),
        ),
    ]
