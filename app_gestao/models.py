from django.db import models


# tabela com os dados de cadastro dos alunos
class CadastroAlunos(models.Model):
    ra = models.CharField(max_length=10, primary_key=True)
    nome_estudante = models.CharField(max_length=255)
    serie_turma = models.CharField(max_length=5)
    endereco = models.CharField(max_length=255)
    responsavel1 = models.CharField(max_length=255)
    responsavel2 = models.CharField(max_length=255, blank=True, null=True)
    contato = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_estudante


# tabela para registro dos atrasos
class RegAtrasos(models.Model):
    ra = models.ForeignKey(CadastroAlunos, on_delete=models.CASCADE)
    data_atraso = models.DateField(blank=False, null=False)
    horario_chegada = models.TimeField(blank=False, null=False)
    justificativa = models.TextField(max_length=255,blank=False, null=False)

    def __str__(self):
        return f"Atraso de {self.ra} em {self.data_atraso}"


# tabela para registro da presença dos alunos



