def classificar(registro: dict[str, object]) -> list[str]:
    produzido = int(registro["produzido"])
    defeitos = int(registro["defeitos"])
    setor = int(registro["setor"])
    percentual = defeitos / produzido * 100
    resultados = [f"Percentual de defeitos: {percentual:.2f}%"]

    if setor == 2:
        resultados.append("Atenção: Cadeia de Resfriamento")
    if defeitos == 0:
        resultados.append("Lote Perfeito")
    else:
        resultados.append("Lote com Incidência de Falhas")
    if percentual > 5:
        resultados.append("Lote Reprovado - Descarte")
    elif percentual >= 1:
        resultados.append("Lote em Análise / Segunda Linha")
    else:
        resultados.append("Lote Aprovado")
    return resultados
