# Dossiê de Acessibilidade: PI Saúde na Palma da Mão

**1ª Atividade Avaliativa: Dossiê do Problema e dos Dados**
Disciplina: Data Science: Princípios e Técnicas ([TADS25.109/3N], 2026.2)
Professor: Rodrigo Rios
Alunas: Thayná Batista da Silva e Polyana Fontes
Instituição: Faculdade Senac Pernambuco, Recife-PE. Curso: Análise e Desenvolvimento de Sistemas.

## Problema

Quais recursos de acessibilidade digital (LBI art. 63, ABNT NBR 17225:2025 e WCAG 2.2 níveis A e AA) são viáveis na 1ª entrega do PI Saúde na Palma da Mão (PWA), com orçamento de R$ 0,00, duas alunas e cerca de duas semanas?

A análise apoia uma decisão: quais recursos entram na 1ª entrega, quais ficam para a 2ª (React Native com IA) e quais ficam de fora.

## Resultado em resumo

Parâmetros assumidos: 20 h de capacidade (2 pessoas x 2 semanas x 5 h por semana), sendo 4 h reservadas para verificação e 16 h para implementação.

| Indicador | Valor |
|---|---|
| Itens do núcleo normativo (A, AA e símbolo da LBI) | 21 itens, 26,0 h |
| Itens que cabem em 16 h | 10 itens (47,6% dos itens), 16,0 h (61,5% das horas do núcleo) |
| Itens adiados para a 2ª entrega | 11 itens, 10,0 h |
| Capacidade para cobrir 100% do núcleo | 30 h totais (150% da assumida) |
| Recursos de personalização da lista inicial | 11 itens, 18,5 h, impacto médio 1,8 (núcleo: 4,5) |
| Custo financeiro | R$ 0,00 |

Pacote recomendado para a 1ª entrega, em ordem de prioridade: N21, N17, N03, N07, N13, N18, N04, N05, N12, N14. Ele inclui o símbolo de acessibilidade exigido pelo art. 63, §1º da LBI e os 9 itens de nível A que atuam nos fluxos de login, cadastro, consulta e agendamento.

## Aviso importante sobre os dados

Os dados são **sintéticos**. Os critérios, níveis e referências vêm de fontes públicas reais (WCAG 2.2, NBR 17225, LBI). As **horas estimadas** e a capacidade da equipe são hipóteses, não medições. A conclusão vale para o cenário simulado. Este material não é parecer jurídico.

## Estrutura do repositório

```
.
├── README.md
├── requirements.txt
├── .gitignore
├── dossie/
│   └── Dossie_Acessibilidade_PI_Saude_na_Palma_da_Mao.docx   Dossiê completo (6 partes, fontes e apêndices)
├── dados/
│   ├── 01_base_original_v1.csv        Base original, preservada sem alterações
│   ├── 02_base_preparada_v2.csv       Base após os tratamentos
│   ├── 03_base_analitica.csv          Impacto, camada, ordem e decisão de cada item
│   ├── 04_log_preparacao.csv          Verificações e tratamentos aplicados
│   ├── 05_grafico1_tabela.csv         Tabela de origem do Gráfico 1
│   ├── 06_grafico2_tabela.csv         Tabela de origem do Gráfico 2
│   ├── 07_sensibilidade.csv           Variação de capacidade e de estimativas
│   ├── 08_conferencia_calculos.csv    Conferências independentes dos cálculos
│   └── 09_resumo.csv                  Indicadores usados no texto
├── graficos/
│   ├── grafico1_esforco_impacto.png
│   ├── grafico2_versao_inicial.png
│   └── grafico2_versao_revisada.png
└── scripts/
    ├── 01_preparar_base.py            Verifica e trata a base original
    └── 02_analisar.py                 Calcula, seleciona, confere e gera os gráficos
```

Os arquivos CSV usam ponto e vírgula como separador, vírgula decimal e codificação UTF-8 com BOM, para abrir corretamente no Excel em português.

## Como reproduzir

Requisitos: Python 3.10 ou superior.

```bash
git clone https://github.com/SEU-USUARIO/pi-saude-acessibilidade-dossie.git
cd pi-saude-acessibilidade-dossie
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/01_preparar_base.py
python scripts/02_analisar.py
```

Os scripts regravam os arquivos 02 a 09 em `dados/` e os gráficos em `graficos/`. O arquivo 01 não é alterado.

### Conferência sem programar (Excel ou Google Planilhas)

1. Abra `dados/03_base_analitica.csv`.
2. Some as horas dos itens com decisão "Fazer no MVP": `=SOMASE(coluna_decisao;"Fazer no MVP";coluna_horas_estimadas)`. O resultado esperado é 16,00.
3. Confira a ordem: ordene por `ordem` e verifique que `horas_acumuladas` cruza 16 h entre N14 (16,0) e N16 (16,5).

## Regras da análise

- **Impacto (1 a 5):** 3 pontos se o critério é nível A, AA ou exigência da LBI (1 ponto nos demais), mais 1 ponto se o recurso atua em fluxo crítico (login, cadastro, consulta, agendamento), mais 1 ponto se beneficia dois ou mais grupos.
- **Camadas:** T0 é a exigência expressa na lei, T1 é nível A em fluxo crítico e T2 são os demais itens.
- **Seleção:** ordem T0, T1, T2; dentro de cada camada, maior impacto por hora. O pacote é a sequência inicial cuja soma de horas cabe na capacidade de implementação.
- **Parâmetros editáveis** no início de `scripts/02_analisar.py`: `CAPACIDADE_TOTAL_H`, `RESERVA_VERIFICACAO_H` e `MULTIPLICADOR_ESTIMATIVA`.

## Limites

- Dados sintéticos e horas estimadas. A capacidade de 20 h é uma suposição.
- O escore de impacto é uma regra da equipe e favorece níveis A e AA por construção.
- Não há testes com pessoas com deficiência nem medição em um PWA real.
- A LGPD (dados de saúde) está fora do escopo.
- Os níveis dos critérios herdados da WCAG 2.0 e 2.1 devem ser conferidos na Referência Rápida do W3C.
- Os materiais do PI citam duas datas para a 1ª entrega (05/10/2026 e 14/10/2026).

## Fontes principais

- BRASIL. Lei nº 13.146/2015 (LBI), art. 63. https://www.planalto.gov.br/ccivil_03/_Ato2015-2018/2015/Lei/L13146.htm
- ABNT. NBR 17225:2025, Acessibilidade em conteúdo e aplicações web: requisitos. 11 mar. 2025.
- W3C. WCAG 2.2 (pt-BR). https://www.w3.org/Translations/WCAG22-pt-BR/
- SENADO FEDERAL. PL 981/2022. https://www25.senado.leg.br/web/atividade/materias/-/materia/152780
- Lista completa, com endereços, no dossiê (seção Fontes).

## Uso de IA

Foi usado o Claude (Anthropic) para pesquisa, estruturação e cálculo. As conferências, correções e descartes estão descritos na Parte 05 do dossiê e nos arquivos `04_log_preparacao.csv` e `08_conferencia_calculos.csv`.

## Licença e uso

Projeto acadêmico da Faculdade Senac Pernambuco. Uso educacional.
