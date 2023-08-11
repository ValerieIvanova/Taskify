from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from taskify.remindersApp.models import Reminder
from taskify.tasksApp.models import Category, TaskStatus, Task

UserModel = get_user_model()


class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name='Test Category', color='#FF0000')
        self.assertEqual(category.name, 'Test Category')
        self.assertEqual(category.color, '#FF0000')

    def test_str_representation(self):
        category = Category.objects.create(name='Test Category', color='#FF0000')
        self.assertEqual(str(category), 'Test Category')


class TaskStatusModelTest(TestCase):
    def test_create_task_status(self):
        status = TaskStatus.objects.create(status='In Progress')
        self.assertEqual(status.status, 'In Progress')

    def test_str_representation(self):
        status = TaskStatus.objects.create(status='In Progress')
        self.assertEqual(str(status), 'In Progress')


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Test Category', color='#FF0000')
        self.status = TaskStatus.objects.create(status='In Progress')
        self.reminder = Reminder.objects.create(reminder_datetime=timezone.now())

    def test_create_task(self):
        task = Task.objects.create(
            title='Test Task',
            start_date=timezone.now().date(),
            user=self.user,
            category=self.category,
            status=self.status,
            reminder=self.reminder
        )
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.start_date, timezone.now().date())
        self.assertEqual(task.user, self.user)
        self.assertEqual(task.category, self.category)
        self.assertEqual(task.status, self.status)
        self.assertEqual(task.reminder, self.reminder)

    def test_str_representation(self):
        task = Task.objects.create(title='Test Task', start_date=timezone.now().date())
        self.assertEqual(str(task), 'Test Task')

    def test_task_deletion_with_reminder(self):
        task = Task.objects.create(title='Test Task', start_date=timezone.now().date(), reminder=self.reminder)
        task.delete()
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())
        self.assertFalse(Reminder.objects.filter(pk=self.reminder.pk).exists())

    def test_task_deletion_without_reminder(self):
        task = Task.objects.create(title='Test Task', start_date=timezone.now().date())
        task.delete()
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())
