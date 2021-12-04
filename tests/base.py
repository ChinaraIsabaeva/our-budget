from django.contrib.auth.models import User
from django.test import TestCase, Client


class BaseTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'test_user',
            'test_user@example.com',
            'randompass',
        )
        self.client = Client()
        self.client.force_login(
            self.user
        )
