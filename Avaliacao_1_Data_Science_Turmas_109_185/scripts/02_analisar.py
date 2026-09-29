"""Análise: calcula impacto, prioridade e decisão, a sensibilidade, as conferências e os gráficos.

Uso:  python scripts/02_analisar.py
Lê dados/02_base_preparada_v2.csv (rode antes scripts/01_preparar_base.py).
"""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
DADOS = RAIZ / "dados"
GRAF = RAIZ / "graficos"

# Parâmetros (hipóteses da equipe, editáveis)
CAPACIDADE_TOTAL_H = 20.0      # 2 pessoas x 2 semanas x 5 h por semana dedicadas à acessibilidade
RESERVA_VERIFICACAO_H = 4.0    # item V01
MULTIPLICADOR_ESTIMATIVA = 1.0

AZUL, LARANJA, VERDE, VERMELHO, ROXO, CINZA = "#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7", "#7A7A7A"


def ler(nome):
    return pd.read_csv(DADOS / nome, sep=";", decimal=",", encoding="utf-8-sig", dtype={"id": str})


def gravar(df, nome):
    df.to_csv(DADOS / nome, sep=";", decimal=",", encoding="utf-8-sig", index=False)


def pontuar(df):
    df = df.copy()
    df["n_grupos"] = df["grupos"].str.split(",").str.len()
    base = {"A": 3, "AA": 3, "LBI": 3, "AAA": 1, "Boa prática": 1}
    df["pts_nivel"] = df["nivel"].map(base)
    df["pts_fluxo"] = (df["fluxo_critico"] == "sim").astype(int)
    df["pts_grupos"] = (df["n_grupos"] >= 2).astype(int)
    df["impacto"] = df["pts_nivel"] + df["pts_fluxo"] + df["pts_grupos"]
    df.loc[df["nivel"] == "Verificação", ["pts_nivel", "pts_fluxo", "pts_grupos", "impacto"]] = pd.NA
    df["razao_impacto_hora"] = (df["impacto"].astype(float) / df["horas_estimadas"]).round(3)
    return df


def camada(linha):
    if linha["aplicavel_mvp"] != "Sim":
        return "-"
    if linha["nivel"] == "LBI":
        return "T0"
    if linha["fluxo_critico"] == "sim" and linha["nivel"] == "A":
        return "T1"
    return "T2"


def ordenar(df, usar_camadas=True):
    """Ordem de prioridade: T0, T1, T2; dentro de cada camada, maior impacto por hora, maior impacto, id."""
    sim = df[df["aplicavel_mvp"] == "Sim"].copy()
    sim["camada"] = sim.apply(camada, axis=1)
    if usar_camadas:
        sim["_c"] = sim["camada"].map({"T0": 0, "T1": 1, "T2": 2})
    else:
        sim["_c"] = 0
    sim = sim.sort_values(["_c", "razao_impacto_hora", "impacto", "id"], ascending=[True, False, False, True]).reset_index(drop=True)
    sim["ordem"] = sim.index + 1
    return sim.drop(columns="_c")


def selecionar(ordem, capacidade_impl, mult=1.0):
    """Seleciona o prefixo da ordem cuja soma de horas cabe na capacidade (para no primeiro item que estoura)."""
    ordem = ordem.copy()
    ordem["horas_ajustadas"] = ordem["horas_estimadas"] * mult
    ordem["horas_acumuladas"] = ordem["horas_ajustadas"].cumsum()
    selecionado, parou = [], False
    for h in ordem["horas_acumuladas"]:
        ok = (not parou) and h <= capacidade_impl + 1e-9
        parou = parou or (not ok)
        selecionado.append(ok)
    ordem["no_pacote"] = selecionado
    return ordem


def otimo_mochila(ordem, capacidade_impl):
    """Conferência: máximo de impacto possível com a capacidade, por programação dinâmica (passos de 0,5 h)."""
    itens = [(int(round(h * 2)), int(i)) for h, i in zip(ordem["horas_estimadas"], ordem["impacto"])]
    cap = int(round(capacidade_impl * 2))
    melhor = [0] * (cap + 1)
    for peso, valor in itens:
        for c in range(cap, peso - 1, -1):
            melhor[c] = max(melhor[c], melhor[c - peso] + valor)
    return melhor[cap]


def main():
    base = pontuar(ler("02_base_preparada_v2.csv"))
    cap_impl = CAPACIDADE_TOTAL_H - RESERVA_VERIFICACAO_H
    ordem = selecionar(ordenar(base), cap_impl)

    # Decisão por item
    def decidir(linha):
        ap = linha["aplicavel_mvp"]
        if ap == "Condicional":
            return "Condicional (só se houver gráficos)"
        if ap == "Alternativa":
            return "Alternativa (não somar)"
        if ap == "Reserva":
            return "Reserva de verificação"
        if linha["no_pacote"]:
            return "Fazer no MVP"
        return "Adiar (2ª entrega)" if linha["id"].startswith("N") else "Backlog (depois do núcleo)"

    base = base.merge(ordem[["id", "camada", "ordem", "horas_acumuladas", "no_pacote"]], on="id", how="left")
    base["camada"] = base["camada"].fillna("-")
    base["no_pacote"] = base["no_pacote"].fillna(False).astype(bool)
    base["decisao"] = base.apply(decidir, axis=1)
    base["_o"] = base["ordem"].fillna(999)
    base = base.sort_values(["_o", "id"]).drop(columns="_o")
    gravar(base, "03_base_analitica.csv")

    nucleo = base[base["id"].str.startswith("N")]
    pers = base[base["id"].str.startswith("P")]
    pacote = base[base["decisao"] == "Fazer no MVP"]
    resumo = {
        "capacidade_total_h": CAPACIDADE_TOTAL_H, "reserva_verificacao_h": RESERVA_VERIFICACAO_H, "capacidade_implementacao_h": cap_impl,
        "itens_nucleo": len(nucleo), "horas_nucleo": nucleo["horas_estimadas"].sum(),
        "itens_pacote": len(pacote), "horas_pacote": pacote["horas_estimadas"].sum(),
        "itens_nucleo_no_pacote": int(pacote["id"].str.startswith("N").sum()),
        "horas_nucleo_no_pacote": pacote.loc[pacote["id"].str.startswith("N"), "horas_estimadas"].sum(),
        "mediana_razao_nucleo": nucleo["razao_impacto_hora"].median(), "mediana_razao_personalizacao": pers["razao_impacto_hora"].median(),
        "media_impacto_nucleo": nucleo["impacto"].astype(float).mean(), "media_impacto_personalizacao": pers["impacto"].astype(float).mean(),
        "horas_personalizacao": pers["horas_estimadas"].sum(), "itens_personalizacao": len(pers),
        "impacto_total_pacote": int(pacote["impacto"].astype(int).sum()),
    }

    # Sensibilidade: capacidade total x multiplicador das estimativas
    linhas = []
    ordem_base = ordenar(base.drop(columns=["camada", "ordem", "horas_acumuladas", "no_pacote", "decisao"]))
    n_nucleo = int(base["id"].str.startswith("N").sum())
    h_nucleo = float(nucleo["horas_estimadas"].sum())
    for mult in (1.0, 1.5):
        for cap_total in (12, 16, 20, 24, 30, 32, 40):
            cap_i = cap_total - RESERVA_VERIFICACAO_H * mult
            sel = selecionar(ordem_base, cap_i, mult)
            pk = sel[sel["no_pacote"]]
            nuc = pk[pk["id"].str.startswith("N")]
            bloq = sel[sel["camada"].isin(["T0", "T1"])]
            linhas.append({
                "multiplicador_das_estimativas": mult, "capacidade_total_h": cap_total, "capacidade_implementacao_h": round(cap_i, 2),
                "itens_no_pacote": len(pk), "horas_usadas": round(float(pk["horas_ajustadas"].sum()), 2),
                "itens_do_nucleo_cobertos": len(nuc), "itens_do_nucleo_total": n_nucleo,
                "pct_itens_do_nucleo": round(100 * len(nuc) / n_nucleo, 1),
                "pct_horas_do_nucleo": round(100 * float(nuc["horas_ajustadas"].sum()) / (h_nucleo * mult), 1),
                "bloqueadores_e_lei_cobertos": f"{int(bloq['no_pacote'].sum())} de {len(bloq)}",
            })
    sens = pd.DataFrame(linhas)
    gravar(sens, "07_sensibilidade.csv")

    # Conferências independentes
    conf = []
    horas_pandas = float(pacote["horas_estimadas"].sum())
    with open(DADOS / "03_base_analitica.csv", encoding="utf-8-sig", newline="") as f:
        horas_csv = sum(float(r["horas_estimadas"].replace(",", ".")) for r in csv.DictReader(f, delimiter=";") if r["decisao"] == "Fazer no MVP")
    conf.append(("Horas do pacote MVP: pandas x leitura direta do CSV", f"{horas_pandas:.2f} x {horas_csv:.2f}", "igual" if abs(horas_pandas - horas_csv) < 1e-9 else "DIFERENTE"))
    conf.append(("Horas do pacote <= capacidade de implementação", f"{horas_pandas:.2f} <= {cap_impl:.2f}", "ok" if horas_pandas <= cap_impl else "ERRO"))
    conf.append(("Soma das horas do núcleo (N01 a N21)", f"{h_nucleo:.2f}", "-"))
    otimo = otimo_mochila(ordem, cap_impl)
    conf.append(("Impacto do pacote x máximo possível (programação dinâmica)", f"{resumo['impacto_total_pacote']} x {otimo}", f"pacote atinge {100 * resumo['impacto_total_pacote'] / otimo:.1f}% do máximo"))
    so_razao = selecionar(ordenar(base.drop(columns=["camada", "ordem", "horas_acumuladas", "no_pacote", "decisao"]), usar_camadas=False), cap_impl)
    excl = so_razao[(~so_razao["no_pacote"]) & (so_razao["nivel"] == "A") & (so_razao["fluxo_critico"] == "sim")]["id"].tolist()
    conf.append(("Regra alternativa (só razão impacto/hora): bloqueadores de fluxo que ficariam de fora", ", ".join(excl) if excl else "nenhum", "regra descartada" if excl else "-"))
    pk_alt = so_razao[so_razao["no_pacote"]]
    conf.append(("Regra alternativa: itens no pacote e horas", f"{len(pk_alt)} itens, {pk_alt['horas_estimadas'].sum():.2f} h", "-"))
    ids_pacote = pacote.sort_values("ordem")["id"].tolist()
    conf.append(("Itens do pacote (regra adotada)", ", ".join(ids_pacote), "-"))
    conf.append(("Custo financeiro total da base", f"R$ {base['custo_reais'].sum():.2f}".replace(".", ","), "-"))
    pd.DataFrame(conf, columns=["conferencia", "valor", "situacao"]).to_csv(DADOS / "08_conferencia_calculos.csv", sep=";", encoding="utf-8-sig", index=False)

    # Tabelas de origem dos gráficos
    g1 = base[base["aplicavel_mvp"].isin(["Sim", "Condicional"])][["id", "recurso", "horas_estimadas", "impacto", "decisao"]]
    gravar(g1, "05_grafico1_tabela.csv")
    g2 = base[base["ordem"].notna()][["ordem", "id", "camada", "horas_estimadas", "horas_acumuladas", "decisao"]].copy()
    g2["ordem"] = g2["ordem"].astype(int)
    gravar(g2, "06_grafico2_tabela.csv")

    desenhar_grafico1(base)
    desenhar_grafico2(base, cap_impl)
    pd.Series(resumo).to_csv(DADOS / "09_resumo.csv", sep=";", encoding="utf-8-sig", header=["valor"], index_label="indicador")
    print(pd.Series(resumo).to_string())
    print(sens.to_string(index=False))
    print(pd.DataFrame(conf, columns=["c", "v", "s"]).to_string(index=False))


def desenhar_grafico1(base):
    d = base[base["aplicavel_mvp"].isin(["Sim"])].copy()
    d["impacto"] = d["impacto"].astype(int)
    cores = {"Fazer no MVP": AZUL, "Adiar (2ª entrega)": VERMELHO, "Backlog (depois do núcleo)": CINZA}
    marca = {"N": "o", "P": "^", "X": "s"}
    fig, ax = plt.subplots(figsize=(11, 6.2), dpi=150)
    # afastar levemente pontos sobrepostos
    d["_k"] = d.groupby(["horas_estimadas", "impacto"]).cumcount()
    d["_n"] = d.groupby(["horas_estimadas", "impacto"])["id"].transform("count")
    d["x"] = d["horas_estimadas"] + (d["_k"] - (d["_n"] - 1) / 2) * 0.13
    for _, r in d.iterrows():
        ax.scatter(r["x"], r["impacto"], s=95, marker=marca[r["id"][0]], color=cores[r["decisao"]], edgecolor="black", linewidth=0.6, zorder=3)
        ax.annotate(r["id"], (r["x"], r["impacto"]), textcoords="offset points", xytext=(0, 9 + (int(r["_k"]) % 2) * 9), ha="center", fontsize=7)
    ax.set_xlim(0.1, 3.4)
    ax.set_ylim(0.4, 5.9)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_xlabel("Esforço estimado (horas de implementação)")
    ax.set_ylabel("Impacto (pontos de 1 a 5)")
    ax.set_title("Esforço x impacto dos recursos de acessibilidade\n(34 itens aplicáveis ao MVP, dados sintéticos)", fontsize=11)
    ax.grid(alpha=0.3)
    from matplotlib.lines import Line2D
    leg = [Line2D([0], [0], marker="o", color="w", markerfacecolor=AZUL, markeredgecolor="black", markersize=9, label="Fazer no MVP"),
           Line2D([0], [0], marker="o", color="w", markerfacecolor=VERMELHO, markeredgecolor="black", markersize=9, label="Adiar (2ª entrega)"),
           Line2D([0], [0], marker="o", color="w", markerfacecolor=CINZA, markeredgecolor="black", markersize=9, label="Backlog (depois do núcleo)"),
           Line2D([0], [0], marker="o", color="w", markerfacecolor="white", markeredgecolor="black", markersize=9, label="Círculo: núcleo (N)"),
           Line2D([0], [0], marker="^", color="w", markerfacecolor="white", markeredgecolor="black", markersize=9, label="Triângulo: personalização (P)"),
           Line2D([0], [0], marker="s", color="w", markerfacecolor="white", markeredgecolor="black", markersize=9, label="Quadrado: extras AAA (X)")]
    ax.legend(handles=leg, loc="center left", bbox_to_anchor=(1.01, 0.5), fontsize=8, framealpha=0.95)
    fig.text(0.01, 0.005, "Fonte: base 03_base_analitica.csv (dados sintéticos, set/2026). Impacto = nível + fluxo crítico + amplitude. Pequeno deslocamento horizontal evita sobreposição.", fontsize=7)
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    fig.savefig(GRAF / "grafico1_esforco_impacto.png")
    plt.close(fig)


def desenhar_grafico2(base, cap_impl):
    d = base[base["ordem"].notna()].sort_values("ordem").copy()
    x = list(range(1, len(d) + 1))
    y = d["horas_acumuladas"].tolist()
    ymax = 52
    # Versão inicial: linha simples, sem rótulos e sem linha de capacidade
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=150)
    ax.plot(x, y, color=AZUL, marker="o", markersize=4)
    ax.set_ylim(0, ymax)
    ax.set_xlabel("Ordem de prioridade dos itens")
    ax.set_ylabel("Horas acumuladas")
    ax.set_title("Horas acumuladas pela ordem de prioridade (versão inicial)", fontsize=11)
    fig.tight_layout()
    fig.savefig(GRAF / "grafico2_versao_inicial.png")
    plt.close(fig)

    # Versão revisada: mesma série, mesma escala, com rótulos, capacidade e cores por camada
    fig, ax = plt.subplots(figsize=(10, 5.6), dpi=150)
    ax.plot(x, y, color="#444444", linewidth=1, zorder=1)
    cor_camada = {"T0": VERDE, "T1": AZUL, "T2": LARANJA}
    forma = {"T0": "D", "T1": "o", "T2": "s"}
    for xi, yi, (_, r) in zip(x, y, d.iterrows()):
        dentro = bool(r["no_pacote"])
        ax.scatter(xi, yi, s=55, marker=forma[r["camada"]], color=cor_camada[r["camada"]], edgecolor="black", linewidth=0.5, zorder=3, alpha=1.0 if dentro else 0.55)
    ax.axhline(cap_impl, color=VERMELHO, linestyle="--", linewidth=1.6, zorder=2)
    ax.text(len(x) + 0.3, cap_impl + 0.8, f"Capacidade de implementação: {cap_impl:.0f} h", color=VERMELHO, ha="right", fontsize=9, fontweight="bold")
    for xi, yi, (_, r) in zip(x, y, d.iterrows()):
        if r["no_pacote"] or xi <= x[[bool(v) for v in d["no_pacote"]].count(True)] + 2:
            ax.annotate(f"{r['id']}\n{yi:.1f}", (xi, yi), textcoords="offset points", xytext=(-2, 7), ha="right", fontsize=6.5)
    n_pk = int(d["no_pacote"].sum())
    ax.axvspan(0.5, n_pk + 0.5, color=AZUL, alpha=0.06, zorder=0)
    ax.text(n_pk / 2 + 0.5, ymax - 3, f"Cabem no MVP: {n_pk} itens, {d.loc[d['no_pacote'], 'horas_estimadas'].sum():.1f} h", ha="center", fontsize=9)
    ax.set_ylim(0, ymax)
    ax.set_xlim(0.5, len(x) + 0.7)
    ax.set_xticks(range(1, len(x) + 1, 3))
    ax.set_xlabel("Ordem de prioridade dos itens")
    ax.set_ylabel("Horas acumuladas")
    ax.set_title("Horas acumuladas pela ordem de prioridade (versão revisada)", fontsize=11)
    ax.grid(alpha=0.25)
    from matplotlib.lines import Line2D
    leg = [Line2D([0], [0], marker="D", color="w", markerfacecolor=VERDE, markeredgecolor="black", markersize=8, label="T0: exigência expressa na lei"),
           Line2D([0], [0], marker="o", color="w", markerfacecolor=AZUL, markeredgecolor="black", markersize=8, label="T1: nível A em fluxo crítico"),
           Line2D([0], [0], marker="s", color="w", markerfacecolor=LARANJA, markeredgecolor="black", markersize=8, label="T2: demais itens")]
    ax.legend(handles=leg, loc="lower right", fontsize=8, framealpha=0.95)
    fig.text(0.01, 0.005, "Fonte: base 06_grafico2_tabela.csv (dados sintéticos, set/2026). Pontos claros ficam fora da capacidade.", fontsize=7)
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    fig.savefig(GRAF / "grafico2_versao_revisada.png")
    plt.close(fig)


if __name__ == "__main__":
    main()
