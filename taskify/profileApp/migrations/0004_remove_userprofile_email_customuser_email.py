# Generated by Django 4.2.4 on 2023-08-02 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0003_remove_userprofile_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]