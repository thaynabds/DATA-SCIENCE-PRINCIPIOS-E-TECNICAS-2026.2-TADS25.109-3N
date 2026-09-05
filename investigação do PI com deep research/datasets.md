# Datasets Verificados

## 1. Consultas e Procedimentos de Saúde

**Órgão:** Secretaria de Saúde do Recife  
**Mantenedor:** EMPREL  
**Fonte:** Portal de Dados Abertos do Recife

Links:

- Dataset: https://dados.recife.pe.gov.br/dataset/consultas-e-procedimentos-de-saude
- Página de recursos: https://dados.recife.pe.gov.br/dataset/consultas-e-procedimentos-de-saude

Descrição:

> Totais de consultas e procedimentos de saúde realizados por tipo, especialidade e localidade.

Campos de interesse:

| Campo | Utilização |
|---|---|
| `especialidade` | análise por especialidade |
| `consultas` | volume de consultas |
| `procedimentos` | volume de procedimentos |
| `usf` | unidade |
| `endereco` | localização |
| `periodo` | dimensão temporal |
| `tipo` | classificação |
| `atencao` | tipo de atenção |

## 2. Unidades Especializadas

**Órgão:** Secretaria de Saúde do Recife  
**Mantenedor:** EMPREL  
**Fonte:** Portal de Dados Abertos do Recife

Links:

- Dataset: https://dados.recife.pe.gov.br/dataset/unidades-especializadas
- Recurso: https://dados.recife.pe.gov.br/dataset/unidades-especializadas

Descrição:

> São serviços de saúde destinados às especialidades médicas e não médicas e, quando necessário, à utilização de equipamentos médico-hospitalares para a produção do cuidado em média e alta complexidade.

Campos de interesse:

| Campo | Utilização |
|---|---|
| `nome_oficial` | unidade |
| `rpa` | região |
| `distrito_sanitario` | distrito |
| `microregiao` | microrregião |
| `cnes` | estabelecimento |
| `tipo_servico` | tipo de serviço |
| `endereço` | localização |
| `bairro` | localização |
| `servico` | serviço |
| `especialidade` | especialidade |
| `como_usar` | uso do serviço |
| `horario` | horário |
| `latitude` | geolocalização |
| `longitude` | geolocalização |

## Adequação

As duas bases são adequadas para análise exploratória e descritiva.

Não foram consideradas adequadas, isoladamente, para previsão de tempo individual de espera ou no-show, pela ausência dessas variáveis em granularidade individual no conjunto selecionado.
