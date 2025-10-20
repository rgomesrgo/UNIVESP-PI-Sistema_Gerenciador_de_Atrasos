from django.test import TestCase
from django.contrib.auth import authenticate

class LoginTests(TestCase):
    def setUp(self):
        # Crie um usuário de teste usando o modelo User do Django
        from django.contrib.auth.models import User
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

class TestarPaginas(TestCase):
    def testar_se_pagina_principal_carrega_completamente(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_gestao/base.html')
        self.assertContains(response, 'SISTEMA DE CONTROLE DE ATRASOS 2.0')