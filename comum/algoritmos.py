from unicodedata import combining, normalize
from typing import TypeVar


Registro = TypeVar("Registro", bound=dict[str, object])


def _chave_nome(nome: object) -> str:
    texto = normalize("NFD", str(nome).casefold())
    return "".join(caractere for caractere in texto if not combining(caractere))


def ordenar_bubble_sort(registros: list[Registro]) -> None:
    for fim in range(len(registros) - 1, 0, -1):
        houve_troca = False
        for indice in range(fim):
            nome_atual = _chave_nome(registros[indice]["nome"])
            proximo_nome = _chave_nome(registros[indice + 1]["nome"])
            if nome_atual > proximo_nome:
                registros[indice], registros[indice + 1] = (
                    registros[indice + 1],
                    registros[indice],
                )
                houve_troca = True
        if not houve_troca:
            break


def buscar_binaria(
    registros: list[Registro],
    nome: str,
) -> Registro | None:
    procurado = _chave_nome(nome.strip())
    inicio = 0
    fim = len(registros) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        nome_meio = _chave_nome(registros[meio]["nome"])
        if nome_meio == procurado:
            return registros[meio]
        if nome_meio < procurado:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None
