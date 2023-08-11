from django.contrib import admin
from django.contrib.auth import get_user_model

from taskify.profileApp.models import UserProfile


UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_superuser', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username',)
    list_filter = ('username', 'is_staff', 'is_active')
    ordering = ('date_joined',)


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name')
    search_fields = ('user', 'first_name', 'last_name')
    list_filter = ('user', 'first_name', 'last_name')
    ordering = ('user', 'first_name', 'last_name')