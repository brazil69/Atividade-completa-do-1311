from comum.algoritmos import buscar_binaria, ordenar_bubble_sort
from comum.entrada import ler_inteiro, ler_texto
from comum.procedimentos import exibir_registro
from .dados import CAMPOS, ENTIDADE
from .regras import classificar


def reservar_passagens(registros: list[dict[str, object]]) -> None:
    ordenar_bubble_sort(registros)
    destino = ler_texto("Destino do voo: ")
    voo = buscar_binaria(registros, destino)
    if voo is None:
        print("Voo não encontrado.")
        return

    exibir_registro(ENTIDADE, CAMPOS, voo, classificar)
    assentos = int(voo["assentos"])
    if assentos == 0:
        print("Não há assentos disponíveis para este voo.")
        return

    quantidade = ler_inteiro(
        f"Quantidade de passagens (1 a {assentos}): ",
        1,
        assentos,
    )
    preco = float(voo["preco"])
    preco_unitario = preco * (1.15 if assentos - quantidade < 10 else 1)
    voo["assentos"] = assentos - quantidade
    print(f"Reserva confirmada: {quantidade} passagem(ns).")
    print(f"Preço por passagem: R$ {preco_unitario:.2f}")
    print(f"Total: R$ {preco_unitario * quantidade:.2f}")
    print(f"Assentos restantes: {voo['assentos']}")
