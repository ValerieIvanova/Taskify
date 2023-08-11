from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from taskify.remindersApp.models import Reminder

UserModel = get_user_model()


class ReminderModelTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(username='testuser', password='testpassword')
        self.reminder = Reminder.objects.create(
            reminder_datetime=datetime.now() + timedelta(days=1),
            message="Test Reminder",
            user=self.user,
        )

    def test_reminder_creation(self):
        self.assertEqual(self.reminder.reminder_datetime.date(), (datetime.now() + timedelta(days=1)).date())
        self.assertEqual(self.reminder.message, "Test Reminder")
        self.assertEqual(self.reminder.user, self.user)

    def test_str_representation(self):
        expected_str = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
        self.assertEqual(str(self.reminder), expected_str)
