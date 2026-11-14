def classificar(registro: dict[str, object]) -> list[str]:
    temperatura = float(registro["temperatura"])
    frequencia = int(registro["frequencia"])
    pressao = int(registro["pressao"])
    resultados = []

    if pressao > 140:
        resultados.append("Alerta: Hipertensão")
    resultados.append(
        "Batimentos Regulares" if 60 <= frequencia <= 100
        else "Batimentos Irregulares"
    )
    if temperatura < 36:
        resultados.append("Hipotermia")
    elif temperatura <= 37.5:
        resultados.append("Normal")
    else:
        resultados.append("Febre")
    return resultados
