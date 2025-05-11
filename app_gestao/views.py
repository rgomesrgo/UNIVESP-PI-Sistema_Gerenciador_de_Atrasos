from django.shortcuts import render, redirect, get_object_or_404
from .models import CadastroAlunos, RegAtrasos #Presenca#, 
from django.contrib import messages
from .forms import RegistroAtrasoForm
from datetime import date, datetime
from django.utils import timezone
import pandas as pd

# direciona para a home
def home(request):
    return render(request, "app_gestao/home.html")

# realiza o cadastro das turmas, atravez do arquivo .xlsx
def cadastro(request):
    if request.method == 'POST' and request.FILES['arquivo_xlsx']:
        arquivo_xlsx = request.FILES['arquivo_xlsx']
        try:
            df = pd.read_excel(arquivo_xlsx)  # Lê o arquivo Excel em um DataFrame

            # Certifica-se de que as colunas do Excel correspondam aos nomes das colunas do banco de dados
            df.rename(columns={
                'R.A.': 'ra',
                'Nome do estudante': 'nome_estudante',
                'Série/turma': 'serie_turma',
                'Endereço': 'endereco',
                'Responsável 1': 'responsavel1',
                'Responsável 2': 'responsavel2',
                'Contato(s)': 'contato'
            }, inplace=True)
            for index, row in df.iterrows():
                CadastroAlunos.objects.update_or_create(
                    ra=row['ra'],
                    defaults={
                        'nome_estudante': row['nome_estudante'],
                        'serie_turma': row['serie_turma'],
                        'endereco': row['endereco'],
                        'responsavel1': row['responsavel1'],
                        'responsavel2': row['responsavel2'],
                        'contato': row['contato'],
                    }
                )
            messages.success(request, 'Dados importados com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro ao importar dados: {e}')   
        return redirect('cadastro')
    return render(request, 'app_gestao/cadastrar_alunos.html')

# realiza o registro de atraso dos alunos
def registrar_atraso(request):
    aluno = None
    ra = None

    if request.method == 'POST':
        ra = request.POST.get('ra')

        if 'buscar' in request.POST:  # Quando o usuário clica em buscar
            try:
                aluno = CadastroAlunos.objects.get(ra=ra)
            except CadastroAlunos.DoesNotExist:
                aluno = None
                messages.error(request, "Aluno não encontrado. Verifique o RA e tente novamente.")

        elif 'salvar' in request.POST:  # Quando o usuário clica em salvar
            try:
                aluno = CadastroAlunos.objects.get(ra=ra)
                justificativa = request.POST.get('justificativa')
                horario_chegada = request.POST.get('horario_chegada')
                data_atraso = request.POST.get('data_atraso')
                RegAtrasos.objects.create(
                    ra=aluno,
                    data_atraso=data_atraso,
                    horario_chegada=horario_chegada,
                    justificativa=justificativa
                )
                messages.success(request, "Atraso registrado com sucesso!")
                return redirect('registrar_atraso')
            except CadastroAlunos.DoesNotExist:
                aluno = None
                messages.error(request, "Ocorreu um erro ao tentar salvar o atraso.")

    return render(request, 'app_gestao/registrar_atraso.html', {'aluno': aluno, 'ra': ra})

# realiza o registro da presença dos alunos
def presenca(request):
        return render(request, 'app_gestao/registrar_presenca.html')

# apresenta o relatório com o atrasos dos alunos de acordo com a turma
def relatorio(request):
        return render(request, 'app_gestao/relatorio.html')

#Limpa os dados dos bancos de dados
def limpar_banco(request):
    if request.method == 'POST':
        CadastroAlunos.objects.all().delete()
        RegAtrasos.objects.all().delete()
        messages.success(request, 'Todos os dados foram apagados com sucesso.')
    return redirect('cadastro')  # substitua com o nome da sua view
