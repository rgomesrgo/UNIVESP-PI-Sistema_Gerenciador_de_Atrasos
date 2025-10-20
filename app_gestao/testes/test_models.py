from django.test import TestCase
from app_gestao.models import CadastroAlunos, RegAtrasos, Presenca
from datetime import date, time

class ModelsTests(TestCase):
    def setUp(self):
        self.aluno = CadastroAlunos.objects.create(
            ra="1234567890",
            nome_estudante="João Silva",
            serie_turma="5A",
            endereco="Rua X, 123",
            responsavel1="Maria Silva",
            responsavel2="José Silva",
            contato="11999999999"
        )

    def test_cadastro_alunos_str(self):
        self.assertEqual(str(self.aluno), "João Silva (5A)")

    def test_registro_atraso(self):
        atraso = RegAtrasos.objects.create(
            ra=self.aluno,
            data_atraso=date.today(),
            horario_chegada=time(8, 30),
            justificativa="Trânsito"
        )
        self.assertEqual(str(atraso), f"Atraso de {self.aluno} em {date.today()}")

    def test_presenca_unique_together(self):
        Presenca.objects.create(aluno=self.aluno, data=date.today(), presente=True)
        with self.assertRaises(Exception):
            # Tenta criar outra presença para o mesmo aluno e data
            Presenca.objects.create(aluno=self.aluno, data=date.today(), presente=False)