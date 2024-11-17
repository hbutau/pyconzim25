from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserManagerTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='user@example.com')
        self.assertEqual(user.email, 'user@example.com')
        self.assertFalse(user.has_usable_password())


    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(email='admin@example.com')
        self.assertEqual(user.email, 'admin@example.com')
        self.assertFalse(user.has_usable_password())
