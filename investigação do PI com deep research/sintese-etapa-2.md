# Síntese da Etapa 2

## Recife Saudável, Data Science

### Problema validado

Existem evidências oficiais de filas, demora na marcação e dificuldades relacionadas ao acesso a consultas e serviços especializados no Recife.

### Evidências

1. [Diário Oficial do Recife, Resolução nº 016/2025](https://dome.recife.pe.gov.br/upload_dome/DO_066_31_05_2025-assinado.pdf)
2. [I Relatório Detalhado Quadrimestral de 2026, Prefeitura do Recife](https://transparencia.recife.pe.gov.br/uploads/pdf/I%20Relat%C3%B3rio%20Detalhado%20Quadrimestral%202026%20-%20vers%C3%A3o%20preliminar_19c2903852976f3b350bfd47ff45260b.pdf)
3. [Prefeitura do Recife, Regulação em Saúde](https://www2.recife.pe.gov.br/servico/regulacao-em-saude)

### Dataset verificado

**Consultas e Procedimentos de Saúde**

https://dados.recife.pe.gov.br/dataset/consultas-e-procedimentos-de-saude

**Unidades Especializadas**

https://dados.recife.pe.gov.br/dataset/unidades-especializadas

### Pergunta

> Quais especialidades e localidades concentram maior volume de consultas e como essa demanda se relaciona, de forma descritiva, com a distribuição das unidades especializadas disponíveis no Recife?

### CRISP-DM

**Business Understanding:** compreender o problema.

**Data Understanding:** conhecer as bases e suas limitações.

**Data Preparation:** limpar e padronizar.

**Modeling:** análise descritiva, agregações, rankings e visualizações.

**Evaluation:** verificar se os resultados respondem à pergunta.

**Deployment:** utilizar os achados para orientar a jornada digital de agendamento.

### Decisão

**AVANÇAR COM RESTRIÇÃO DE ESCOPO.**

### Restrição

Não utilizar os datasets selecionados para afirmar que:

- o aplicativo causará redução de filas;
- é possível prever o tempo individual de espera;
- é possível prever no-show;
- é possível realizar inferência clínica.

### Regra

> **Problema validado. Dataset existente. Variáveis suficientes para análise descritiva. Evidência insuficiente para previsão de filas.**
