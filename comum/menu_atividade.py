from collections.abc import Callable
from pathlib import Path

from comum.banco_dados import (
    atualizar_registro,
    carregar_registros,
    excluir_registro,
    inserir_registros,
)
from comum.entrada import Campo, ler_inteiro
from comum.procedimentos import (
    cadastrar_registro,
    cadastrar_registros,
    editar_registro,
    listar_registros,
    ordenar_registros,
    pesquisar_registro,
    selecionar_registro,
)


def executar_menu_atividade(
    titulo: str,
    entidade: str,
    campos: tuple[Campo, ...],
    classificar: Callable[[dict[str, object]], list[str]],
    acao_extra: Callable[[list[dict[str, object]]], None] | None = None,
    caminho_banco: str | Path | None = None,
) -> bool:
    try:
        registros = carregar_registros(titulo, caminho_banco)
    except (OSError, ValueError) as erro:
        print(f"Não foi possível acessar o banco de dados: {erro}")
        return False

    while True:
        print(f"\n--- {titulo} ---")
        print("1 - Cadastrar os 5 registros")
        print("2 - Listar registros")
        print("3 - Ordenar por nome (Bubble Sort)")
        print("4 - Pesquisar por nome (Busca Binária)")
        print("5 - Cadastrar um registro")
        print("6 - Editar um registro")
        print("7 - Eliminar um registro")
        opcao_extra = 8
        if acao_extra is not None:
            print("8 - Reservar passagens")
            opcao_extra = 9
        opcao_voltar = opcao_extra
        print(f"{opcao_voltar} - Voltar ao menu geral")
        print("0 - Encerrar o programa")
        opcao = ler_inteiro("Escolha uma opção: ", 0, opcao_voltar)

        if opcao == 0:
            return True
        if opcao == opcao_voltar:
            return False
        if opcao == 1:
            if registros:
                print("Os registros já foram cadastrados.")
            else:
                novos_registros = cadastrar_registros(entidade, campos)
                try:
                    inserir_registros(titulo, novos_registros, caminho_banco)
                except (OSError, ValueError) as erro:
                    print(f"Não foi possível cadastrar os registros: {erro}")
                else:
                    registros = carregar_registros(titulo, caminho_banco)
                    print("Registros cadastrados e salvos no banco de dados.")
        elif opcao == 5:
            novo_registro = cadastrar_registro(entidade, campos)
            try:
                inserir_registros(titulo, [novo_registro], caminho_banco)
            except (OSError, ValueError) as erro:
                print(f"Não foi possível cadastrar o registro: {erro}")
            else:
                registros = carregar_registros(titulo, caminho_banco)
                print("Registro cadastrado e salvo no banco de dados.")
        elif opcao in (2, 3, 4, 6, 7) and not registros:
            print("Cadastre os cinco registros antes de usar esta opção.")
        elif opcao == 2:
            listar_registros(entidade, campos, registros, classificar)
        elif opcao == 3:
            ordenar_registros(entidade, campos, registros, classificar)
        elif opcao == 4:
            pesquisar_registro(entidade, campos, registros, classificar)
        elif opcao == 6:
            registro = selecionar_registro(entidade, registros)
            editar_registro(entidade, campos, registro)
            try:
                atualizar_registro(titulo, registro, caminho_banco)
            except (LookupError, OSError, ValueError) as erro:
                registros = carregar_registros(titulo, caminho_banco)
                print(f"Não foi possível salvar as alterações: {erro}")
            else:
                print("Registro atualizado.")
        elif opcao == 7:
            registro = selecionar_registro(entidade, registros)
            confirmacao = ler_inteiro("Confirma a exclusão? (1 - Sim, 2 - Não): ", 1, 2)
            if confirmacao == 1:
                try:
                    excluir_registro(titulo, int(registro["id"]), caminho_banco)
                except (LookupError, OSError, ValueError) as erro:
                    print(f"Não foi possível eliminar o registro: {erro}")
                else:
                    registros = carregar_registros(titulo, caminho_banco)
                    print("Registro eliminado.")
        elif opcao == 8 and acao_extra is not None:
            acao_extra(registros)
            for registro in registros:
                try:
                    atualizar_registro(titulo, registro, caminho_banco)
                except (LookupError, OSError, ValueError) as erro:
                    registros = carregar_registros(titulo, caminho_banco)
                    print(f"Não foi possível salvar os dados atualizados: {erro}")
                    break
