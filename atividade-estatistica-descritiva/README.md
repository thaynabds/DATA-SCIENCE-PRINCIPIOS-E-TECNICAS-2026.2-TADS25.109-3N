# Preço típico da gasolina comum

Atividade de estatística descritiva. A pergunta é: qual é o preço típico da gasolina comum nos postos pesquisados pela ANP.

**Aluna:** Thayná Batista da Silva
**Faculdade Senac de Pernambuco, Recife-PE**
**Curso:** Tecnólogo em Análise e Desenvolvimento de Sistemas
**Unidade curricular:** Data Science: Princípios e Técnicas, 2026.2 [TADS25.109/3N]
**Professor:** Rodrigo Rios

A entrega para leitura é a ficha, com os números, os gráficos e a conclusão:

[entrega/FICHA.md](entrega/FICHA.md)

## O que a análise responde

Nos 51 postos, a mediana é R$ 6,97 por litro. Essa é a medida usada como preço típico do conjunto. A média é R$ 6,9649, a moda é R$ 6,95, a amplitude é R$ 0,10 e o desvio padrão amostral é R$ 0,0202.

A conta completa, o motivo da escolha e a limitação dos dados estão na ficha.

## Pastas

| Pasta ou arquivo | Função |
| --- | --- |
| `dados/Dados_Gasolina_ANP_2026-09-21_a_27.csv` | Base usada nas contas. Separador ponto e vírgula, decimal com vírgula. |
| `dados/Dataset_Gasolina_ANP.xlsx` | Arquivo da atividade, com as abas Dados, Guia e Original_ANP. |
| `entrega/FICHA.md` | Ficha com resultados, gráficos e conclusão. |
| `entrega/histograma.png` | Histograma com faixas de R$ 0,02. |
| `entrega/boxplot.png` | Boxplot com os quartis do método da aula. |
| `entrega/conferencia_calculos.xlsx` | Planilha com fórmulas para conferir média, mediana, moda, amplitude e desvio padrão. |
| `entrega/resultados.csv` | Valores calculados, com as casas decimais do cálculo. |
| `src/calcular.py` | Script que lê a base, confere as contas e gera a planilha e os gráficos. |

## Como repetir as contas

Na pasta deste projeto:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/calcular.py
```

O script confere a quantidade, a soma, a média, a mediana, a moda, a amplitude, os quartis e o começo do desvio padrão. Se alguma dessas contas mudar, ele para com erro.

Para conferir na planilha, abra `entrega/conferencia_calculos.xlsx` no LibreOffice ou no Excel e leia a aba Medidas. As fórmulas recalculam os mesmos resultados. A convenção do desvio padrão é a amostral, com divisor n - 1.

## Fonte dos preços

Agência Nacional do Petróleo, Gás Natural e Biocombustíveis. Série histórica de preços de combustíveis e de GLP. Dados de setembro de 2026. Acesso em: 8 out. 2026.
https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis

O recorte traz gasolina comum em Recife, Olinda e Jaboatão dos Guararapes, na semana de 21 a 27/09/2026. Há 51 coletas.
