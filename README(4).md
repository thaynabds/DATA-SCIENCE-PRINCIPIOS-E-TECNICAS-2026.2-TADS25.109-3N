# Recife Saudável

> **Atividade de Investigação do Projeto Integrador com Deep Research**
>
> **Unidade Curricular:** [TADS25.109/3N] Data Science: Princípios e Técnicas, 2026.2  
> **Curso:** Tecnólogo em Análise e Desenvolvimento de Sistemas  
> **Instituição:** Faculdade Senac Pernambuco, Recife, PE  
> **Professor:** Rodrigo Rios de Larrazábal  
> **Projeto Integrador:** Saúde na Palma da Mão  
> **Equipe:** Thayná Batista da Silva e Poliana Fontes

---

## Índice

- [Sobre a atividade](#sobre-a-atividade)
- [Equipe](#equipe)
- [Projeto Recife Saudável](#projeto-recife-saudável)
- [Etapa 2, Investigação](#etapa-2-investigação)
- [Problema validado](#problema-validado)
- [Datasets verificados](#datasets-verificados)
- [Pergunta de Data Science](#pergunta-de-data-science)
- [Prompt CRISP-DM](#prompt-crisp-dm)
- [Decisão registrada](#decisão-registrada)
- [Síntese para apresentação](#síntese-para-apresentação)
- [Documentação](#documentação)
- [Links do projeto](#links-do-projeto)
- [Referências](#referências)
- [Autoria e equipe](#autoria-e-equipe)

---

## Sobre a atividade

Esta entrega registra a **Etapa 2, Do plano de trabalho à investigação**, da atividade de Data Science do Projeto Integrador.

A investigação foi estruturada para responder aos quatro produtos exigidos pela atividade:

1. **1 problema validado**, sustentado por evidências rastreáveis.
2. **1 dataset verificado**, com análise de aderência ao contexto.
3. **1 prompt CRISP-DM**, com objetivo, contexto, saída, limites e verificação.
4. **1 decisão registrada**, indicando se a equipe pode avançar ou precisa revisar o problema.

> **Regra metodológica:** sem fonte, não há evidência. Sem dataset, não há análise. Sem verificação, não há avanço.

---

## Equipe

| Integrante | Atuação no projeto |
|---|---|
| **Thayná Batista da Silva** | Scrum Master, Product Designer, Requirements Analyst e Developer |
| **Poliana Fontes** | Desenvolvedora Full Stack, Modelagem de Banco de Dados e Documentação Técnica |

As integrantes **Thayná Batista da Silva e Poliana Fontes** realizaram esta investigação como equipe.

---

## Projeto Recife Saudável

O **Recife Saudável** é um projeto acadêmico de aplicativo centrado no paciente, desenvolvido no contexto do Projeto Integrador **Saúde na Palma da Mão**.

O MVP tem como objetivo apoiar:

- cadastro e autenticação do paciente;
- pré-triagem informativa em quatro etapas;
- consulta de especialidades e profissionais;
- consulta de disponibilidade;
- agendamento de consultas;
- gerenciamento das marcações;
- experiência acessível e simplificada.

O aplicativo **não realiza diagnóstico médico, prescrição, ajuste de medicamentos ou decisão clínica automatizada**.

### Proposta de valor

> **“Reduza filas, retrabalho e tempo de espera com uma triagem digital simples, acessível e segura, que organiza a demanda e acelera o agendamento de consultas.”**

---

# Etapa 2, Investigação

## 1. Problema validado

### Problema investigado

> **O acesso a consultas e serviços especializados de saúde no Recife envolve etapas de encaminhamento, regulação e disponibilidade de vagas, com ocorrência documentada de filas e demora na marcação, indicando espaço para soluções digitais que reduzam o atrito da jornada e organizem melhor o acesso ao serviço.**

### Evidência 1, demora na marcação

O Conselho Municipal de Saúde do Recife registrou dificuldades relacionadas à Regulação e reclamações da população sobre demora na marcação de consultas e serviços especializados.

Fonte oficial:

- [Diário Oficial do Recife, Resolução nº 016/2025](https://dome.recife.pe.gov.br/upload_dome/DO_066_31_05_2025-assinado.pdf)

### Evidência 2, filas e tempo de espera

Documento oficial da Secretaria de Saúde do Recife registra o monitoramento de filas de consultas, exames e cirurgias e informa, em 25/05/2026, mediana de espera de **193 dias para consultas**, **159 dias para exames** e **101 dias para cirurgias**.

Fonte oficial:

- [I Relatório Detalhado Quadrimestral de 2026, Prefeitura do Recife](https://transparencia.recife.pe.gov.br/uploads/pdf/I%20Relat%C3%B3rio%20Detalhado%20Quadrimestral%202026%20-%20vers%C3%A3o%20preliminar_19c2903852976f3b350bfd47ff45260b.pdf)

### Evidência 3, complexidade do processo de acesso

A Prefeitura do Recife descreve o acesso à atenção especializada por meio das unidades de referência e da Central de Regulação, com agendamento condicionado à disponibilidade de vagas.

Fonte oficial:

- [Prefeitura do Recife, Regulação em Saúde](https://www2.recife.pe.gov.br/servico/regulacao-em-saude)
- [Conecta Recife, serviços de saúde](https://conecta.recife.pe.gov.br/)

### Conclusão

**Problema validado.**

As evidências oficiais sustentam a existência de dificuldades de acesso, filas, demora e complexidade de regulação.

**Limitação:** as evidências não provam, por si só, que um aplicativo reduzirá filas. Essa relação permanece como **hipótese de produto**, que deverá ser validada posteriormente.

---

# 2. Datasets verificados

Foram selecionadas duas bases oficiais do **Portal de Dados Abertos da Prefeitura do Recife**.

## Dataset A, Consultas e Procedimentos de Saúde

**Descrição:** totais de consultas e procedimentos de saúde realizados por tipo, especialidade e localidade.

- [Portal de Dados Abertos, Consultas e Procedimentos de Saúde](https://dados.recife.pe.gov.br/dataset/consultas-e-procedimentos-de-saude)
- [Recurso CSV, Consultas e Procedimentos, 2023](https://dados.recife.pe.gov.br/dataset/consultas-e-procedimentos-de-saude)

Principais campos relevantes:

| Campo | Utilidade |
|---|---|
| `especialidade` | análise por especialidade |
| `consultas` | volume de consultas |
| `procedimentos` | volume de procedimentos |
| `usf` | unidade |
| `endereco` | localização |
| `periodo` | dimensão temporal |
| `tipo` | classificação do atendimento |
| `atencao` | tipo de atenção |

O conjunto é mantido pela **Secretaria de Saúde** e pelo **EMPREL** e possui frequência de atualização anual.

## Dataset B, Unidades Especializadas

**Descrição:** unidades destinadas à atenção especializada, incluindo serviços e especialidades médicas e não médicas.

- [Portal de Dados Abertos, Unidades Especializadas](https://dados.recife.pe.gov.br/dataset/unidades-especializadas)
- [Recurso CSV, Unidades Especializadas](https://dados.recife.pe.gov.br/dataset/unidades-especializadas)

Principais campos relevantes:

| Campo | Utilidade |
|---|---|
| `nome_oficial` | identificação da unidade |
| `rpa` | Região Político Administrativa |
| `distrito_sanitario` | distrito sanitário |
| `microregiao` | microrregião |
| `cnes` | identificação do estabelecimento |
| `tipo_servico` | tipo de serviço |
| `endereço` | localização |
| `bairro` | localização |
| `servico` | serviço ofertado |
| `especialidade` | especialidade |
| `como_usar` | orientação para utilização |
| `horario` | horário |
| `latitude` | latitude |
| `longitude` | longitude |

A página oficial informa atualização em **06/03/2026** e frequência de atualização semestral.

---

## Verificação da adequação dos datasets

| Critério | Resultado | Avaliação |
|---|---|---|
| A base existe? | **Sim** | Bases oficiais do Portal de Dados Abertos do Recife |
| Cobre o contexto? | **Sim** | Dados da rede de saúde do Recife |
| Possui especialidade? | **Sim** | Campo `especialidade` |
| Possui volume de consultas? | **Sim** | Dataset de consultas e procedimentos |
| Possui localização? | **Sim** | Unidade, endereço, bairro, RPA e distrito |
| Possui horários? | **Sim, parcialmente** | Dataset de unidades especializadas |
| Possui fila individual? | **Não** | Não identificada como variável pública nas bases selecionadas |
| Possui tempo individual de espera? | **Não** | Não disponível no nível individual |
| Possui no-show? | **Não** | Não identificado |
| Permite análise descritiva? | **Sim** | Variáveis suficientes para agregações e comparações |
| Permite previsão confiável de fila? | **Não, atualmente** | Ausência de variáveis individuais e temporais suficientes |

### Resultado

**Dataset verificado com restrição metodológica.**

As bases permitem análise exploratória e descritiva da relação entre **demanda, especialidade, unidade e localização**.

Elas não sustentam, atualmente, afirmações robustas de previsão de:

- tempo individual de espera;
- no-show;
- probabilidade clínica;
- redução de filas causada pelo aplicativo.

---

# 3. Pergunta de Data Science

> **Quais especialidades e localidades concentram maior volume de consultas e como essa demanda se relaciona, de forma descritiva, com a distribuição das unidades especializadas disponíveis no Recife?**

### Hipótese

> A demanda por serviços especializados está distribuída de maneira desigual entre especialidades e localidades, permitindo identificar concentrações de demanda e apoiar decisões sobre organização da jornada digital de agendamento.

A hipótese deverá ser testada pelos dados.

---

# 4. Prompt CRISP-DM

O prompt completo está em:

- [`docs/prompt-crisp-dm.md`](docs/prompt-crisp-dm.md)

O prompt foi estruturado em:

1. Business Understanding.
2. Data Understanding.
3. Data Preparation.
4. Modeling.
5. Evaluation.
6. Deployment.

Também contém limites explícitos para impedir extrapolação dos dados e uso inadequado em decisões clínicas.

---

# 5. Decisão registrada

## **DECISÃO: AVANÇAR COM RESTRIÇÃO DE ESCOPO**

A equipe pode avançar porque:

- o problema possui evidências oficiais rastreáveis;
- existem datasets públicos oficiais;
- as variáveis selecionadas são adequadas para análise exploratória;
- o objetivo pode ser formulado sem utilizar dados reais de pacientes.

### Restrição

O projeto deverá permanecer no escopo de:

> **Análise descritiva da demanda e da oferta de serviços especializados no Recife, identificando concentração de consultas por especialidade e localidade e utilizando os resultados para apoiar decisões de organização da jornada de agendamento do Recife Saudável.**

---

# 6. Síntese para apresentação

### PROBLEMA VALIDADO

Há evidências oficiais de filas, demora na marcação e dificuldades de acesso a consultas especializadas no Recife.

### DATASET VERIFICADO

**Consultas e Procedimentos de Saúde, 2023**

[Portal de Dados Abertos do Recife](https://dados.recife.pe.gov.br/dataset/consultas-e-procedimentos-de-saude)

**Unidades Especializadas**

[Portal de Dados Abertos do Recife](https://dados.recife.pe.gov.br/dataset/unidades-especializadas)

### PERGUNTA

**Quais especialidades e localidades concentram maior demanda e como essa demanda se relaciona à distribuição das unidades especializadas?**

### MÉTODO

**CRISP-DM**

Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment.

### DECISÃO

**AVANÇAR**, utilizando análise descritiva.

### LIMITAÇÃO

Os datasets selecionados não possuem dados individualizados suficientes para previsão confiável de tempo de espera ou no-show.

---

# Documentação

- [`docs/investigacao-deep-research.md`](docs/investigacao-deep-research.md)
- [`docs/prompt-crisp-dm.md`](docs/prompt-crisp-dm.md)
- [`docs/datasets.md`](docs/datasets.md)
- [`docs/sintese-etapa-2.md`](docs/sintese-etapa-2.md)
- [`docs/referencias.md`](docs/referencias.md)

---

# Links do projeto

| Recurso | Link |
|---|---|
| YouTrack | https://grupotp.youtrack.cloud/articles/SPM |
| Drive | https://drive.google.com/drive/folders/1RgXpDg9M1NR0oKzka6owzkyy6r-ssMyG?usp=sharing |
| Figma | https://www.figma.com/make/HgsxSju4V0c9LixmfcUxm7/Saude-Recife-App-Development |
| GitHub | https://github.com/GrupoTP/App-Recife-Saudavel-Senac-PE-2026.2 |
| Notebook Gemini | https://notebook.google.com/notebook/9ad08a2a-b743-4e0a-aa1a-ba70398cd8ca |
| Relato de uso de IA | https://grupotp.youtrack.cloud/articles/SPM-A-8/Relatorio-de-Uso-de-IA |

---

# Referências

As referências foram mantidas com seus **links completos**, para permitir rastreabilidade da pesquisa.

## Pesquisa e Data Science

- [OpenAI, Deep Research](https://developers.openai.com/api/docs/guides/deep-research)
- [OpenAI, Prompting](https://learn.chatgpt.com/docs/prompting)
- [IBM, CRISP-DM](https://public.dhe.ibm.com/software/analytics/spss/documentatiom/modeler/17.1/br_po/ModelerCRISPDM.pdf)

## Saúde e Recife

- [Prefeitura do Recife, Regulação em Saúde](https://www2.recife.pe.gov.br/servico/regulacao-em-saude)
- [Portal de Dados Abertos do Recife, Consultas e Procedimentos de Saúde](https://dados.recife.pe.gov.br/dataset/consultas-e-procedimentos-de-saude)
- [Portal de Dados Abertos do Recife, Unidades Especializadas](https://dados.recife.pe.gov.br/dataset/unidades-especializadas)
- [Conecta Recife](https://conecta.recife.pe.gov.br/)
- [Diário Oficial do Recife, Resolução nº 016/2025](https://dome.recife.pe.gov.br/upload_dome/DO_066_31_05_2025-assinado.pdf)
- [Prefeitura do Recife, I Relatório Detalhado Quadrimestral de 2026](https://transparencia.recife.pe.gov.br/uploads/pdf/I%20Relat%C3%B3rio%20Detalhado%20Quadrimestral%202026%20-%20vers%C3%A3o%20preliminar_19c2903852976f3b350bfd47ff45260b.pdf)

## Legislação, privacidade e segurança

- [Planalto, Lei nº 13.709/2018, LGPD](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- [ANPD, Direitos dos Titulares](https://www.gov.br/anpd/pt-br/assuntos/titular-de-dados-1/direito-dos-titulares)
- [ANPD, RIPD](https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/relatorio-de-impacto-a-protecao-de-dados-pessoais-ripd)
- [Planalto, Lei nº 13.787/2018, prontuário do paciente](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13787.htm)

## Acessibilidade e tecnologia

- [W3C, WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [React Native, Accessibility](https://reactnative.dev/docs/accessibility)
- [MDN, Progressive Web Apps](https://developer.mozilla.org/pt-BR/docs/Web/Progressive_web_apps)
- [Spring, Building a RESTful Web Service](https://spring.io/guides/gs/rest-service/)
- [ANVISA, Software como Dispositivo Médico](https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/2022/software-como-dispositivo-medico-perguntas-e-respostas/)

---

# Autoria e equipe

## 👩‍💻 Thayná Batista da Silva

<div align="center">

<a href="https://br.linkedin.com/in/thaynabds" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
</a>
<a href="https://www.instagram.com/thaynabdstec/" target="_blank">
  <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" />
</a>
<a href="mailto:thaynabdstec@gmail.com">
  <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
</a>

**Atuação:** Scrum Master, Product Designer, Requirements Analyst e Developer.

</div>

## 👩‍💻 Poliana Fontes

<div align="center">

**Atuação:** Desenvolvedora Full Stack, Modelagem de Banco de Dados e Documentação Técnica.

</div>

---

<div align="center">

**Equipe Recife Saudável**

**Thayná Batista da Silva e Poliana Fontes**

Atividade acadêmica da Unidade Curricular **[TADS25.109/3N] Data Science: Princípios e Técnicas, 2026.2**  
Faculdade Senac Pernambuco, Recife, PE  
Professor: **Rodrigo Rios de Larrazábal**

**Copyright © 2026, ThaynaBDSTec, todos os direitos reservados.**

</div>
