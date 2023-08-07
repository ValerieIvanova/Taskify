from django.urls import path

from taskify.tasksApp.views import Dashboard, TaskDetails, TaskAdd, TaskEdit, TaskDelete, task_calendar, task_list, \
    mark_task_as_completed

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('calendar/', task_calendar, name='task_calendar'),
    path('calendar/events/', task_list, name='task_list'),
    path('add/', TaskAdd.as_view(), name='add_task'),
    path('details/<int:pk>/', TaskDetails.as_view(), name='details_task'),
    path('edit/<int:pk>/', TaskEdit.as_view(), name='edit_task'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete_task'),
    path('mark_task_completed/<int:task_id>/', mark_task_as_completed, name='mark_task_completed'),
]
