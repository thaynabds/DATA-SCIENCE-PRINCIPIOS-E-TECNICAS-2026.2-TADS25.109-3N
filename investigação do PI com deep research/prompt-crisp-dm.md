# Prompt CRISP-DM, Recife Saudável

## Objetivo

Prompt estruturado para investigação e análise de Data Science sobre a demanda e a oferta de serviços especializados no Recife.

```text
Atue como um cientista de dados responsável por uma análise exploratória e descritiva sobre o acesso a serviços de saúde especializados no Recife.

CONTEXTO:
O Projeto Integrador "Recife Saudável", da Faculdade Senac Pernambuco, propõe uma jornada digital para cadastro, pré-triagem informativa e agendamento de consultas. Evidências oficiais da Prefeitura do Recife indicam existência de filas, demora na marcação e necessidade de monitoramento da demanda por consultas e serviços especializados.

OBJETIVO:
Investigar a distribuição da demanda por consultas e procedimentos especializados no Recife e relacioná-la, de forma descritiva, à distribuição das unidades e especialidades disponíveis.

DADOS:
Utilize prioritariamente:
1. Dataset "Consultas e Procedimentos de Saúde", Portal de Dados Abertos do Recife.
2. Dataset "Unidades Especializadas", Portal de Dados Abertos do Recife.

FONTES:
https://dados.recife.pe.gov.br/dataset/consultas-e-procedimentos-de-saude
https://dados.recife.pe.gov.br/dataset/unidades-especializadas

VARIÁVEIS DE INTERESSE:
especialidade, consultas, procedimentos, tipo, atenção, período, unidade, endereço, bairro, RPA, distrito sanitário, serviço, horário, latitude e longitude.

SAÍDAS ESPERADAS:
1. Estatísticas descritivas.
2. Ranking das especialidades por volume de consultas.
3. Distribuição das consultas por localidade.
4. Quantidade de unidades especializadas por especialidade e localidade.
5. Comparação entre demanda observada e distribuição das unidades.
6. Identificação de concentrações, diferenças ou possíveis desequilíbrios.
7. Visualizações adequadas para cada análise.
8. Limitações dos dados.
9. Conclusões exclusivamente suportadas pelas evidências.

LIMITES:
Não realizar diagnóstico médico.
Não utilizar os dados para inferir condições clínicas individuais.
Não criar modelos de decisão clínica.
Não afirmar causalidade entre uso de aplicativo e redução de filas.
Não estimar tempo individual de espera quando essa variável não estiver presente na base.
Não inventar valores ausentes.
Não extrapolar resultados para toda a população quando a cobertura dos dados não permitir.

VERIFICAÇÃO:
Antes da análise:
1. verificar quantidade de registros;
2. verificar tipos das variáveis;
3. identificar valores ausentes;
4. detectar duplicidades;
5. verificar inconsistências de especialidade e localização;
6. verificar período temporal;
7. documentar transformações realizadas.

CRISP-DM:
Business Understanding:
Definir o problema de acesso e organização da demanda.

Data Understanding:
Descrever as bases, variáveis, origem, período e limitações.

Data Preparation:
Limpar, padronizar e integrar as bases quando houver chave ou correspondência confiável.

Modeling:
Priorizar análise estatística descritiva, agregações, rankings e visualizações.
Não utilizar modelagem preditiva caso os dados não suportem essa abordagem.

Evaluation:
Verificar se os resultados respondem à pergunta de negócio e se são compatíveis com as variáveis disponíveis.
Registrar limitações e resultados inconclusivos.

Deployment:
Produzir recomendações que possam orientar o desenho do Recife Saudável, especialmente organização de especialidades, localização de serviços e redução de atrito na jornada de agendamento.

ENTREGA:
Produzir uma síntese executiva contendo:
problema,
dados utilizados,
método,
principais achados,
limitações,
decisão final da equipe.
```
