from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_username_and_email(self):
        username = "outboxGuy"
        email = "test@outbox.com"
        password = "test123"

        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password=password
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized_email(self):
        email = "test@OUTBOX.COM"
        user = get_user_model().objects.create_user(
            username="outboxGuy",
            email=email,
            password="test123"
        )

        self.assertEqual(user.email, email.lower())


