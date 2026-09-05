# Investigação de Deep Research, Recife Saudável

## Identificação

**Unidade Curricular:** TADS25.109/3N, Data Science: Princípios e Técnicas, 2026.2  
**Instituição:** Faculdade Senac Pernambuco, Recife, PE  
**Curso:** Tecnólogo em Análise e Desenvolvimento de Sistemas  
**Professor:** Rodrigo Rios de Larrazábal  
**Projeto Integrador:** Saúde na Palma da Mão  
**Equipe:** Thayná Batista da Silva e Poliana Fontes  
**Data:** 05/09/2026

## 1. Objetivo da investigação

Transformar o briefing do Recife Saudável em um problema investigável de Data Science, identificar evidências rastreáveis, verificar datasets públicos adequados e registrar uma decisão metodológica conforme a atividade de Etapa 2.

## 2. Problema validado

### Formulação

O acesso a consultas e serviços especializados de saúde no Recife envolve etapas de encaminhamento, regulação e disponibilidade de vagas, com ocorrência documentada de filas e demora na marcação, indicando espaço para soluções digitais que reduzam o atrito da jornada e organizem melhor o acesso ao serviço.

### Evidência 1

O Conselho Municipal de Saúde do Recife registrou dificuldades relacionadas à Regulação e reclamações da população sobre demora na marcação de consultas e serviços especializados.

**Fonte:**  
https://dome.recife.pe.gov.br/upload_dome/DO_066_31_05_2025-assinado.pdf

### Evidência 2

O I Relatório Detalhado Quadrimestral de 2026 da Secretaria de Saúde do Recife registra o monitoramento de filas e informa, em 25/05/2026, mediana de espera de 193 dias para consultas, 159 dias para exames e 101 dias para cirurgias.

**Fonte:**  
https://transparencia.recife.pe.gov.br/uploads/pdf/I%20Relat%C3%B3rio%20Detalhado%20Quadrimestral%202026%20-%20vers%C3%A3o%20preliminar_19c2903852976f3b350bfd47ff45260b.pdf

### Evidência 3

A Prefeitura do Recife descreve o acesso à atenção especializada mediante unidades de referência e Central de Regulação, com agendamento conforme disponibilidade de vagas.

**Fontes:**
- https://www2.recife.pe.gov.br/servico/regulacao-em-saude
- https://conecta.recife.pe.gov.br/

### Conclusão

**Problema validado.**

A pesquisa sustenta a existência de uma questão real de acesso, espera e organização da demanda.

Não há evidência suficiente para afirmar que o uso de um aplicativo, sozinho, reduzirá filas. Essa relação deve ser tratada como hipótese.

## 3. Datasets verificados

### Dataset A

**Consultas e Procedimentos de Saúde**

Fonte oficial:

https://dados.recife.pe.gov.br/dataset/consultas-e-procedimentos-de-saude

Descrição oficial: totais de consultas e procedimentos de saúde realizados por tipo, especialidade e localidade.

Variáveis relevantes:

- `especialidade`
- `consultas`
- `procedimentos`
- `usf`
- `endereco`
- `periodo`
- `tipo`
- `atencao`

### Dataset B

**Unidades Especializadas**

Fonte oficial:

https://dados.recife.pe.gov.br/dataset/unidades-especializadas

Variáveis relevantes:

- `nome_oficial`
- `rpa`
- `distrito_sanitario`
- `microregiao`
- `cnes`
- `tipo_servico`
- `endereço`
- `bairro`
- `servico`
- `especialidade`
- `como_usar`
- `horario`
- `latitude`
- `longitude`

### Validação

| Critério | Resultado |
|---|---|
| Base pública existente | Sim |
| Fonte oficial | Sim |
| Contexto Recife | Sim |
| Especialidade | Sim |
| Volume de consultas | Sim |
| Localização | Sim |
| Horários | Sim, parcialmente |
| Fila individual | Não |
| Tempo individual de espera | Não |
| No-show | Não |
| Análise descritiva | Sim |
| Previsão de espera | Não suportada atualmente |

## 4. Pergunta de Data Science

> Quais especialidades e localidades concentram maior volume de consultas e como essa demanda se relaciona, de forma descritiva, com a distribuição das unidades especializadas disponíveis no Recife?

## 5. Hipótese

A demanda por serviços especializados está distribuída de maneira desigual entre especialidades e localidades, permitindo identificar concentrações de demanda e apoiar decisões sobre organização da jornada digital de agendamento.

## 6. Decisão

### AVANÇAR COM RESTRIÇÃO DE ESCOPO

A equipe pode avançar com análise exploratória e descritiva.

O escopo não contempla, nesta etapa:

- previsão individual de tempo de espera;
- previsão de no-show;
- diagnóstico;
- decisão clínica;
- inferência sobre condições médicas individuais;
- afirmação causal de que o aplicativo reduzirá filas.

## 7. Conclusão metodológica

Os dados disponíveis atendem ao objetivo de investigar a distribuição da demanda e da oferta de serviços especializados.

Para ampliar a análise para previsão de filas ou no-show seriam necessárias outras variáveis e uma nova avaliação da qualidade, granularidade, temporalidade e completude dos dados.

## 8. Fontes consultadas

- OpenAI, Deep Research: https://developers.openai.com/api/docs/guides/deep-research
- OpenAI, Prompting: https://learn.chatgpt.com/docs/prompting
- IBM, CRISP-DM: https://public.dhe.ibm.com/software/analytics/spss/documentatiom/modeler/17.1/br_po/ModelerCRISPDM.pdf
- Prefeitura do Recife, Regulação em Saúde: https://www2.recife.pe.gov.br/servico/regulacao-em-saude
- Portal de Dados Abertos, Consultas e Procedimentos: https://dados.recife.pe.gov.br/dataset/consultas-e-procedimentos-de-saude
- Portal de Dados Abertos, Unidades Especializadas: https://dados.recife.pe.gov.br/dataset/unidades-especializadas
- Diário Oficial do Recife: https://dome.recife.pe.gov.br/upload_dome/DO_066_31_05_2025-assinado.pdf
- Transparência Recife: https://transparencia.recife.pe.gov.br/
