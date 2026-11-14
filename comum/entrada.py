from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class Campo:
    chave: str
    rotulo: str
    tipo: str
    minimo: int | float | None = None
    maximo: int | float | None = None


def ler_texto(mensagem: str) -> str:
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("O texto não pode ficar vazio.")


def _esta_no_intervalo(
    valor: int | float,
    minimo: int | float | None,
    maximo: int | float | None,
) -> bool:
    return (
        (minimo is None or valor >= minimo)
        and (maximo is None or valor <= maximo)
    )


def ler_inteiro(
    mensagem: str,
    minimo: int | None = None,
    maximo: int | None = None,
) -> int:
    while True:
        try:
            valor = int(input(mensagem).strip())
        except ValueError:
            print("Digite um número inteiro válido.")
            continue
        if not _esta_no_intervalo(valor, minimo, maximo):
            print(_mensagem_intervalo(minimo, maximo))
            continue
        return valor


def ler_decimal(
    mensagem: str,
    minimo: float | None = None,
    maximo: float | None = None,
) -> float:
    while True:
        try:
            valor = float(input(mensagem).strip().replace(",", "."))
        except ValueError:
            print("Digite um número válido.")
            continue
        if not isfinite(valor):
            print("Digite um número finito.")
            continue
        if not _esta_no_intervalo(valor, minimo, maximo):
            print(_mensagem_intervalo(minimo, maximo))
            continue
        return valor


def _mensagem_intervalo(
    minimo: int | float | None,
    maximo: int | float | None,
) -> str:
    if minimo is not None and maximo is not None:
        return f"Digite um valor entre {minimo} e {maximo}."
    if minimo is not None:
        return f"Digite um valor maior ou igual a {minimo}."
    if maximo is not None:
        return f"Digite um valor menor ou igual a {maximo}."
    return "Digite um valor válido."


def ler_valor(campo: Campo) -> str | int | float:
    mensagem = f"{campo.rotulo}: "
    if campo.tipo == "texto":
        return ler_texto(mensagem)
    if campo.tipo == "inteiro":
        return ler_inteiro(mensagem, campo.minimo, campo.maximo)
    if campo.tipo == "decimal":
        return ler_decimal(mensagem, campo.minimo, campo.maximo)
    raise ValueError(f"Tipo de campo desconhecido: {campo.tipo}")
