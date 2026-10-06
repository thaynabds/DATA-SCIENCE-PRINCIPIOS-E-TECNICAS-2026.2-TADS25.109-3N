# DataViz parte 2: votação simulada no Recife

Faculdade Senac Pernambuco, Recife-PE.
Tecnólogo em Análise e Desenvolvimento de Sistemas.
Unidade curricular: Data Science: Princípios e Técnicas, 2026.2, turma TADS25.109/3N.
Professor: Rodrigo Rios.
Aluna: Thayná Batista da Silva.
Entrega: 06/10/2026.

A página para o professor é o arquivo `entrega/pagina.pdf`. Ela tem os dois gráficos, a justificativa e a conclusão.

Os dados são uma simulação de aula. Não são o resultado de uma eleição real.

## Respostas

Raquel Lima venceu no recorte. Ela teve 15.546 votos válidos de 24.215. Isso é 64,20% dos votos válidos.

João Capim teve 8.499 votos válidos, 35,10%. Ivan Pinto teve 170, 0,70%.

Se abstiveram 7.738 eleitores. Eram 33.970 aptos e 26.232 compareceram. A taxa é 7.738 dividido por 33.970, ou seja, 22,78% dos aptos.

A maior taxa de abstenção foi na SEC021, na Várzea: 304 de 800 aptos, 38,00%. Depois veio a SEC022, 326 de 1.050, 31,05%. Depois a SEC024, 564 de 1.880, 30,00%.

A SEC012, na Boa Vista, teve mais abstenções em quantidade, 588 pessoas. A taxa dela foi 588 de 2.260, 26,02%. Quantidade maior não é taxa maior.

## Como as contas foram feitas

Cruzei as duas bases pela seção.

- Comparecimento é o número de linhas da base de votos. Cada linha é um eleitor presente.
- Abstenção é eleitores aptos menos comparecimento.
- Taxa de abstenção é abstenção dividido pelos eleitores aptos daquela seção, ou do recorte todo.
- Branco e nulo entram no comparecimento. Eles não entram nos votos válidos.
- O percentual de cada candidato é o voto dele dividido pelo total de votos válidos, não pelo total de aptos.

As somas fecham:

- 33.970 = 26.232 + 7.738
- 26.232 = 24.215 + 1.250 + 767
- 24.215 = 15.546 + 8.499 + 170

A tabela seção por seção está em `entrega/secoes_calculadas.csv`. Os totais estão em `entrega/totais.csv`.

## Por que estes dois gráficos

A aula pede comparar os gráficos antes de escolher.

| Gráfico | Serve para | Nesta atividade |
| --- | --- | --- |
| Dumbbell | A mesma categoria em dois momentos | Não usei. Só há uma eleição. |
| Bolhas | Três medidas juntas | Usei. Taxa, parte da Raquel e aptos. |
| Treemap | Partes que somam um total | Não usei. Taxa não soma. |
| Cascata | O que formou um saldo | Não usei. Não mostra candidato nem seção. |
| Funil | Quantos chegaram a cada etapa | Não usei. Não mostra para quem foi o voto. |
| Sankey | O caminho e a divisão | Usei. Aptos, comparecimento, tipo de voto e candidato. |
| Mapa | O lugar explica o padrão | Não usei. A base não tem o desenho do bairro. |

O Sankey responde quem venceu e quantos se abstiveram. As bolhas mostram qual seção teve a maior taxa. A área da bolha é o número de aptos. Se a quantidade fosse 4 vezes maior, o raio só dobraria.

## Pastas

- `dados/`: as duas bases da atividade.
- `src/calcular.py`: cruza as bases e confere as somas.
- `src/graficos.py`: desenha o Sankey e as bolhas.
- `src/pagina.py`: monta a página.
- `entrega/`: PDF, imagens e tabelas.

## Como gerar de novo

Na pasta do projeto:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m src.pagina
```

O script para se algum total não fechar. A pasta `.venv` não entra no GitHub.

## Fontes

- Rios, Rodrigo. DataViz com inteligência artificial, parte 2. Faculdade Senac Pernambuco, 2026. Material da aula.
- Google. Sankey diagram. Google for Developers. https://developers.google.com/chart/interactive/docs/gallery/sankey
- Wilke, Claus O. Fundamentals of Data Visualization. Sebastopol: O'Reilly Media, 2019. https://clauswilke.com/dataviz/
- Instituto Brasileiro de Geografia e Estatística. API de malhas geográficas, versão 3. https://servicodados.ibge.gov.br/api/docs/malhas?versao=3

A regra de branco e nulo é a regra dada na atividade: os dois contam como comparecimento e não contam como voto válido.
