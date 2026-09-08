# Prompts da Análise, Saúde Recife

## Prompt Inicial

Analise os arquivos fornecidos sobre o Saúde Recife, incluindo a planilha de cadastro de unidades e o PDF de orientações de acesso.

Responda à pergunta: “O cadastro permite orientar o acesso?”

Formule uma pergunta analítica e uma hipótese verificável. Identifique as informações presentes na planilha que ajudam a orientar o acesso e compare com as orientações do PDF.

Apresente os principais achados, faça pelo menos um cálculo usando os dados da planilha e proponha uma melhoria para o aplicativo.

Não invente informações que não estejam nos arquivos.

## Metaprompt

Atue como revisor de prompts para uma análise de Data Science.

Analise o prompt inicial considerando objetivo, entradas, informações ausentes, ambiguidades, restrições, riscos de inferência indevida, critérios de qualidade, necessidade de validação numérica, rastreabilidade entre fonte e conclusão e formato de saída.

Identifique o que precisa ser acrescentado para impedir que horário, especialidade, telefone ou endereço da unidade sejam interpretados como prova de elegibilidade, agendamento ou disponibilidade.

Produza uma versão revisada.

A versão revisada deve usar o PDF para extrair primeiro os critérios de acesso e depois usar esses critérios para analisar a planilha. Deve comparar campo por campo, separar evidência, hipótese e inferência, definir o critério antes de qualquer proporção, conferir o cálculo, validar uma orientação do PDF contra fonte oficial quando possível, apresentar exatamente dois achados, registrar limitações, recomendar uma melhoria viável e não inventar dados ou fontes.

## Prompt Refinado

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

Extraia somente critérios explicitamente relacionados a unidade de referência,
endereço residencial, cobertura por equipe, requisitos de agendamento,
requisitos de acesso digital, canais de contato e condições de atendimento.

Para cada critério, registre critério, serviço, evidência textual resumida,
fonte e nível de abrangência.
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

Faça um cálculo proporcional usando:
registros que atendem ao critério / registros avaliados × 100.

Mostre numerador, denominador, fórmula e resultado.
Confirme o resultado por uma segunda forma de contagem.
</etapa_4_calculo>

<etapa_5_validacao>
Valide uma orientação do PDF na fonte oficial correspondente, se disponível.

Separe claramente evidência da fonte, resultado calculado, interpretação e limitação.
</etapa_5_validacao>

<etapa_6_saida>
Entregue pergunta analítica, hipótese, exatamente dois achados, cálculo conferido,
orientação conferida, recomendação, limitações e conclusão.

Não invente dados.
Não transforme informação cadastral em prova de acesso.
Não confunda presença de serviço com disponibilidade.
Mantenha rastreabilidade para cada conclusão.
</etapa_6_saida>

## Critérios de comparação

| Critério | Prompt inicial | Prompt refinado |
|---|---|---|
| Objetivo | Sim | Sim |
| Uso do PDF antes da planilha | Não explicitado | Explicitamente encadeado |
| Mapeamento critério × campo | Não | Sim |
| Controle de inferências | Parcial | Explícito |
| Critério antes da proporção | Não | Sim |
| Validação oficial | Não obrigatória | Obrigatória quando possível |
| Rastreabilidade | Genérica | Explícita |
| Limitações | Genéricas | Obrigatórias |
| Exatamente dois achados | Não | Sim |

## Mudança concreta

O refinamento acrescenta controles para impedir que a análise conclua que uma unidade é acessível apenas porque possui uma especialidade ou horário cadastrado.

A regra mais importante é:

> Não trate especialidade como disponibilidade.

Isso responde diretamente ao alerta do material didático de que informação presente no cadastro não prova acesso.