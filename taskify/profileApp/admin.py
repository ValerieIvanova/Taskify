from django.contrib import admin

from taskify.profileApp.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')
    search_fields = ('user', 'first_name', 'last_name')
    list_filter = ('user', 'first_name', 'last_name')
    ordering = ('user', 'first_name', 'last_name')