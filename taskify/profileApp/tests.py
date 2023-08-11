from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate
from taskify.profileApp.models import UserProfile

UserModel = get_user_model()


class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(username='testuser', password='testpassword')

    def test_create_user(self):
        user = UserModel.objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_str_representation(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_get_by_natural_key(self):
        natural_user = UserModel.get_by_natural_key('testuser')
        self.assertEqual(natural_user, self.user)

    def test_create_user_invalid_data(self):
        with self.assertRaises(ValueError):
            UserModel.objects.create_user(username='a' * (UserModel.USERNAME_MAX_LENGTH + 1), password='testpassword')

    def test_login_invalid_credentials(self):
        user = authenticate(username='invalid_user', password='invalid_password')
        self.assertIsNone(user)


class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(username='testuser2', password='testpassword')
        self.profile = UserProfile.objects.get(user=self.user)
        self.profile.first_name = "Test"
        self.profile.last_name = 'Testov'
        self.profile.age = 30
        self.profile.email = 'test@example.com'
        self.profile.save()

    def test_create_user_profile(self):
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.first_name, 'Test')
        self.assertEqual(profile.last_name, 'Testov')
        self.assertEqual(profile.age, 30)
        self.assertEqual(profile.email, 'test@example.com')

    def test_str_representation(self):
        self.assertEqual(str(self.profile), 'Test Testov')
