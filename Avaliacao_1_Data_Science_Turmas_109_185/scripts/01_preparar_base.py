"""Preparação da base: lê a base original (v1), aplica verificações e tratamentos
documentados e grava a base preparada (v2) e o log de preparação.

Uso:  python scripts/01_preparar_base.py
A base original nunca é alterada.
"""
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
DADOS = RAIZ / "dados"

ORIGINAL = DADOS / "01_base_original_v1.csv"
PREPARADA = DADOS / "02_base_preparada_v2.csv"
LOG = DADOS / "04_log_preparacao.csv"

NIVEIS = {"A", "AA", "AAA", "LBI", "Boa prática", "Verificação"}
PILARES = {"Perceptível", "Operável", "Compreensível", "Robusto", "Lei"}
GRUPOS = {"visual", "auditiva", "motora", "cognitiva", "aprendizagem", "neurologica", "idosa"}
FLUXO = {"sim", "não"}

log = []


def registrar(etapa, verificacao, resultado):
    log.append({"etapa": etapa, "verificacao_ou_tratamento": verificacao, "resultado": resultado})


def ler(caminho):
    return pd.read_csv(caminho, sep=";", decimal=",", encoding="utf-8-sig", dtype={"id": str})


def verificar(df, etapa):
    registrar(etapa, "Número de linhas", str(len(df)))
    registrar(etapa, "Ids duplicados", str(int(df["id"].duplicated().sum())))
    registrar(etapa, "Células vazias nas colunas obrigatórias", str(int(df[["id", "recurso", "referencia", "nivel", "pilar", "grupos", "fluxo_critico", "horas_estimadas", "aplicavel_mvp"]].isna().sum().sum())))
    registrar(etapa, "Níveis fora do vocabulário", str(sorted(set(df["nivel"]) - NIVEIS)))
    registrar(etapa, "Pilares fora do vocabulário", str(sorted(set(df["pilar"]) - PILARES)))
    grupos_usados = {g.strip() for celula in df["grupos"] for g in celula.split(",")}
    registrar(etapa, "Grupos fora do vocabulário", str(sorted(grupos_usados - GRUPOS)))
    registrar(etapa, "Valores de fluxo_critico fora do vocabulário", str(sorted(set(df["fluxo_critico"]) - FLUXO)))
    registrar(etapa, "Horas menores ou iguais a zero", str(int((df["horas_estimadas"] <= 0).sum())))


def main():
    df = ler(ORIGINAL)
    verificar(df, "Verificação da base original (v1)")

    # Verificação de cobertura dos requisitos expressos na lei (LBI art. 63, par. 1: símbolo de acessibilidade em destaque)
    tem_simbolo = bool((df["nivel"] == "LBI").any())
    registrar("Cobertura legal", "Existe item para o símbolo de acessibilidade (LBI art. 63, par. 1)?", "sim" if tem_simbolo else "NÃO, lacuna encontrada")

    # Tratamento 1: acrescentar o requisito expresso na lei
    if not tem_simbolo:
        novo = {
            "id": "N21",
            "recurso": "Símbolo de acessibilidade em destaque e página de acessibilidade",
            "referencia": "LBI (Lei 13.146/2015), art. 63, par. 1",
            "nivel": "LBI", "pilar": "Lei", "grupos": "visual,auditiva,motora,cognitiva",
            "fluxo_critico": "não", "horas_estimadas": 1.5, "aplicavel_mvp": "Sim",
            "observacao": "Único requisito de interface citado literalmente no art. 63. Acrescentado na preparação.",
        }
        df = pd.concat([df, pd.DataFrame([novo])], ignore_index=True)
        registrar("Tratamento 1", "Acrescentado N21 (símbolo de acessibilidade em destaque)", "+1 linha, 1,5 h")

    # Tratamento 2: seletor de data e horário. Controle nativo (barato) x componente customizado (caro)
    i = df.index[df["id"] == "N13"][0]
    antes = float(df.loc[i, "horas_estimadas"])
    df.loc[i, "recurso"] = "Seletor de data e horário com controles nativos (input de data, select ou radio)"
    df.loc[i, "horas_estimadas"] = 1.5
    df.loc[i, "observacao"] = "Usar elementos HTML nativos reduz o custo. A versão customizada ficou em X03."
    alt = {
        "id": "X03", "recurso": "Calendário customizado seguindo o padrão ARIA (alternativa a N13)",
        "referencia": "WCAG 2.2: 2.1.1 (A), 4.1.2 (A)", "nivel": "Boa prática", "pilar": "Operável",
        "grupos": "motora,visual,cognitiva", "fluxo_critico": "sim", "horas_estimadas": 6.0,
        "aplicavel_mvp": "Alternativa", "observacao": "Alternativa a N13. Não somar com N13.",
    }
    df = pd.concat([df, pd.DataFrame([alt])], ignore_index=True)
    registrar("Tratamento 2", "N13 separado em versão nativa (N13) e customizada (X03)", f"N13: {antes:.1f} h para 1.5 h; X03: 6.0 h como alternativa (não soma)".replace(".", ","))

    # Tratamento 3: itens de gráficos só valem se o produto tiver gráficos (o escopo da 1ª entrega não os prevê)
    mask = df["id"].str.startswith("G")
    df.loc[mask, "aplicavel_mvp"] = "Condicional"
    registrar("Tratamento 3", "Itens G01 a G05 marcados como Condicional", f"{int(mask.sum())} linhas fora da seleção do MVP")

    # Tratamento 4: verificação é reserva de tempo, não recurso
    df.loc[df["id"] == "V01", "aplicavel_mvp"] = "Reserva"
    registrar("Tratamento 4", "V01 tratado como reserva de tempo (não pontua impacto)", "1 linha")

    # Custo financeiro: todas as ferramentas previstas são gratuitas
    df["custo_reais"] = 0.0
    registrar("Tratamento 5", "Coluna custo_reais criada com R$ 0,00 (Lighthouse, axe DevTools, WAVE, NVDA e navegador são gratuitos)", "custo total R$ 0,00")

    ordem = {"N": 0, "P": 1, "X": 2, "G": 3, "V": 4}
    df["_o"] = df["id"].str[0].map(ordem)
    df = df.sort_values(["_o", "id"]).drop(columns="_o").reset_index(drop=True)

    verificar(df, "Verificação da base preparada (v2)")
    df.to_csv(PREPARADA, sep=";", decimal=",", encoding="utf-8-sig", index=False)
    pd.DataFrame(log).to_csv(LOG, sep=";", encoding="utf-8-sig", index=False)
    print(pd.DataFrame(log).to_string(index=False))


if __name__ == "__main__":
    main()
