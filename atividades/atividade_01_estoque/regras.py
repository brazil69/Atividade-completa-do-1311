def classificar(registro: dict[str, object]) -> list[str]:
    quantidade = int(registro["quantidade"])
    custo = float(registro["custo"])
    venda = float(registro["venda"])
    resultados = []

    if venda < custo:
        resultados.append("Alerta: Prejuízo!")
    resultados.append("Disponível" if quantidade > 0 else "Indisponível")
    if quantidade < 10:
        resultados.append("Estoque Crítico")
    elif quantidade <= 50:
        resultados.append("Estoque Normal")
    else:
        resultados.append("Estoque Alto")
    return resultados
