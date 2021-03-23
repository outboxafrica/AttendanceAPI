"""
Tests for the views
"""
from .test_base import Testbase
from django.contrib.auth import get_user_model
from ..views import RegisterAPIView

class RegistrationAPIViewTestCase(Testbase):
  """
  View to post user
  """
