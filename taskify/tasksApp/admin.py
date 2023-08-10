from django.contrib import admin

from taskify.tasksApp.models import Category, TaskStatus, Task


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    list_filter = ('name', 'color')
    search_fields = ('name', 'color')


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'reminder', 'created_on', 'user')
    list_filter = ('status', 'category', 'user')
    search_fields = ('title', 'description', 'user')
    ordering = ('-created_on',)
    date_hierarchy = 'created_on'
