from django.urls import path

from taskify.remindersApp.views import AddReminderView, DeleteReminderView

urlpatterns = [
    path('add-reminder/<int:pk>', AddReminderView.as_view(), name='add_reminder'),
    path('delete-reminder/<int:pk>', DeleteReminderView.as_view(), name='delete_reminder'),
]