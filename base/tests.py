from django.test import TestCase,Client
from django.contrib.auth.models import User
from base.models import Tickets

class UserCreationTest(TestCase):
    def setUp(self):
        self.client=Client()
        self.user=User.objects.get(id=1)
        print(self.user)

    def test_model_creation(self):
        ticket=Tickets.objects.create(user=self.user,title='testTitle',summary='hello world')
        assert Tickets.objects.count() == 1   


