def classificar(registro: dict[str, object]) -> list[str]:
    total_vendido = float(registro["total_vendido"])
    imoveis = int(registro["imoveis"])
    satisfacao = float(registro["satisfacao"])
    resultados = []

    if total_vendido > 1_000_000:
        total_vendido += 2000
        resultados.append("Super Meta Atingida! Bônus de R$ 2.000,00 aplicado")
        resultados.append(f"Total com bônus: R$ {total_vendido:.2f}")
    resultados.append(
        "Excelente Atendimento" if satisfacao >= 4
        else "Treinamento Necessário"
    )
    if imoveis > 5:
        resultados.append("Meta Ouro")
    elif 2 <= imoveis <= 4:
        resultados.append("Meta Prata")
    elif imoveis < 2:
        resultados.append("Abaixo da Meta")
    else:
        resultados.append("Meta de vendas não definida no enunciado")
    return resultados
