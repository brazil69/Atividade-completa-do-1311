def classificar(registro: dict[str, object]) -> list[str]:
    quilometragem = int(registro["quilometragem"])
    consumo = float(registro["consumo"])
    capacidade = float(registro["capacidade"])
    resultados = []

    if consumo < 6:
        resultados.append("Aviso: Alto Custo de Combustível")
    resultados.append("Porte: Pesado" if capacidade > 2000 else "Porte: Leve")
    if quilometragem <= 20_000:
        resultados.append("Revisão Leve")
    elif quilometragem <= 60_000:
        resultados.append("Revisão Geral")
    else:
        resultados.append("Troca de Componentes Pesados")
    return resultados
