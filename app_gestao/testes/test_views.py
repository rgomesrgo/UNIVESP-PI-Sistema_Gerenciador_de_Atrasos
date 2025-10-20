from django.test import TestCase
from app_gestao.models import CadastroAlunos
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
import pandas as pd
from io import BytesIO

class ViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_home_view_status(self):
        response = self.client.get(reverse('home'))  # ajuste o nome da url
        self.assertEqual(response.status_code, 200)

    def test_home_view_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'app_gestao/base.html')

    def test_cadastro_aluno_view_post(self):
        # cria um Excel de teste em memória
        df = pd.DataFrame([{
            'R.A.': '9876543210',
            'Nome do estudante': 'Maria Souza',
            'Série/turma': '6B',
            'Endereço': 'Rua Y, 456',
            'Responsável 1': 'Carlos Souza',
            'Responsável 2': 'Maria Souza',
            'Contato(s)': '11988888888'
            
        }])
        buffer = BytesIO()
        df.to_excel(buffer, index=False)
        buffer.seek(0)
        arquivo = SimpleUploadedFile('alunos.xlsx', buffer.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response = self.client.post(reverse('cadastro'), {'arquivo_xlsx': arquivo})
        self.assertEqual(response.status_code, 302)  # redireciona após salvar
        self.assertTrue(CadastroAlunos.objects.filter(ra='9876543210').exists())