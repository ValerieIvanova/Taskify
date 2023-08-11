from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from django.urls import reverse

from taskify.remindersApp.models import Reminder
from taskify.tasksApp.models import Task

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


# Test Views:

class ReminderAddViewTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')
        self.task = Task.objects.create(
            title='Test Task',
            start_date='2023-08-15',
            user=self.user,
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('add_reminder', kwargs={'pk': self.task.pk}))
        self.assertRedirects(response, f'/profile/login/?next=/reminders/add-reminder/{self.task.pk}')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('add_reminder', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('add_reminder', kwargs={'pk': self.task.pk}))
        self.assertTemplateUsed(response, 'reminders/add_reminder.html')

    def test_form_submission_creates_reminder(self):
        self.client.login(username='testuser', password='testpassword')
        form_data = {
            'reminder_datetime': '2023-12-31 23:59:59',
            'message': 'Test reminder message',
        }
        response = self.client.post(reverse('add_reminder', kwargs={'pk': self.task.pk}), data=form_data)

        self.assertEqual(response.status_code, 200)

        task = Task.objects.get(pk=self.task.pk)
        self.assertEqual(task.reminder, Reminder.objects.first())
