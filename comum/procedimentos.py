from collections.abc import Callable

from comum.algoritmos import buscar_binaria, ordenar_bubble_sort
from comum.entrada import Campo, ler_inteiro, ler_texto, ler_valor


def _formatar_valor(valor: object) -> str:
    if isinstance(valor, float):
        return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return str(valor)


def exibir_registro(
    entidade: str,
    campos: tuple[Campo, ...],
    registro: dict[str, object],
    classificar: Callable[[dict[str, object]], list[str]],
) -> None:
    print(f"\n{entidade}: {registro['nome']}")
    for campo in campos:
        print(f"  {campo.rotulo}: {_formatar_valor(registro[campo.chave])}")
    for resultado in classificar(registro):
        print(f"  - {resultado}")


def cadastrar_registros(
    entidade: str,
    campos: tuple[Campo, ...],
) -> list[dict[str, object]]:
    registros: list[dict[str, object]] = []
    print(f"\nCadastro de 5 {entidade.lower()}(s)")

    for numero in range(1, 6):
        print(f"\n{entidade} {numero}/5")
        while True:
            nome = ler_texto(f"Nome de {entidade.lower()}: ")
            if any(
                str(registro["nome"]).casefold() == nome.casefold()
                for registro in registros
            ):
                print("Esse nome já foi cadastrado. Digite um nome diferente.")
                continue
            break

        registro: dict[str, object] = {"nome": nome}
        for campo in campos:
            registro[campo.chave] = ler_valor(campo)
        registros.append(registro)
    return registros


def cadastrar_registro(
    entidade: str,
    campos: tuple[Campo, ...],
) -> dict[str, object]:
    print(f"\nCadastro de {entidade.lower()}")
    registro: dict[str, object] = {"nome": ler_texto(f"Nome de {entidade.lower()}: ")}
    for campo in campos:
        registro[campo.chave] = ler_valor(campo)
    return registro


def selecionar_registro(
    entidade: str,
    registros: list[dict[str, object]],
) -> dict[str, object]:
    print(f"\nSelecione o(a) {entidade.lower()}:")
    for numero, registro in enumerate(registros, start=1):
        print(f"{numero} - {registro['nome']}")
    return registros[ler_inteiro("Número do registro: ", 1, len(registros)) - 1]


def editar_registro(
    entidade: str,
    campos: tuple[Campo, ...],
    registro: dict[str, object],
) -> None:
    print(f"\nEditando {entidade.lower()}: {registro['nome']}")
    print("0 - Nome")
    for numero, campo in enumerate(campos, start=1):
        print(f"{numero} - {campo.rotulo}")
    opcao = ler_inteiro("Qual dado deseja editar? ", 0, len(campos))
    if opcao == 0:
        registro["nome"] = ler_texto(f"Novo nome de {entidade.lower()}: ")
    else:
        campo = campos[opcao - 1]
        registro[campo.chave] = ler_valor(campo)


def listar_registros(
    entidade: str,
    campos: tuple[Campo, ...],
    registros: list[dict[str, object]],
    classificar: Callable[[dict[str, object]], list[str]],
) -> None:
    for registro in registros:
        exibir_registro(entidade, campos, registro, classificar)


def ordenar_registros(
    entidade: str,
    campos: tuple[Campo, ...],
    registros: list[dict[str, object]],
    classificar: Callable[[dict[str, object]], list[str]],
) -> None:
    ordenar_bubble_sort(registros)
    print(f"\n{entidade}s ordenados por nome:")
    listar_registros(entidade, campos, registros, classificar)


def pesquisar_registro(
    entidade: str,
    campos: tuple[Campo, ...],
    registros: list[dict[str, object]],
    classificar: Callable[[dict[str, object]], list[str]],
) -> None:
    ordenar_bubble_sort(registros)
    nome = ler_texto(f"Nome de {entidade.lower()} para pesquisar: ")
    registro = buscar_binaria(registros, nome)
    if registro is None:
        print(f"{entidade} não encontrado(a).")
        return
    exibir_registro(entidade, campos, registro, classificar)
