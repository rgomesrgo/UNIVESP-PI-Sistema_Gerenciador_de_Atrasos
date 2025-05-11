from django.shortcuts import render, redirect, get_object_or_404
from .models import CadastroAlunos, RegAtrasos, Presenca
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

# realiza o registro da presença dos alunos
def registrar_presenca(request):
    data_selecionada = request.POST.get("data") or request.GET.get("data")
    turma_selecionada = request.POST.get("turma") or request.GET.get("turma")
    alunos = []

    if turma_selecionada:
        alunos = CadastroAlunos.objects.filter(serie_turma=turma_selecionada)

    if request.method == "POST" and "registrar" in request.POST:
        for aluno in alunos:
            status = request.POST.get(f"presenca_{aluno.ra}", "presente")
            presente = status == "presente"
            try:
                Presenca.objects.update_or_create(
                    aluno=aluno,
                    data=data_selecionada,
                    defaults={"presente": presente}
                )
            except IntegrityError:
                messages.error(request, f"Erro ao registrar presença para {aluno.nome_estudante}")

        messages.success(request, "Presenças registradas com sucesso!")
        return redirect("registrar_presenca")

    turmas = CadastroAlunos.objects.values_list("serie_turma", flat=True).distinct()

    return render(request, "app_gestao/registrar_presenca.html", {
        "data_selecionada": data_selecionada,
        "turma_selecionada": turma_selecionada,
        "alunos": alunos,
        "turmas": turmas,
    })

# apresenta o relatório com o atrasos dos alunos de acordo com a turma
def relatorio(request):
        return render(request, 'app_gestao/relatorio.html')

#Limpa os dados dos bancos de dados
def limpar_banco(request):
    if request.method == 'POST':
        CadastroAlunos.objects.all().delete()
        RegAtrasos.objects.all().delete()
        Presenca.objects.all().delete()
        messages.success(request, 'Todos os dados foram apagados com sucesso.')
    return redirect('cadastro')  # substitua com o nome da sua view

#seleciona o aluno para o registro do atraso
def registrar_atraso(request):
    turmas = CadastroAlunos.objects.values_list('serie_turma', flat=True).distinct()
    alunos = []
    turma_selecionada = None

    if request.method == 'POST':
        turma_selecionada = request.POST.get('turma')
        if turma_selecionada:
            alunos = CadastroAlunos.objects.filter(serie_turma=turma_selecionada)

    return render(request, 'app_gestao/registrar_atraso.html', {
        'turmas': turmas,
        'alunos': alunos,
        'turma_selecionada': turma_selecionada,
    })

#efetua o registro do atraso do aluno selecionado no banco de dados
def registrar_atraso_aluno(request, ra):
    aluno = get_object_or_404(CadastroAlunos, ra=ra)

    if request.method == 'POST' and 'salvar' in request.POST:
        data_atraso = request.POST.get('data_atraso')
        horario_chegada = request.POST.get('horario_chegada')
        justificativa = request.POST.get('justificativa')

        RegAtrasos.objects.create(
            ra=aluno,
            data_atraso=data_atraso,
            horario_chegada=horario_chegada,
            justificativa=justificativa,
        )
        messages.success(request, 'Atraso registrado com sucesso!')
        return redirect('registrar_atraso')

    return render(request, 'app_gestao/registrar_atraso_aluno.html', {'aluno': aluno})