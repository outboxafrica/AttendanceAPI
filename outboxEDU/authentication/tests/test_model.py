from .test_base import TestBase
from django.contrib.auth import get_user_model
from ..models import User, UserManager


class ModelUserTestCase(TestBase):

# A class to test Model class

    def test_create_user(self):   
        self.saved_user.save()

    def test_new_user_normalized_email(self):
        email = "test@OUTBOX.COM"
        user = get_user_model().objects.create_user(
            username="outboxGuy",
            email=email,
            password="test123"
        )

        self.assertEqual(user.email, email.lower())

    def test_create_normal_user_with_no_username(self):
        with self.assertRaises(TypeError):
            user=User.objects.create_user(
                username=None,
                email=self.email,
                password=self.password
            )

    def test_create_normal_user_with_no_email(self):
        with self.assertRaises(TypeError):
            user=User.objects.create_user(
                username=self.username,
                email=None,
                password=self.password
            )

# Tests super user
class ModelUserManagerTestcase(TestBase):

    def test_create_superuser(self):

        user = User.objects.create_superuser(
            username=self.username,
            email=self.email,
            password=self.password
            )
        self.assertEqual(user.username, self.username)

        self.assertTrue(user.password, self.saved_user)

        self.assertTrue(user.is_superuser)

        self.assertTrue(user.is_staff)

        self.assertTrue(user.email_verified)


    def test_create_superuser_with_password_none(self):
        with self.assertRaises(TypeError):
            user = User.objects.create_superuser(
                username=self.username,
                email=self.email,
                password=None)

    def test_create_superuser_with_no_username(self):
        with self.assertRaises(TypeError):
            user=User.objects.create_superuser(
                username=None,
                email=self.email,
                password=self.password)

    def test_create_superuser_with_no_email(self):
        with self.assertRaises(TypeError):
            user=User.objects.create_superuser(
                username= self.username,
                email=None,
                password=self.password)
                
