from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TemplatesTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_home_view_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_gestao/base.html')

    def test_home_template_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'SISTEMA DE CONTROLE DE ATRASOS 2.0')
        self.assertContains(response, '<footer')
        self.assertContains(response, '<nav')