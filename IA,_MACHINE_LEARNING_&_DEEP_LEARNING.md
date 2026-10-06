# IA, Machine Learning & Deep Learning — Recife Saudável

## 1. Contexto

**Projeto:** Recife Saudável — Saúde na Palma da Mão  
**Unidade Curricular:** Data Science: Princípios e Técnicas — 2026.2  
**Alunas:** Thayná Batista da Silva e Polyana Fontes  
**Instituição:** Faculdade Senac de Pernambuco

A atividade solicita retomar o problema e o dataset já investigados, escolher uma tarefa do Projeto Integrador e propor uma abordagem entre **automação, IA sem ML, ML sem DL ou DL**. Também solicita explicar entrada, funcionamento e saída, pedir uma crítica a uma IA, conferir essa crítica com a aula e registrar o que foi aceito, corrigido ou descartado, além de apresentar dados, teste e decisão.

## 2. Tarefa escolhida

### Automatização da validação e do registro de consultas

A tarefa escolhida é automatizar o fluxo de agendamento de consultas existente no Recife Saudável.

A proposta não tenta diagnosticar o paciente nem tomar uma decisão clínica. O objetivo é executar automaticamente regras administrativas e funcionais do agendamento.

## 3. Abordagem escolhida

**Abordagem: Automação convencional.**

A aula diferencia automação convencional de automação com IA. Na automação convencional, são executadas rotinas previamente definidas. Portanto, uma tarefa não precisa utilizar Machine Learning ou Deep Learning apenas por ser automatizada.

Essa escolha é compatível com o problema, com os dados disponíveis e com o escopo acadêmico do projeto.

## 4. Entrada, funcionamento e saída

### Entrada

- paciente autenticado;
- especialidade escolhida;
- profissional;
- data;
- horário;
- dados necessários para concluir o agendamento.

### Funcionamento

1. validar os campos obrigatórios;
2. verificar se a especialidade é válida;
3. verificar se o profissional está associado à especialidade;
4. consultar a disponibilidade;
5. verificar se o horário continua livre;
6. registrar o agendamento;
7. impedir conflito de horário;
8. retornar o resultado ao paciente.

### Saída

- **Sucesso:** consulta registrada e confirmação apresentada.
- **Erro:** agendamento não realizado, com mensagem informativa sobre a validação que falhou.

## 5. Compatibilidade com o protótipo

A proposta aproveita o fluxo já previsto no protótipo: seleção de especialidade, consulta de disponibilidade, escolha de profissional, data e horário e confirmação do agendamento.

Assim, não é necessário criar uma nova funcionalidade de IA no Figma para atender esta atividade. A automação fica no comportamento do sistema por trás das telas existentes.

Também não é necessário adicionar seleção pública de perfil. O fluxo permanece centrado no paciente.

## 6. Dados disponíveis e dados faltantes

### Dados disponíveis ou utilizáveis no projeto

- unidades e serviços;
- especialidades;
- profissionais;
- informações de disponibilidade necessárias ao protótipo;
- datas e horários de atendimento;
- dados fictícios de pacientes para demonstração;
- dados cadastrais utilizados pelo fluxo de agendamento.

O dataset anteriormente investigado também possui informações de unidades, especialidades, serviços, períodos, endereços, bairros, RPA, distrito, horários e localização.

### Dados que seriam necessários para Machine Learning

Para treinar e avaliar um modelo de previsão ou recomendação seriam necessários dados históricos compatíveis com a tarefa, por exemplo:

- histórico de agendamentos;
- horários solicitados e efetivamente utilizados;
- cancelamentos;
- faltas;
- reagendamentos;
- demanda histórica por especialidade;
- resultados reais associados aos registros.

Esses dados não estão disponíveis em quantidade e estrutura suficientes para justificar um modelo de ML neste MVP.

O dataset investigado também não contém, por si só, histórico individual de filas, tempo individual de espera, faltas ou dados clínicos suficientes para construir uma previsão individual desse tipo.

## 7. Teste da proposta

A avaliação da automação será funcional, verificando se as regras são executadas corretamente.

| Caso | Entrada | Resultado esperado |
|---|---|---|
| 1 | Horário disponível | Agendamento confirmado |
| 2 | Horário ocupado | Agendamento recusado |
| 3 | Profissional incompatível com a especialidade | Agendamento recusado |
| 4 | Campo obrigatório ausente | Erro de validação |
| 5 | Dados válidos e horário livre | Consulta registrada |

O teste não mede acurácia de Machine Learning porque não existe um modelo treinado. Ele verifica se a automação produz o comportamento definido pelas regras.

## 8. Crítica solicitada à IA

A crítica realizada sobre a proposta indicou que utilizar ML ou DL apenas para tornar o projeto mais sofisticado aumentaria a complexidade sem resolver uma necessidade demonstrada.

Também foi apontado que ML exige dados históricos adequados e uma forma de avaliar o desempenho em casos que não participaram do treinamento. A aula reforça que acertar o treinamento não é suficiente: o modelo deve ser avaliado em novos casos.

### O que foi aceito

- a escolha da abordagem deve considerar a tarefa e os dados disponíveis;
- ML depende de dados compatíveis com a tarefa;
- a avaliação precisa sustentar a escolha;
- uma tarefa mais complexa não exige automaticamente Deep Learning;
- a automação convencional é suficiente para regras determinísticas de agendamento.

### O que foi corrigido

A proposta inicial de utilizar Machine Learning para recomendar opções de atendimento foi substituída por automação convencional, porque não havia dados históricos e rotulados suficientes para sustentar o treinamento e a avaliação de um modelo.

### O que foi descartado

- treinamento de ML com dados inventados;
- utilização de Deep Learning sem necessidade;
- criação de uma funcionalidade de diagnóstico ou decisão clínica;
- inclusão de uma tela artificial de IA apenas para cumprir a atividade.

## 9. Decisão final

| Abordagem | Decisão | Motivo |
|---|---|---|
| Automação convencional | **Escolhida** | Resolve a tarefa com regras definidas e é compatível com o protótipo |
| IA sem ML | Não escolhida para o MVP | Não há necessidade de raciocínio adicional para a tarefa |
| ML sem DL | Futuro | Poderia ser estudado com histórico suficiente e uma pergunta preditiva bem definida |
| Deep Learning | Descartada | Não há tarefa nem dados que justifiquem redes neurais profundas |

Portanto, a decisão final para o MVP é implementar **automação convencional no agendamento**.

Uma futura versão poderia estudar Machine Learning para tarefas como previsão de demanda, risco de cancelamento ou identificação de períodos de maior procura, desde que existam dados históricos adequados, critérios de avaliação e governança dos dados.

## 10. Limites da solução

A automação proposta não:

- diagnostica doenças;
- prescreve tratamentos;
- altera medicamentos;
- substitui profissionais de saúde;
- decide prioridade clínica;
- realiza triagem clínica automatizada;
- prevê o estado de saúde do paciente.

A pré-triagem continua sendo uma etapa informativa para organizar e preparar o atendimento.

## 11. Relação com a aula

A proposta segue os critérios apresentados na aula: a pergunta/tarefa deve orientar o método, os dados precisam ser compatíveis com a tarefa e a escolha deve possuir uma avaliação que sustente a decisão.

A aula também apresenta que IA é um campo abrangente, ML trabalha com aprendizado a partir de dados ou experiências e DL é uma parte de ML baseada em redes neurais profundas. Ela ressalta ainda que nem toda automação utiliza IA.

## 12. Conclusão

Para o escopo atual do Recife Saudável, a automação convencional é a alternativa mais coerente. Ela atende diretamente ao fluxo de agendamento já definido, pode ser implementada com regras determinísticas e permite uma avaliação funcional objetiva.

ML e DL não serão utilizados apenas por serem tecnologias mais complexas. A adoção futura dessas abordagens dependerá de uma tarefa que realmente exija aprendizado e da existência de dados adequados para treinamento e avaliação.

## Referência principal da atividade

Slides da unidade curricular **Data Science: Princípios e Técnicas — IA, Machine Learning & Deep Learning**, Professor Rodrigo Rios, 2026.2.
