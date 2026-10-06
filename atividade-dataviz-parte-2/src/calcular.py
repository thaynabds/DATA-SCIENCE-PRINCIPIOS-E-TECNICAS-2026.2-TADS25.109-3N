from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
PASTA_DADOS = RAIZ / "dados"
PASTA_ENTREGA = RAIZ / "entrega"

TOTAIS_ESPERADOS = {
    "eleitores_aptos": 33970,
    "comparecimento": 26232,
    "abstencao": 7738,
    "votos_validos": 24215,
    "brancos": 767,
    "nulos": 1250,
    "raquel_lima": 15546,
    "joao_capim": 8499,
    "ivan_pinto": 170,
}


def inteiro_br(valor):
    return f"{int(valor):,}".replace(",", ".")


def percentual(parte, todo, casas=2):
    return round(100 * parte / todo, casas)


def percentual_br(parte, todo, casas=2):
    texto = f"{percentual(parte, todo, casas):.{casas}f}"
    return texto.replace(".", ",") + "%"


def carregar_bases():
    votos = pd.read_csv(
        PASTA_DADOS / "01_Votos_Simulados.csv",
        sep=";",
        encoding="utf-8-sig",
    )
    secoes = pd.read_csv(
        PASTA_DADOS / "02_Secoes_Eleitorais.csv",
        sep=";",
        encoding="utf-8-sig",
    )
    votos.columns = [coluna.strip() for coluna in votos.columns]
    secoes.columns = [coluna.strip() for coluna in secoes.columns]
    for coluna in ("secao_id", "tipo_voto", "candidato", "bairro"):
        if coluna in votos.columns:
            votos[coluna] = votos[coluna].astype(str).str.strip()
        if coluna in secoes.columns:
            secoes[coluna] = secoes[coluna].astype(str).str.strip()
    secoes["eleitores_aptos"] = secoes["eleitores_aptos"].astype(int)
    return votos, secoes


def montar_secoes(votos, secoes):
    contagem = (
        votos.groupby(["secao_id", "tipo_voto"], observed=True)
        .size()
        .unstack(fill_value=0)
    )
    for tipo in ("VALIDO", "BRANCO", "NULO"):
        if tipo not in contagem.columns:
            contagem[tipo] = 0

    validos = votos[votos["tipo_voto"] == "VALIDO"]
    por_candidato = (
        validos.groupby(["secao_id", "candidato"], observed=True)
        .size()
        .unstack(fill_value=0)
    )
    for nome in ("Raquel Lima", "João Capim", "Ivan Pinto"):
        if nome not in por_candidato.columns:
            por_candidato[nome] = 0

    tabela = secoes.merge(contagem, left_on="secao_id", right_index=True, how="left")
    tabela = tabela.merge(por_candidato, left_on="secao_id", right_index=True, how="left")
    tabela[["VALIDO", "BRANCO", "NULO"]] = tabela[["VALIDO", "BRANCO", "NULO"]].fillna(0)
    tabela[["Raquel Lima", "João Capim", "Ivan Pinto"]] = tabela[
        ["Raquel Lima", "João Capim", "Ivan Pinto"]
    ].fillna(0)

    tabela["comparecimento"] = tabela["VALIDO"] + tabela["BRANCO"] + tabela["NULO"]
    tabela["abstencao"] = tabela["eleitores_aptos"] - tabela["comparecimento"]
    tabela["taxa_abstencao"] = tabela["abstencao"] / tabela["eleitores_aptos"]
    tabela["votos_validos"] = tabela["VALIDO"].astype(int)
    tabela["percentual_raquel_nos_validos"] = tabela["Raquel Lima"] / tabela["votos_validos"]

    def vencedor(linha):
        placar = {
            "Raquel Lima": linha["Raquel Lima"],
            "João Capim": linha["João Capim"],
            "Ivan Pinto": linha["Ivan Pinto"],
        }
        return max(placar, key=placar.get)

    tabela["vencedor_secao"] = tabela.apply(vencedor, axis=1)
    return tabela.sort_values(
        ["taxa_abstencao", "secao_id"],
        ascending=[False, True],
    ).reset_index(drop=True)


def resumir(votos, tabela):
    aptos = int(tabela["eleitores_aptos"].sum())
    comparecimento = int(len(votos))
    abstencao = aptos - comparecimento
    validos = int((votos["tipo_voto"] == "VALIDO").sum())
    brancos = int((votos["tipo_voto"] == "BRANCO").sum())
    nulos = int((votos["tipo_voto"] == "NULO").sum())
    raquel = int(
        ((votos["tipo_voto"] == "VALIDO") & (votos["candidato"] == "Raquel Lima")).sum()
    )
    joao = int(
        ((votos["tipo_voto"] == "VALIDO") & (votos["candidato"] == "João Capim")).sum()
    )
    ivan = int(
        ((votos["tipo_voto"] == "VALIDO") & (votos["candidato"] == "Ivan Pinto")).sum()
    )
    return {
        "eleitores_aptos": aptos,
        "comparecimento": comparecimento,
        "abstencao": abstencao,
        "votos_validos": validos,
        "brancos": brancos,
        "nulos": nulos,
        "raquel_lima": raquel,
        "joao_capim": joao,
        "ivan_pinto": ivan,
        "saidas_branco_nulo": brancos + nulos,
    }


def conferir(votos, secoes, tabela, resumo):
    erros = []

    if votos["id_voto"].duplicated().any():
        erros.append("Ha voto repetido.")
    if set(votos["secao_id"]) != set(secoes["secao_id"]):
        erros.append("As secoes das duas bases nao batem.")
    if (tabela["comparecimento"] > tabela["eleitores_aptos"]).any():
        erros.append("Uma secao tem mais votos do que eleitores aptos.")
    if (tabela["abstencao"] < 0).any():
        erros.append("Abstenção negativa.")
    if int(tabela["comparecimento"].sum()) != int(len(votos)):
        erros.append("A soma do comparecimento por secao nao fecha com a base de votos.")

    tipos = set(votos["tipo_voto"])
    if tipos != {"VALIDO", "BRANCO", "NULO"}:
        erros.append(f"Tipo de voto fora do esperado: {tipos}")

    candidatos_validos = set(votos.loc[votos["tipo_voto"] == "VALIDO", "candidato"])
    if candidatos_validos != {"Raquel Lima", "João Capim", "Ivan Pinto"}:
        erros.append(f"Candidato fora do esperado: {candidatos_validos}")

    fora_do_valido = set(votos.loc[votos["tipo_voto"] != "VALIDO", "candidato"])
    if fora_do_valido != {"NAO_SE_APLICA"}:
        erros.append("Branco ou nulo esta ligado a um candidato.")

    for chave, valor in TOTAIS_ESPERADOS.items():
        if resumo[chave] != valor:
            erros.append(f"{chave} deu {resumo[chave]}, o esperado era {valor}.")

    soma_aptos = resumo["comparecimento"] + resumo["abstencao"]
    if soma_aptos != resumo["eleitores_aptos"]:
        erros.append("Aptos nao fecham com comparecimento mais abstenção.")

    soma_presentes = resumo["votos_validos"] + resumo["brancos"] + resumo["nulos"]
    if soma_presentes != resumo["comparecimento"]:
        erros.append("Comparecimento nao fecha com validos, brancos e nulos.")

    soma_validos = resumo["raquel_lima"] + resumo["joao_capim"] + resumo["ivan_pinto"]
    if soma_validos != resumo["votos_validos"]:
        erros.append("Votos validos nao fecham com os tres candidatos.")

    partes = [
        percentual(resumo["raquel_lima"], resumo["votos_validos"]),
        percentual(resumo["joao_capim"], resumo["votos_validos"]),
        percentual(resumo["ivan_pinto"], resumo["votos_validos"]),
    ]
    if round(sum(partes), 2) != 100:
        erros.append(f"Os percentuais dos candidatos nao fecham em 100: {partes}")

    sec021 = tabela.loc[tabela["secao_id"] == "SEC021"].iloc[0]
    if int(sec021["abstencao"]) != 304 or int(sec021["eleitores_aptos"]) != 800:
        erros.append("A conta da SEC021 mudou.")
    if tabela.iloc[0]["secao_id"] != "SEC021":
        erros.append("A maior taxa de abstenção nao ficou na SEC021.")

    if erros:
        raise ValueError("Conferencia falhou: " + " ".join(erros))


def salvar_tabelas(tabela, resumo):
    PASTA_ENTREGA.mkdir(parents=True, exist_ok=True)
    colunas = [
        "secao_id",
        "bairro",
        "eleitores_aptos",
        "comparecimento",
        "abstencao",
        "taxa_abstencao",
        "votos_validos",
        "BRANCO",
        "NULO",
        "Raquel Lima",
        "João Capim",
        "Ivan Pinto",
        "vencedor_secao",
        "percentual_raquel_nos_validos",
    ]
    saida = tabela[colunas].copy()
    saida["taxa_abstencao"] = (saida["taxa_abstencao"] * 100).round(2)
    saida["percentual_raquel_nos_validos"] = (
        saida["percentual_raquel_nos_validos"] * 100
    ).round(2)
    saida = saida.rename(
        columns={
            "BRANCO": "brancos",
            "NULO": "nulos",
            "Raquel Lima": "votos_raquel_lima",
            "João Capim": "votos_joao_capim",
            "Ivan Pinto": "votos_ivan_pinto",
            "taxa_abstencao": "taxa_abstencao_percentual",
            "percentual_raquel_nos_validos": "raquel_nos_votos_validos_percentual",
        }
    )
    saida.to_csv(PASTA_ENTREGA / "secoes_calculadas.csv", index=False, sep=";")

    resumo_df = pd.DataFrame([resumo])
    resumo_df.to_csv(PASTA_ENTREGA / "totais.csv", index=False, sep=";")
    return saida
