from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginTests(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpass123'
        User.objects.create_user(username=self.username, password=self.password)

    def test_login_sucesso(self):
        result = authenticate(username=self.username, password=self.password)
        self.assertIsNotNone(result)

    def test_login_senha_incorreta(self):
        result = authenticate(username=self.username, password='wrongpass')
        self.assertIsNone(result)

    def test_login_usuario_inexistente(self):
        result = authenticate(username='nouser', password='any_pass')
        self.assertIsNone(result)