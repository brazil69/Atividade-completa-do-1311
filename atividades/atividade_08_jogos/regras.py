from datetime import date


def classificar(registro: dict[str, object]) -> list[str]:
    ano = int(registro["ano"])
    classificacao = int(registro["classificacao"])
    diaria = float(registro["diaria"])
    diaria_final = diaria + (5 if ano == date.today().year else 0)
    resultados = []

    if ano == date.today().year:
        resultados.append("Taxa de Lançamento Aplicada: R$ 5,00")
    resultados.append(
        f"Diária final: R$ {diaria_final:.2f} "
        f"({'Categoria Premium' if diaria_final > 20 else 'Categoria Standard'})"
    )
    if classificacao == 0:
        resultados.append("Livre")
    elif classificacao < 16:
        resultados.append("Recomendado para Adolescentes")
    elif classificacao == 18:
        resultados.append("Exclusivo para Adultos")
    else:
        resultados.append("Classificação indicativa não definida no enunciado")
    return resultados
