def classificar(registro: dict[str, object]) -> list[str]:
    orcado = float(registro["orcado"])
    gasto = float(registro["gasto"])
    prioridade = int(registro["prioridade"])
    resultados = []

    if gasto > orcado:
        resultados.append("Alerta: Orçamento Estourado!")
    elif gasto < orcado / 2:
        resultados.append("Economia Excelente")
    else:
        resultados.append("Gasto Dentro do Previsto")
    resultados.append(
        {1: "Despesa Essencial", 2: "Despesa Útil", 3: "Despesa Supérflua"}[
            prioridade
        ]
    )
    return resultados
