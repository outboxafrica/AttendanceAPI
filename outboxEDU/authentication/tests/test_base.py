import json

from rest_framework.test import APITestCase, APIClient
from ..models import User

class TestBase(APITestCase):
  def setUp(self):
    self.client  = APIClient()

    self.userdata:{
        "username":"little",
        "email":"little@gmail.com",
        "password":"little33"
      }
    self.userdata2 = {
        "username":"little",
        "email":"little@gmail.com",
        "password":"little33"
    }
    self.userdata3 ={
      "username":"little",
      "email":"little@gmail.com",
      "password":"li"
    }

  # individualise user
  username = "jennylittle234"
  email = "jennylittle234@gmail.com"
  password = "1234little"

  # create user
  saved_user = User(
    username=username,
    email=email,
    password=password)
    