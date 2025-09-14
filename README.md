
<div style="text-align: center;">
  <img src="https://univesp.br/sites/527174b7b24a527adc000002/assets/590b74fb9caf4d3c61001003/Univesp_logo_jpg_rgb.jpg" width="400"/>
</div>


## Projeto Integrador em Computação II - DRP14 - Turma 001 - Grupo 007
**Ementa da disciplina Projeto Integrador em Computação II:** Resolução de problemas. Levantamento de requisitos. Desenvolvimento web com framework. HTML. CSS. Linguagem de script. Banco de Dados. Controle de Versão. Nuvem. API. Acessibilidade. Testes. Análise de dados.

**Carga Horária:** 80 h 

**Objetivo:** Desenvolver um software com framework web que utilize banco de dados, inclua script web (Javascript), nuvem, uso de API, acessibilidade, controle de versão e testes. Opcionalmente, incluir análise de dados.

### Grupo:
ALFONSO JAIME DE CARVALHO MELO USLAR

CARLOS DE OLIVEIRA RODRIGUES

DANIELA DE PROENCA MIAO

DOUGLAS RODRIGUES SILVA

MARCELO ALMEIDA DE SOUZA

LUCAS MELO DE CHIARA

RAFAEL GOMES DE OLIVEIRA

ROBSON DOS SANTOS PIMENTA MARTINS



## Autorização de Uso
### 1. Salve uma cópia da aplicação para desenvolver as suas melhorias!
<a href="https://github.com/lucasdechiara/UNIVESP-PI-Sistema_Gerenciador_de_Atrasos/fork">
    <img alt="Folk" title="Fork Button" src="https://shields.io/badge/-DAR%20FORK-red.svg?&style=for-the-badge&logo=github&logoColor=white"/></a>


## SISTEMA DE CONTROLE DE ATRASOS

**OBJETIVO:** Gerenciar o horário de entrada dos estudantes que chegam após o fechamento dos portões.

**USUÁRIOS:** Este sistema será utilizado pelo setor da secretaria e equipe de gestão.

### Escopo:
1. O sistema é constituído por banco de dados (PostgreSQL) onde estão armazenadas as informações dos anlunos: nome, R.A. (Registro do Aluno), série/turma, endereço, nome dos responsáveis e contatos.
2. O sistema não se integra aos sistemas da escola, assim os dados precisam ser carregados via arquivo .xlsx.
3. São efetuados dois tipos de registros: registro de frequência e registro das ocorrências em relação aos atrasos. 
4. Especificado a turma do aluno, ao clicar no nome do aluno é habilitado o campo para registro do atraso.
5. O sistema permite a inclusão/exclusão de alunos.
6. Por fim, o sistema apresenta um quantificador do total de presenças e atrasos dos alunos, de acordo com a seleção da turma e do mês, a última coluna indica o percentual de atraso, com base nesse percentual são definidas duas regras do negócio:
•	Se o aluno possuir algum atraso no mês a linha é pintada de amarelo.
•	Caso o percentual seja superior a 50% a linha fica vermelha.
7. Um relatório .xlsx com a relação de atrasos e justificativas pode ser extraído do sistema.

### Bibliotecas:
* utilize o arquivo "requirements.txt" para instalar as bibliotecas necessárias
 
### Métodos e Instrumentos:
* Linguagem de Programação: Python
* Framework Web: Django
* Banco de Dados: PostgreSQL
* Biblioteca para Leitura de Arquivos Excel: openpyxl e pandas
* Framework CSS: Bootstrap 5
* Ambiente de Desenvolvimento Integrado (IDE): Visual Studio Code (VSCode)
* Sistema de Controle de Versão: Git


### Apresentação do sistema no YouTube:
<a href="https://www.youtube.com/watch?v=QbGWYWc5gDA">
  <img src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png" width="50" />
</a>


#### Repositório destinado ao versionamento da aplicação desenvolvida na disciplina de Projeto Integrador II da UNIVESP.
