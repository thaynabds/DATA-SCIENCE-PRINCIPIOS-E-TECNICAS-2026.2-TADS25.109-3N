# Análise Completa, Saúde Recife

## SEÇÃO 1: RESUMO EXECUTIVO

### Pergunta analítica

Quais informações presentes no cadastro de unidades são suficientes para orientar o cidadão sobre sua unidade de referência e o caminho de acesso a serviços de saúde, quando comparadas às regras apresentadas no Conecta Recife?

### Hipótese verificável

H1: o cadastro, isoladamente, não contém todas as informações necessárias para orientar o acesso de forma confiável, porque registra atributos das unidades, mas não representa integralmente critérios dependentes do cidadão, como endereço residencial, cobertura territorial, requisitos de acesso digital, vínculo com equipe e disponibilidade de atendimento.

### Achado 1

A planilha possui 153 registros, sendo 131 USF e 22 UBS. O cadastro apresenta endereço, bairro, horário, telefone, especialidades e orientação de uso. Entretanto, o campo `endereço` representa a localização da unidade, enquanto o PDF indica que a unidade de referência pode depender do endereço residencial do cidadão.

A planilha, portanto, descreve unidades, mas não permite, isoladamente, determinar a unidade de referência de um cidadão específico.

### Achado 2

138 dos 153 registros possuem odontologia no campo `especialidade`, equivalendo a 90,20%. Porém, a orientação oficial para odontologia diferencia o atendimento de pessoas cobertas por equipe de Saúde da Família daquele destinado a pessoas sem essa cobertura.

Logo, presença de odontologia no cadastro não deve ser interpretada como autorização para o cidadão escolher qualquer unidade, nem como prova de vaga ou agendamento.

### Recomendação

Adicionar ao aplicativo uma etapa de identificação personalizada da unidade de referência, combinando endereço residencial, regras de cobertura e vínculo com equipe. A interface deve separar claramente dados da unidade, regras de acesso e disponibilidade de agenda.

---

# SEÇÃO 2: REGISTRO CRISP-DM E ANÁLISE TÉCNICA

## 2.1 Business Understanding

O problema de negócio é avaliar se o cadastro de unidades de saúde oferece informações suficientes para apoiar uma orientação confiável de acesso aos serviços do Saúde Recife.

A pergunta proposta pela atividade é: “O cadastro permite orientar o acesso?”.

O ponto central é distinguir informação cadastral de informação de acesso. O material didático alerta expressamente que horário de funcionamento não comprova canal de agendamento, elegibilidade ou disponibilidade de consulta.

## 2.2 Data Understanding

Foram examinados:

1. `01_Cadastro_Unidades_Saude_Recife.xlsx`.
2. `02_Orientacoes_Acesso_Saude_Recife.pdf`.
3. `Aula_Prompts_Data_Science_PI_Saude_SENAC.pdf`.

A planilha contém quatro abas:

- `Leia_me`
- `Cadastro`
- `Dicionario`
- `Fontes`

A aba `Cadastro` possui 153 registros e 11 campos:

`id_registro`, `origem`, `nome_oficial`, `horario`, `como_usar`, `especialidade`, `endereço`, `bairro`, `fone`, `cnes`, `fonte_url`.

Distribuição da origem:

| Origem | Registros |
|---|---:|
| USF | 131 |
| UBS | 22 |
| Total | 153 |

O campo `horario` possui três representações textuais:

| Horário | Registros |
|---|---:|
| segunda a sexta 08:00 às 17:00 | 127 |
| SEGUNDA A SEXTA 08:00 ÀS 17:00 | 22 |
| 24h | 4 |

As duas primeiras representam a mesma informação com diferença de capitalização.

O campo `como_usar` apresenta duas variantes que diferem essencialmente pela capitalização. Todos os 153 registros contêm a orientação de residência em área de cobertura e cadastro prévio.

## 2.3 Data Preparation

Os valores originais foram preservados.

Tratamentos analíticos:

1. Diferenças de capitalização foram consideradas equivalentes para contagens semânticas.
2. O campo `id_registro` foi tratado como identificador didático, conforme o dicionário.
3. O campo `endereço` foi interpretado como endereço da unidade, não como endereço residencial.
4. O campo `horario` foi interpretado como horário cadastral, não como agenda.
5. O campo `especialidade` foi utilizado para verificar presença declarada de odontologia.
6. Não foram preenchidas lacunas com inferências externas.
7. O campo `fone` possui um valor vazio, preservado conforme a planilha.

## 2.4 Data Analysis

### Análise da adequação para orientar acesso

O PDF informa quatro grupos de condições relevantes:

1. A unidade de referência pode depender do endereço residencial.
2. O caminho pode mudar conforme cobertura por equipe de Saúde da Família.
3. A marcação digital possui requisitos específicos.
4. O canal de contato pelo WhatsApp exige cadastro e vínculo específicos.

A planilha oferece endereço da unidade, especialidades, horário, telefone e texto de utilização. Porém, não possui campos específicos para:

- endereço residencial do cidadão;
- cobertura individual;
- vínculo do cidadão com equipe;
- CPF;
- Cartão SUS;
- comprovante de residência;
- senha do Conecta Recife;
- elegibilidade individual;
- agenda ou vagas em tempo real.

Isso demonstra uma diferença entre cadastro da rede e mecanismo de orientação personalizada.

## 2.5 Conferência de cálculo

Critério definido antes da contagem:

> considerar o registro como positivo quando o campo `especialidade`, tratado sem distinção entre maiúsculas e minúsculas, contém a expressão relacionada a odontologia.

Resultado:

- total avaliado: 153;
- positivos: 138;
- negativos: 15.

Cálculo:

`138 / 153 × 100 = 90,196078...`

Arredondamento para duas casas:

**90,20%**

A conta está correta.

Importante: 90,20% significa apenas que odontologia aparece no cadastro de 138 registros. Não significa que 90,20% das unidades tenham vaga, que 90,20% possam receber qualquer cidadão ou que seja possível agendar em qualquer uma delas.

## 2.6 Conferência da orientação

Foi conferida a orientação de que a busca da unidade pode utilizar o endereço residencial.

A página oficial consultada descreve o serviço “Buscar Minha Unidade de Saúde por Endereço” e orienta o cidadão a informar o endereço de sua residência.

Também foi conferida a orientação odontológica. A página oficial informa caminhos diferentes para pessoas cobertas e não cobertas por equipe de Saúde da Família. No caminho digital, orienta o acesso ao Conecta Recife, escolha do serviço odontológico e seleção de profissional, dia e horário.

A orientação presente no PDF está, portanto, coerente com as páginas oficiais consultadas em 8 de setembro de 2026.

## 2.7 Avaliação

A hipótese é sustentada pelos dados.

O cadastro é útil para identificar características declaradas das unidades, mas não possui, sozinho, todas as variáveis necessárias para orientar o acesso individualizado.

Conclusão controlada:

> **O cadastro permite apoiar a orientação, mas não permite, isoladamente, determinar o acesso individual do cidadão.**

---

# SEÇÃO 3: ENGENHARIA DE PROMPT

## 3.1 Prompt inicial

```text
Analise os arquivos fornecidos sobre o Saúde Recife, incluindo a planilha de cadastro de unidades e o PDF de orientações de acesso.

Responda à pergunta: “O cadastro permite orientar o acesso?”

Formule uma pergunta analítica e uma hipótese verificável. Identifique as informações presentes na planilha que ajudam a orientar o acesso e compare com as orientações do PDF.

Apresente os principais achados, faça pelo menos um cálculo usando os dados da planilha e proponha uma melhoria para o aplicativo.

Não invente informações que não estejam nos arquivos.
```

## 3.2 Metaprompt aplicado

```text
Atue como revisor de prompts para uma análise de Data Science.

Analise o prompt inicial considerando:
1. objetivo;
2. entradas disponíveis;
3. informações ausentes;
4. ambiguidades;
5. restrições;
6. riscos de inferência indevida;
7. critérios de qualidade;
8. necessidade de validação numérica;
9. necessidade de rastreabilidade entre fonte e conclusão;
10. formato de saída.

Identifique o que precisa ser acrescentado para impedir que horário, especialidade, telefone ou endereço da unidade sejam interpretados como prova de elegibilidade, agendamento ou disponibilidade.

Depois produza uma versão revisada do prompt.

A versão revisada deve:
- usar o PDF para extrair primeiro os critérios de acesso;
- usar esses critérios como referência para analisar a planilha;
- comparar campo por campo;
- separar evidência, hipótese e inferência;
- definir o critério antes de qualquer proporção;
- conferir o cálculo;
- validar uma orientação do PDF contra sua fonte oficial, quando possível;
- apresentar exatamente dois achados;
- registrar limitações;
- recomendar uma melhoria viável;
- preservar a rastreabilidade;
- não inventar dados, fontes ou disponibilidade.
```

## 3.3 Prompt refinado com encadeamento

```text
<objetivo>
Investigar se o cadastro de unidades do Saúde Recife contém informações suficientes
para apoiar a orientação de acesso aos serviços.
</objetivo>

<fontes>
Fonte A: PDF de orientações de acesso do Saúde Recife.
Fonte B: planilha de cadastro de unidades de saúde.
Fonte C: fontes oficiais do Conecta Recife indicadas no PDF, quando usadas para validação.
</fontes>

<etapa_1_pdf>
Leia primeiro o PDF.

Extraia somente critérios explicitamente relacionados a:
- unidade de referência;
- endereço residencial;
- cobertura por equipe;
- requisitos de agendamento;
- requisitos de acesso digital;
- canais de contato;
- condições de atendimento.

Para cada critério, registre:
critério, serviço, evidência textual resumida, fonte e nível de abrangência.
</etapa_1_pdf>

<etapa_2_planilha>
Depois leia a planilha.

Use a saída da etapa 1 como referência.
Mapeie cada critério para os campos existentes na planilha.

Classifique cada critério como:
- atendido;
- parcialmente atendido;
- não representado.

Não trate endereço da unidade como endereço residencial.
Não trate horário cadastral como agenda.
Não trate especialidade como disponibilidade.
Não trate telefone como prova de agendamento.
</etapa_2_planilha>

<etapa_3_hipotese>
Formule uma pergunta analítica clara e uma hipótese verificável.
</etapa_3_hipotese>

<etapa_4_calculo>
Defina explicitamente o critério antes da contagem.
Faça um cálculo proporcional usando a fórmula:

registros que atendem ao critério / registros avaliados × 100.

Mostre numerador, denominador, fórmula e resultado.
Confirme o resultado por uma segunda forma de contagem.
</etapa_4_calculo>

<etapa_5_validacao>
Valide uma orientação do PDF na fonte oficial correspondente, se disponível.
Separe claramente:
- evidência da fonte;
- resultado calculado;
- interpretação;
- limitação.
</etapa_5_validacao>

<etapa_6_saida>
Entregue:
1. pergunta analítica;
2. hipótese;
3. exatamente dois achados;
4. cálculo conferido;
5. orientação conferida;
6. recomendação de melhoria;
7. limitações;
8. conclusão.

Não invente dados.
Não transforme informação cadastral em prova de acesso.
Não confunda presença de serviço com disponibilidade.
Mantenha rastreabilidade para cada conclusão.
</etapa_6_saida>
```

## 3.4 Encadeamento técnico

O encadeamento aplicado é:

```text
PDF
↓
Critérios de acesso
↓
Matriz de critérios necessários
↓
Planilha
↓
Mapeamento dos campos disponíveis
↓
Classificação das lacunas
↓
Cálculo
↓
Validação da orientação
↓
Achados
↓
Recomendação
```

Essa abordagem segue o material da aula, que define prompt chaining como uma sequência em que a saída de uma etapa alimenta a etapa seguinte.

## 3.5 Comparação

A comparação deve ser interpretada com uma ressalva metodológica: não foi fornecido um log independente de duas execuções do modelo. Portanto, a comparação abaixo é uma comparação controlada entre o resultado produzido pelo prompt direto e o resultado esperado pelo prompt refinado, e não uma medição estatística de duas execuções.

### Resultado do prompt inicial

O prompt inicial consegue localizar informações importantes, como endereço, horário, especialidades e regras gerais. Porém, sem uma matriz explícita de critérios, existe maior risco de concluir que a existência de uma especialidade ou horário significa possibilidade de acesso.

### Resultado do prompt refinado

O prompt refinado obriga o processo a:

1. extrair primeiro as regras do PDF;
2. usar as regras como critérios de comparação;
3. separar endereço da unidade de endereço residencial;
4. separar especialidade de disponibilidade;
5. validar o cálculo;
6. validar uma orientação na fonte oficial;
7. registrar limitações.

### Mudança concreta após o refinamento

A mudança mais importante é a inclusão da regra:

> **“Não trate especialidade como disponibilidade.”**

Isso transforma a análise de uma simples descrição da planilha em uma comparação entre requisitos de acesso e evidências efetivamente presentes no cadastro.

Outra mudança concreta é a exigência de verificar o critério antes da proporção. Isso reduz o risco de apresentar percentuais sem definir o universo e o significado da contagem.

---

# SEÇÃO 4: CONCLUSÃO

A resposta à pergunta “O cadastro permite orientar o acesso?” é:

**Parcialmente.**

O cadastro permite apoiar a orientação porque contém informações úteis sobre unidades, como localização, horário, especialidades, telefone e tipo de unidade. Porém, não é suficiente para determinar individualmente a unidade de referência e o caminho de acesso do cidadão.

A principal lacuna é a ausência, na estrutura analisada, de informações que dependem do cidadão e das regras de cobertura. Por isso, a solução recomendada é integrar o cadastro da rede com uma camada de regras de acesso e dados cadastrais do usuário, mantendo separadas as informações cadastrais, as regras de elegibilidade e a disponibilidade de agenda.

## 👩‍💻 Autora

<div align="center">

### Thayná Batista da Silva

<a href="https://br.linkedin.com/in/thaynabds" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
</a>
<a href="https://www.instagram.com/thaynabdstec/" target="_blank">
  <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" />
</a>
<a href="mailto:thaynabdstec@gmail.com">
  <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
</a>

📧 thaynabdstec@gmail.com · 📱 +55 (81) 97912-6121

Estudante de **Análise e Desenvolvimento de Sistemas** — Faculdade Senac Recife · Previsão de formatura: 2027

<br/>

<img src="https://raw.githubusercontent.com/thaynabds/AppMedSmart/refs/heads/main/Cart%C3%A3o%20TEC%20Thayn%C3%A1%20Batista%20da%20Silva.png" alt="Cartão TEC Thayná Batista da Silva" />

</div>

---

<div align="center">

Feito com 💜 por **Thayná Batista da Silva** para o **A Unidade Curricular [TADS25.109/3N] DATA SCIENCE: PRINCÍPIOS E TÉCNICAS - 2026.2 da Faculdade Senac Recife-PE, Tecnólogo em Análise e Desenvolvimento de Sistemas, 2026.2, Professor Rodrigo Rios de Larrazábal**

**Copyright © 2026 — ThaynaBDSTec - Todos os direitos reservados.**

</div>
