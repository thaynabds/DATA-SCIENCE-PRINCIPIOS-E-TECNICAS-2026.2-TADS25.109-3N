import textwrap

import matplotlib.pyplot as plt

from src.calcular import (
    PASTA_ENTREGA,
    carregar_bases,
    conferir,
    inteiro_br,
    montar_secoes,
    percentual_br,
    resumir,
    salvar_tabelas,
)
from src.graficos import desenhar_bolhas, desenhar_sankey

plt.rcParams["font.family"] = "DejaVu Sans"


def _linha_secao(tabela, secao_id):
    linha = tabela.loc[tabela["secao_id"] == secao_id].iloc[0]
    return (
        f"{secao_id}, {linha['bairro']}: "
        f"{inteiro_br(linha['abstencao'])} de {inteiro_br(linha['eleitores_aptos'])} aptos, "
        f"{percentual_br(linha['abstencao'], linha['eleitores_aptos'])}"
    )


def _texto(resumo, tabela):
    raquel = percentual_br(resumo["raquel_lima"], resumo["votos_validos"])
    joao = percentual_br(resumo["joao_capim"], resumo["votos_validos"])
    ivan = percentual_br(resumo["ivan_pinto"], resumo["votos_validos"])
    taxa = percentual_br(resumo["abstencao"], resumo["eleitores_aptos"])

    madalena = tabela[tabela["bairro"] == "Madalena"]
    validos_madalena = int(madalena["votos_validos"].sum())
    joao_madalena = int(madalena["João Capim"].sum())
    secoes_joao = sorted(
        tabela.loc[tabela["vencedor_secao"] == "João Capim", "secao_id"]
    )
    if secoes_joao != ["SEC013", "SEC015", "SEC016"]:
        raise ValueError(f"Secoes em que João venceu mudaram: {secoes_joao}")
    if int(joao_madalena) != 1666 or validos_madalena != 3292:
        raise ValueError("Conta da Madalena mudou.")

    sec012 = tabela.loc[tabela["secao_id"] == "SEC012"].iloc[0]
    if int(sec012["abstencao"]) != int(tabela["abstencao"].max()):
        raise ValueError("A maior quantidade de abstenções não está na SEC012.")

    escolha = (
        "Comparei os gráficos da aula e fiquei com dois. "
        "O dumbbell pede a mesma categoria em dois momentos. Aqui há uma eleição só. "
        "O treemap serve para partes que somam um total. Taxa de abstenção não soma. "
        "A cascata sai de um saldo e chega em outro, sem mostrar candidato nem seção. "
        "O funil mostra quantos passaram em cada etapa, sem mostrar para quem foi o voto. "
        "O mapa precisaria do desenho do bairro. A base só tem o nome, então não inventei mapa. "
        "O Sankey mostra o caminho de todos os aptos. As bolhas mostram cada seção com três medidas: "
        "taxa de abstenção, parte da Raquel nos votos válidos e, na área, quantos aptos a seção tem. "
        "Se a quantidade fosse 4 vezes maior, o raio só dobraria, porque a área é que representa o valor."
    )
    conclusao = (
        f"Raquel Lima venceu, com {inteiro_br(resumo['raquel_lima'])} votos válidos "
        f"de {inteiro_br(resumo['votos_validos'])}. "
        f"A conta é {inteiro_br(resumo['raquel_lima'])} dividido por "
        f"{inteiro_br(resumo['votos_validos'])}, ou seja, {raquel} dos votos válidos. "
        f"João Capim teve {inteiro_br(resumo['joao_capim'])} ({joao}). "
        f"Ivan Pinto teve {inteiro_br(resumo['ivan_pinto'])} ({ivan}). "
        f"Branco e nulo entram no comparecimento e ficam de fora dessa conta. "
        f"Se abstiveram {inteiro_br(resumo['abstencao'])} eleitores: "
        f"{inteiro_br(resumo['eleitores_aptos'])} aptos menos "
        f"{inteiro_br(resumo['comparecimento'])} presentes. "
        f"A taxa é {inteiro_br(resumo['abstencao'])} dividido por "
        f"{inteiro_br(resumo['eleitores_aptos'])}, ou seja, {taxa} dos aptos. "
        f"Maior taxa: {_linha_secao(tabela, 'SEC021')}. "
        f"Depois, {_linha_secao(tabela, 'SEC022')}. "
        f"Depois, {_linha_secao(tabela, 'SEC024')}. "
        f"A SEC012, Boa Vista, teve mais abstenções em quantidade, "
        f"{inteiro_br(sec012['abstencao'])}. A taxa foi menor: "
        f"{inteiro_br(sec012['abstencao'])} de {inteiro_br(sec012['eleitores_aptos'])}, "
        f"{percentual_br(sec012['abstencao'], sec012['eleitores_aptos'])}. "
        f"Nas seções SEC013, SEC015 e SEC016, da Madalena, João Capim teve mais votos válidos. "
        f"No bairro, foram {inteiro_br(joao_madalena)} de {inteiro_br(validos_madalena)}. "
        "Isso não muda a vitória de Raquel no recorte."
    )
    conferencia = (
        f"Conferência: {inteiro_br(resumo['eleitores_aptos'])} = "
        f"{inteiro_br(resumo['comparecimento'])} + {inteiro_br(resumo['abstencao'])}. "
        f"{inteiro_br(resumo['comparecimento'])} = {inteiro_br(resumo['votos_validos'])} + "
        f"{inteiro_br(resumo['nulos'])} + {inteiro_br(resumo['brancos'])}. "
        f"{inteiro_br(resumo['votos_validos'])} = {inteiro_br(resumo['raquel_lima'])} + "
        f"{inteiro_br(resumo['joao_capim'])} + {inteiro_br(resumo['ivan_pinto'])}."
    )
    return escolha, conclusao, conferencia


def _bloco(fig, x, y, titulo, texto, tamanho=7.15, largura_caracteres=128):
    fig.text(x, y, titulo, fontsize=9, color="#1A1A1A", ha="left", va="top")
    linhas = textwrap.wrap(texto, width=largura_caracteres)
    fig.text(
        x,
        y - 0.026,
        "\n".join(linhas),
        fontsize=tamanho,
        color="#243040",
        ha="left",
        va="top",
        linespacing=1.25,
    )
    altura_linha = (tamanho * 1.25) / 72 / 8.27
    return y - 0.026 - altura_linha * len(linhas) - 0.012


def gerar():
    PASTA_ENTREGA.mkdir(parents=True, exist_ok=True)
    votos, secoes = carregar_bases()
    tabela = montar_secoes(votos, secoes)
    resumo = resumir(votos, tabela)
    conferir(votos, secoes, tabela, resumo)
    salvar_tabelas(tabela, resumo)
    escolha, conclusao, conferencia = _texto(resumo, tabela)

    (PASTA_ENTREGA / "conferencia.txt").write_text(
        conferencia + "\n\nEscolha\n" + escolha + "\n\nConclusao\n" + conclusao + "\n",
        encoding="utf-8",
    )

    figura = plt.figure(figsize=(11.69, 8.27), dpi=150, facecolor="white")
    figura.text(
        0.045,
        0.978,
        "Faculdade Senac Pernambuco  |  ADS  |  Data Science: Princípios e Técnicas  |  2026.2",
        fontsize=8,
        color="#1F4E79",
        ha="left",
        va="top",
    )
    figura.text(
        0.045,
        0.954,
        "Atividade DataViz parte 2  |  Prof. Rodrigo Rios  |  Aluna: Thayná Batista da Silva  |  Recife-PE  |  06/10/2026",
        fontsize=8,
        color="#3D4C5C",
        ha="left",
        va="top",
    )
    figura.text(
        0.045,
        0.922,
        "Votação simulada para governador no Recife",
        fontsize=15,
        color="#1A1A1A",
        ha="left",
        va="top",
    )
    figura.text(
        0.045,
        0.892,
        "Recorte didático. Um voto por eleitor presente. Branco e nulo contam como comparecimento, não como voto válido.",
        fontsize=8,
        color="#3D4C5C",
        ha="left",
        va="top",
    )
    figura.text(
        0.045,
        0.862,
        "1. Caminho dos eleitores aptos",
        fontsize=11,
        color="#1A1A1A",
        ha="left",
        va="top",
    )
    figura.text(
        0.575,
        0.862,
        "2. Seções: taxa, votos da Raquel e aptos na área",
        fontsize=11,
        color="#1A1A1A",
        ha="left",
        va="top",
    )

    ax_sankey = figura.add_axes([0.03, 0.445, 0.50, 0.395])
    ax_bolhas = figura.add_axes([0.575, 0.445, 0.38, 0.395])
    desenhar_sankey(ax_sankey, resumo, inteiro_br)
    desenhar_bolhas(ax_bolhas, tabela, resumo, percentual_br)

    y_texto = _bloco(figura, 0.045, 0.428, "Por que estes dois gráficos", escolha)
    _bloco(figura, 0.045, y_texto, "O que os números mostram", conclusao)
    figura.text(
        0.045,
        0.058,
        conferencia,
        fontsize=7.1,
        color="#1A1A1A",
        ha="left",
        va="center",
    )
    figura.text(
        0.045,
        0.028,
        "Fontes: aula DataViz parte 2, prof. Rodrigo Rios, Senac PE. "
        "Google, Sankey diagram, Google for Developers. "
        "Wilke, C. O. Fundamentals of Data Visualization. O'Reilly, 2019. clauswilke.com/dataviz. "
        "Sem malha do IBGE na base, por isso não há mapa.",
        fontsize=6,
        color="#5C6370",
        ha="left",
        va="center",
    )

    pdf = PASTA_ENTREGA / "pagina.pdf"
    figura.savefig(pdf, format="pdf")
    figura.savefig(PASTA_ENTREGA / "pagina.png", format="png")

    figura_sankey, eixo_sankey = plt.subplots(figsize=(10, 5.6), dpi=150)
    desenhar_sankey(eixo_sankey, resumo, inteiro_br)
    figura_sankey.tight_layout()
    figura_sankey.savefig(PASTA_ENTREGA / "grafico_sankey.png", dpi=150)
    plt.close(figura_sankey)

    figura_bolhas, eixo_bolhas = plt.subplots(figsize=(8.2, 5.6), dpi=150)
    desenhar_bolhas(eixo_bolhas, tabela, resumo, percentual_br)
    figura_bolhas.tight_layout()
    figura_bolhas.savefig(PASTA_ENTREGA / "grafico_bolhas.png", dpi=150)
    plt.close(figura_bolhas)
    plt.close(figura)
    return pdf


if __name__ == "__main__":
    caminho = gerar()
    print(caminho)
