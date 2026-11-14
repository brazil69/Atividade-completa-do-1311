def classificar(registro: dict[str, object]) -> list[str]:
    assentos = int(registro["assentos"])
    preco = float(registro["preco"])
    resultados = []

    if assentos > 0:
        resultados.append("Passagens à Venda")
    else:
        resultados.append("Voo Esgotado")
    if assentos == 50:
        resultados.append("Voo Sem Demanda")
    if 0 < assentos < 10:
        resultados.append("Últimas Vagas - Aplicar Taxa de 15%")
    resultados.append(
        "Tarifa Executiva / VIP" if preco > 1500 else "Preço Padrão"
    )
    return resultados
