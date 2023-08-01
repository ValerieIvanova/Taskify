from django.contrib import admin

from taskify.remindersApp.models import Reminder


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    pass
