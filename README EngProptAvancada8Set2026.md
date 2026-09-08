# Saúde Recife, Análise de Dados com Engenharia de Prompt

Análise acadêmica da Unidade Curricular **TADS25.109/3N, Data Science: Princípios e Técnicas, 2026.2**, da Faculdade Senac de Pernambuco.

O exercício investiga a questão:

> **O cadastro permite orientar o acesso aos serviços do Saúde Recife?**

A análise combina uma planilha de cadastro de unidades de saúde e um PDF com orientações de acesso do Conecta Recife. O trabalho aplica conceitos de **CRISP-DM**, decomposição de problemas, metaprompting, encadeamento de prompts, comparação de respostas, validação de cálculos e análise de lacunas informacionais.

## 1. Identificação

| Campo | Informação |
|---|---|
| Aluna | Thayná Batista da Silva |
| Curso | Análise e Desenvolvimento de Sistemas |
| Turma | `[TADS25.109/3N]` |
| Unidade Curricular | Data Science: Princípios e Técnicas |
| Período | 2026.2 |
| Instituição | Faculdade Senac de Pernambuco |
| Tema | Saúde Recife, acesso aos serviços |
| Metodologia | CRISP-DM + Engenharia de Prompt |

## 2. Pergunta analítica

**Quais informações presentes no cadastro de unidades são suficientes para orientar o cidadão sobre sua unidade de referência e o caminho de acesso a serviços de saúde, quando comparadas às regras apresentadas no Conecta Recife?**

### Hipótese verificável

**H1:** O cadastro, isoladamente, não contém todas as informações necessárias para orientar o acesso de forma confiável, porque registra atributos da unidade, mas não representa integralmente critérios dependentes do cidadão, como endereço residencial, cobertura territorial, requisitos de acesso digital, vínculo com equipe e disponibilidade de atendimento.

## 3. Principais achados

### Achado 1, lacuna para identificação da unidade de referência

A planilha possui 153 registros, sendo 131 USF e 22 UBS, e informa endereço, bairro, horário, telefone, especialidades e uma orientação textual de uso. Entretanto, o endereço disponível é o **endereço da unidade**, não o endereço residencial do cidadão.

O PDF informa que a unidade de referência pode depender do endereço de residência e, no caso de odontologia, também da existência ou não de cobertura por equipe de Saúde da Família.

Portanto, o cadastro ajuda a descrever unidades, mas não permite, sozinho, determinar a unidade de referência de um cidadão específico.

### Achado 2, especialidade não equivale a caminho de acesso

138 dos 153 registros possuem odontologia indicada no campo `especialidade`, correspondendo a **90,20%** do cadastro.

Esse dado demonstra presença cadastral da especialidade, mas não demonstra que o cidadão possa simplesmente escolher qualquer uma dessas unidades. As orientações oficiais distinguem o caminho de acesso conforme a cobertura por equipe de Saúde da Família e a unidade de referência da residência.

Assim, o campo `especialidade` é útil para descrever oferta declarada, mas insuficiente para orientar acesso sem contexto territorial e de elegibilidade.

## 4. Conferência de cálculo

Critério:

> registros cujo campo `especialidade` contém o termo relacionado a odontologia, independentemente de maiúsculas ou minúsculas.

- Registros avaliados: 153
- Registros com odontologia: 138
- Fórmula: `138 / 153 × 100`
- Resultado: **90,196078...%**
- Resultado arredondado: **90,20%**

A conferência foi realizada diretamente sobre a planilha, utilizando busca textual no campo `especialidade`.

Esse percentual não representa disponibilidade de vagas, capacidade de atendimento ou possibilidade de agendamento.

## 5. Conferência de orientação

A orientação sobre o serviço de busca da unidade de saúde por endereço informa que o cidadão pode localizar sua unidade a partir do endereço de residência.

A orientação também é compatível com a página oficial consultada, que descreve a localização da unidade através do endereço residencial.

Na orientação de odontologia, a fonte oficial diferencia cidadãos cobertos por equipe de Saúde da Família daqueles que não possuem essa cobertura. Essa distinção confirma que o cadastro de estabelecimentos não é suficiente para inferir automaticamente a unidade de referência de cada cidadão.

## 6. Recomendação

Implementar no aplicativo uma etapa de **identificação personalizada da unidade de referência**, utilizando os dados cadastrais do cidadão, especialmente endereço residencial, e aplicando regras de cobertura territorial e vínculo com equipe.

O resultado deveria apresentar:

1. Unidade de referência.
2. Tipo da unidade, USF ou UBS.
3. Serviços compatíveis com o perfil e a referência.
4. Forma de acesso, presencial ou digital.
5. Requisitos necessários.
6. Canal de contato.
7. Aviso explícito de que horário cadastral não representa disponibilidade de consulta.

A recomendação deve evitar inferências não suportadas pelo cadastro, principalmente transformar a existência de uma especialidade ou um horário em promessa de atendimento.

## 7. Estrutura do repositório

```text
.
├── README.md
├── analise-completa.md
├── prompts.md
├── dados/
│   └── 01_Cadastro_Unidades_Saude_Recife.xlsx
├── fontes/
│   ├── 02_Orientacoes_Acesso_Saude_Recife.pdf
│   └── Aula_Prompts_Data_Science_PI_Saude_SENAC.pdf
└── evidencias/
    └── calculo-odontologia.md
```

Os nomes e caminhos acima são uma sugestão de organização para o GitHub. Os arquivos-fonte originais devem ser mantidos no repositório apenas quando sua distribuição estiver autorizada.

## 8. Como reproduzir a análise

1. Abrir a planilha `01_Cadastro_Unidades_Saude_Recife.xlsx`.
2. Utilizar a aba `Cadastro` como tabela principal.
3. Consultar a aba `Dicionario` antes de interpretar os campos.
4. Consultar a aba `Fontes` para rastreabilidade.
5. Ler o PDF `02_Orientacoes_Acesso_Saude_Recife.pdf`.
6. Comparar os critérios de acesso do PDF com os atributos efetivamente disponíveis na planilha.
7. Para a conferência numérica, contar os registros cujo campo `especialidade` contém odontologia.
8. Calcular `registros que atendem ao critério / registros avaliados × 100`.
9. Não interpretar horário, especialidade ou telefone como prova de disponibilidade ou agendamento.
10. Registrar limitações e lacunas antes de formular recomendações.

## 9. CRISP-DM aplicado

### Business Understanding

Problema: avaliar se o cadastro de unidades fornece informações suficientes para orientar o acesso aos serviços de saúde.

### Data Understanding

Foram examinadas a planilha de unidades e o PDF de orientações de acesso. A planilha contém 153 registros, 131 USF e 22 UBS, além de atributos como nome, horário, orientação de uso, especialidade, endereço, bairro, telefone, CNES e fonte.

### Data Preparation

Os valores originais foram preservados. Para contagens semânticas, diferenças de capitalização foram tratadas de forma case-insensitive. O identificador `id_registro` foi interpretado conforme o dicionário da planilha, como identificador didático, não como código oficial.

### Modeling / Analysis

Foi utilizada análise descritiva e comparação cruzada entre os critérios de acesso documentados no PDF e os campos cadastrais da planilha.

### Evaluation

Os resultados foram conferidos por cálculo independente e por validação das orientações nas páginas oficiais do Conecta Recife. A avaliação também considerou as limitações explicitadas nos próprios documentos.

### Deployment

A principal proposta de aplicação é incorporar uma camada de orientação personalizada ao aplicativo, separando dados cadastrais da unidade de regras de acesso e dados específicos do cidadão.

## 10. Engenharia de Prompt

A análise utiliza:

- Decomposição.
- Metaprompting.
- Encadeamento.
- Saída estruturada.
- Critérios de validação.
- Comparação.
- Refinamento iterativo.

O fluxo principal é:

```text
PDF de orientações
        ↓
Extração dos critérios de acesso
        ↓
Definição dos campos necessários
        ↓
Planilha de unidades
        ↓
Mapeamento campo × critério
        ↓
Cálculos
        ↓
Validação
        ↓
Achados
        ↓
Recomendação
```

## 11. Limitações

A análise não demonstra:

- disponibilidade de vagas;
- disponibilidade de profissionais em tempo real;
- agendamento concluído;
- elegibilidade individual completa;
- cobertura territorial individual de cada cidadão;
- funcionamento atual de cada unidade;
- efetividade de um telefone para agendamento.

Essas limitações são importantes porque o material didático alerta que informação presente no cadastro não prova, por si só, acesso ao serviço.

## 12. Referências

### Materiais da atividade

SENAC PERNAMBUCO. Faculdade Senac Pernambuco. **Engenharia de prompt avançada, aplicações em Data Science, PI Saúde na Palma da Mão**. Recife: Senac Pernambuco, 2026.

SENAC PERNAMBUCO. Faculdade Senac Pernambuco. **Plano de Ensino: Data Science, princípios e técnicas**. Recife: Senac Pernambuco, 2026.

RECIFE. Secretaria de Saúde. **Unidades de Saúde da Família, USF, e Unidades Básicas de Saúde, UBS**. Portal de Dados Abertos do Recife. Acesso em 8 set. 2026.

### CRISP-DM

CHAPMAN, Pete et al. **CRISP-DM 1.0: Step-by-step data mining guide**. SPSS, 2000.

### Engenharia de Prompt

ANTHROPIC. **Prompting best practices**. Anthropic Documentation. Acesso em 8 set. 2026.

BROWN, Tom B. et al. **Language models are few-shot learners**. Advances in Neural Information Processing Systems, v. 33, p. 1877-1901, 2020.

### Fontes oficiais do Conecta Recife

RECIFE. Secretaria de Saúde. **Buscar Minha Unidade de Saúde por Endereço, Onde posso ser atendido?** Conecta Recife. Acesso em 8 set. 2026.

RECIFE. Secretaria de Saúde. **Agendar consulta odontológica na atenção básica**. Conecta Recife. Acesso em 8 set. 2026.

RECIFE. Secretaria de Saúde. **Agendar consultas e procedimentos na Minha Unidade de Saúde**. Conecta Recife. Acesso em 8 set. 2026.

RECIFE. Secretaria de Saúde. **Falar com sua equipe de saúde pelo WhatsApp**. Conecta Recife. Acesso em 8 set. 2026.

## 13. Autoria

**Thayná Batista da Silva**

Análise e Desenvolvimento de Sistemas, Faculdade Senac de Pernambuco.

Unidade Curricular: `[TADS25.109/3N] DATA SCIENCE: PRINCÍPIOS E TÉCNICAS, 2026.2`