from matplotlib.patches import FancyBboxPatch, PathPatch
from matplotlib.path import Path

CORES_BAIRRO = {
    "Boa Viagem": "#0072B2",
    "Boa Vista": "#E69F00",
    "Casa Amarela": "#009E73",
    "Madalena": "#CC79A7",
    "Santo Amaro": "#56B4E9",
    "Várzea": "#D55E00",
}

COR_FLUXO = "#1F4E79"
COR_ABSTENCAO = "#C65911"
COR_BRANCO = "#8A8F98"
COR_NULO = "#5C6370"
COR_RAQUEL = "#1B7F4E"
COR_JOAO = "#2E75B6"
COR_IVAN = "#6B5B95"


def _fita(ax, x0, x1, y0_topo, y0_base, y1_topo, y1_base, cor):
    meio = (x0 + x1) / 2
    pontos = [
        (x0, y0_topo),
        (meio, y0_topo),
        (meio, y1_topo),
        (x1, y1_topo),
        (x1, y1_base),
        (meio, y1_base),
        (meio, y0_base),
        (x0, y0_base),
        (x0, y0_topo),
    ]
    codigos = [
        Path.MOVETO,
        Path.CURVE4,
        Path.CURVE4,
        Path.CURVE4,
        Path.LINETO,
        Path.CURVE4,
        Path.CURVE4,
        Path.CURVE4,
        Path.CLOSEPOLY,
    ]
    ax.add_patch(
        PathPatch(
            Path(pontos, codigos),
            facecolor=cor,
            edgecolor="none",
            alpha=0.38,
            lw=0,
            zorder=1,
        )
    )


def _espalhar_rotulos(centros, minimo=0.07, piso=0.06, teto=0.94):
    posicoes = list(centros)
    for indice in range(1, len(posicoes)):
        if posicoes[indice - 1] - posicoes[indice] < minimo:
            posicoes[indice] = posicoes[indice - 1] - minimo
    if posicoes and posicoes[-1] < piso:
        ajuste = piso - posicoes[-1]
        posicoes = [min(teto, valor + ajuste) for valor in posicoes]
    return posicoes


def _caixa(ax, x, y_base, largura, altura, cor):
    ax.add_patch(
        FancyBboxPatch(
            (x, y_base),
            largura,
            altura,
            boxstyle="round,pad=0.001,rounding_size=0.004",
            facecolor=cor,
            edgecolor="white",
            linewidth=0.6,
            mutation_aspect=0.3,
            zorder=3,
        )
    )


def _empilhar(itens, topo, altura_util, folga):
    """itens: lista de (nome, valor, cor). Alturas proporcionais ao valor."""
    total = sum(valor for _, valor, _ in itens)
    folgas = folga * (len(itens) - 1)
    util = altura_util - folgas
    cursor = topo
    blocos = []
    for nome, valor, cor in itens:
        altura = util * valor / total
        base = cursor - altura
        blocos.append(
            {
                "nome": nome,
                "valor": valor,
                "cor": cor,
                "topo": cursor,
                "base": base,
            }
        )
        cursor = base - folga
    return blocos


def desenhar_sankey(ax, resumo, inteiro_br):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    topo = 0.90
    altura = 0.78
    folga = 0.028
    largura = 0.018
    xs = [0.02, 0.30, 0.56, 0.80]

    coluna_1 = _empilhar(
        [
            ("Compareceram", resumo["comparecimento"], COR_FLUXO),
            ("Abstenção", resumo["abstencao"], COR_ABSTENCAO),
        ],
        topo,
        altura,
        folga,
    )
    compareceram, abstencao = coluna_1

    coluna_2 = _empilhar(
        [
            ("Votos válidos", resumo["votos_validos"], COR_FLUXO),
            ("Nulos", resumo["nulos"], COR_NULO),
            ("Brancos", resumo["brancos"], COR_BRANCO),
        ],
        compareceram["topo"],
        compareceram["topo"] - compareceram["base"],
        0.02,
    )
    validos, nulos, brancos = coluna_2

    coluna_3 = _empilhar(
        [
            ("Raquel Lima", resumo["raquel_lima"], COR_RAQUEL),
            ("João Capim", resumo["joao_capim"], COR_JOAO),
            ("Ivan Pinto", resumo["ivan_pinto"], COR_IVAN),
        ],
        validos["topo"],
        validos["topo"] - validos["base"],
        0.018,
    )

    aptos_topo = compareceram["topo"]
    altura_aptos = (compareceram["topo"] - compareceram["base"]) + (
        abstencao["topo"] - abstencao["base"]
    )
    aptos_base = aptos_topo - altura_aptos
    corte = aptos_topo - altura_aptos * (
        resumo["comparecimento"] / resumo["eleitores_aptos"]
    )

    _fita(
        ax,
        xs[0] + largura,
        xs[1],
        aptos_topo,
        corte,
        compareceram["topo"],
        compareceram["base"],
        COR_FLUXO,
    )
    _fita(
        ax,
        xs[0] + largura,
        xs[1],
        corte,
        aptos_base,
        abstencao["topo"],
        abstencao["base"],
        COR_ABSTENCAO,
    )

    cursor = compareceram["topo"]
    faixa = compareceram["topo"] - compareceram["base"]
    for bloco in coluna_2:
        trecho = faixa * bloco["valor"] / resumo["comparecimento"]
        _fita(
            ax,
            xs[1] + largura,
            xs[2],
            cursor,
            cursor - trecho,
            bloco["topo"],
            bloco["base"],
            bloco["cor"],
        )
        cursor -= trecho

    cursor = validos["topo"]
    faixa = validos["topo"] - validos["base"]
    for bloco in coluna_3:
        trecho = faixa * bloco["valor"] / resumo["votos_validos"]
        _fita(
            ax,
            xs[2] + largura,
            xs[3],
            cursor,
            cursor - trecho,
            bloco["topo"],
            bloco["base"],
            bloco["cor"],
        )
        cursor -= trecho

    _caixa(ax, xs[0], aptos_base, largura, altura_aptos, COR_FLUXO)
    for bloco, x in (
        *[(item, xs[1]) for item in coluna_1],
        *[(item, xs[2]) for item in coluna_2],
        *[(item, xs[3]) for item in coluna_3],
    ):
        _caixa(ax, x, bloco["base"], largura, bloco["topo"] - bloco["base"], bloco["cor"])

    ax.text(
        xs[0] + largura + 0.012,
        (aptos_topo + aptos_base) / 2,
        f"Eleitores aptos\n{inteiro_br(resumo['eleitores_aptos'])}",
        va="center",
        ha="left",
        fontsize=7.5,
        color="#1A1A1A",
        linespacing=1.15,
    )

    rotulos = [
        (xs[1], coluna_1, 0.055),
        (xs[2], coluna_2, 0.078),
        (xs[3], coluna_3, 0.07),
    ]
    for x, blocos, minimo in rotulos:
        centros = [(bloco["topo"] + bloco["base"]) / 2 for bloco in blocos]
        posicoes = _espalhar_rotulos(centros, minimo=minimo)
        for bloco, centro, posicao in zip(blocos, centros, posicoes):
            if abs(posicao - centro) > 0.012:
                ax.plot(
                    [x + largura, x + largura + 0.012],
                    [centro, posicao],
                    color="#8A93A0",
                    lw=0.5,
                    zorder=2,
                )
            ax.text(
                x + largura + 0.016,
                posicao,
                f"{bloco['nome']}\n{inteiro_br(bloco['valor'])}",
                va="center",
                ha="left",
                fontsize=6.6,
                color="#1A1A1A",
                linespacing=1.05,
                zorder=4,
            )



def desenhar_bolhas(ax, tabela, resumo, percentual_br):
    maior_eleitorado = tabela["eleitores_aptos"].max()
    for bairro, cor in CORES_BAIRRO.items():
        parte = tabela[tabela["bairro"] == bairro]
        ax.scatter(
            parte["taxa_abstencao"] * 100,
            parte["percentual_raquel_nos_validos"] * 100,
            s=parte["eleitores_aptos"] / maior_eleitorado * 420,
            c=cor,
            alpha=0.88,
            edgecolors="white",
            linewidths=0.6,
            label=bairro,
            zorder=3,
        )

    taxa_cidade = 100 * resumo["abstencao"] / resumo["eleitores_aptos"]
    ax.axvline(taxa_cidade, color="#C65911", lw=0.8, ls="--", zorder=1)
    ax.axhline(50, color="#5C6370", lw=0.8, ls="--", zorder=1)
    ax.text(
        taxa_cidade - 0.5,
        82.6,
        f"taxa do recorte, {percentual_br(resumo['abstencao'], resumo['eleitores_aptos'])}",
        color="#C65911",
        fontsize=6.4,
        va="top",
        ha="right",
    )
    ax.text(
        40.6,
        51.3,
        "linha dos 50%",
        color="#5C6370",
        fontsize=6.4,
        va="bottom",
        ha="right",
    )

    destaques = tabela[tabela["secao_id"].isin(["SEC021", "SEC022", "SEC024"])]
    deslocamentos = {"SEC021": (0.4, 1.3), "SEC022": (0.4, -2.6), "SEC024": (-3.6, 1.2)}
    for _, linha in destaques.iterrows():
        dx, dy = deslocamentos[linha["secao_id"]]
        ax.annotate(
            linha["secao_id"],
            (
                linha["taxa_abstencao"] * 100,
                linha["percentual_raquel_nos_validos"] * 100,
            ),
            xytext=(
                linha["taxa_abstencao"] * 100 + dx,
                linha["percentual_raquel_nos_validos"] * 100 + dy,
            ),
            fontsize=7,
            color="#1A1A1A",
            arrowprops={"arrowstyle": "-", "color": "#1A1A1A", "lw": 0.4},
        )

    ax.set_xlim(9, 42)
    ax.set_ylim(42, 84)
    ax.set_xlabel("Taxa de abstenção da seção (%)", fontsize=8)
    ax.set_ylabel("Raquel Lima nos votos válidos da seção (%)", fontsize=8)
    ax.tick_params(labelsize=7.5)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="both", color="#E6E6E6", lw=0.6, zorder=0)
    legenda = ax.legend(
        frameon=True,
        framealpha=0.94,
        edgecolor="#E6E6E6",
        fontsize=6.3,
        loc="upper right",
        title="Bairro",
        title_fontsize=6.5,
    )
    for marca in legenda.legend_handles:
        marca.set_sizes([36])
    ax.set_axisbelow(True)
