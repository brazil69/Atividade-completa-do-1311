def classificar(registro: dict[str, object]) -> list[str]:
    cpu = float(registro["cpu"])
    ram = float(registro["ram"])
    uptime = float(registro["uptime"])
    resultados = []

    if uptime > 720:
        resultados.append("Reinicialização Preventiva Necessária")
    if cpu > 85 or ram > 85:
        resultados.append("Sobrecarga Crítica")
    elif cpu < 40 and ram < 40:
        resultados.append("Servidor Ocioso")
    elif 50 <= cpu <= 85 or 50 <= ram <= 85:
        resultados.append("Carga Moderada")
    else:
        resultados.append("Status: Estável")
    return resultados
