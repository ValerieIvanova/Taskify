from django.urls import path

from taskify.remindersApp.views import ReminderAdd, ReminderDelete

urlpatterns = [
    path('add-reminder/<int:pk>', ReminderAdd.as_view(), name='add_reminder'),
    path('delete-reminder/<int:pk>', ReminderDelete.as_view(), name='delete_reminder'),
]
