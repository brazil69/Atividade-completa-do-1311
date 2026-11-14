def classificar(registro: dict[str, object]) -> list[str]:
    nota1 = float(registro["nota1"])
    nota2 = float(registro["nota2"])
    faltas = int(registro["faltas"])
    media = (nota1 + nota2) / 2
    resultados = [f"Média: {media:.2f}"]

    if faltas > 20:
        resultados.append("Reprovado por Faltas")
    resultados.append(
        "Desempenho em Queda" if nota1 > nota2
        else "Desempenho em Evolução"
    )
    if media >= 7:
        resultados.append("Aprovado")
    elif media >= 5:
        resultados.append("Recuperação")
    else:
        resultados.append("Reprovado por Nota")
    return resultados
