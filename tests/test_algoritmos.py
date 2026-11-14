import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from comum.algoritmos import buscar_binaria, ordenar_bubble_sort
from comum.menu_atividade import executar_menu_atividade
from comum.banco_dados import carregar_registros
from atividades.atividade_06_passagens.dados import CAMPOS, ENTIDADE, TITULO
from atividades.atividade_06_passagens.procedimentos import reservar_passagens
from atividades.atividade_06_passagens.regras import classificar
from menu_principal import executar_menu_principal


def executar_menu_temporario(*args, **kwargs):
    with TemporaryDirectory() as diretorio:
        return executar_menu_atividade(
            *args,
            caminho_banco=Path(diretorio) / "teste.xlsx",
            **kwargs,
        )


class AlgoritmosTest(unittest.TestCase):
    def test_bubble_sort_move_registros_com_seus_dados(self) -> None:
        registros = [
            {"nome": "Zebra", "valor": 1},
            {"nome": "Árvore", "valor": 2},
            {"nome": "Casa", "valor": 3},
        ]
        ordenar_bubble_sort(registros)
        self.assertEqual([registro["nome"] for registro in registros], ["Árvore", "Casa", "Zebra"])
        self.assertEqual(registros[0]["valor"], 2)

    def test_busca_binaria_ignora_maiusculas_e_acentos_da_consulta(self) -> None:
        registros = [{"nome": "Árvore"}, {"nome": "Bruno"}, {"nome": "Caio"}]
        self.assertEqual(buscar_binaria(registros, "arvore"), {"nome": "Árvore"})
        self.assertEqual(buscar_binaria(registros, "BRUNO"), {"nome": "Bruno"})
        self.assertIsNone(buscar_binaria(registros, "Diana"))

    def test_menu_da_atividade_aparece_antes_do_cadastro(self) -> None:
        saida = StringIO()
        with patch("builtins.input", return_value="8"):
            with redirect_stdout(saida):
                executar_menu_temporario("Atividade de teste", "Registro", (), lambda _: [])
        self.assertIn("--- Atividade de teste ---", saida.getvalue())
        self.assertIn("1 - Cadastrar os 5 registros", saida.getvalue())
        self.assertIn("5 - Cadastrar um registro", saida.getvalue())
        self.assertIn("6 - Editar um registro", saida.getvalue())
        self.assertIn("7 - Eliminar um registro", saida.getvalue())
        self.assertIn("8 - Voltar ao menu geral", saida.getvalue())
        self.assertIn("0 - Encerrar o programa", saida.getvalue())

    def test_menu_da_atividade_pode_encerrar_o_programa(self) -> None:
        with patch("builtins.input", return_value="0"):
            resultado = executar_menu_temporario(
                "Atividade de teste", "Registro", (), lambda _: []
            )
        self.assertTrue(resultado)

    def test_menu_da_atividade_pode_voltar_ao_menu_geral(self) -> None:
        with patch("builtins.input", return_value="8"):
            resultado = executar_menu_temporario(
                "Atividade de teste", "Registro", (), lambda _: []
            )
        self.assertFalse(resultado)

    def test_menu_com_acao_extra_usa_opcao_separada_para_voltar(self) -> None:
        saida = StringIO()
        with patch("builtins.input", return_value="9"):
            with redirect_stdout(saida):
                resultado = executar_menu_temporario(
                    "Atividade de teste",
                    "Registro",
                    (),
                    lambda _: [],
                    acao_extra=lambda _: None,
                )
        self.assertIn("9 - Voltar ao menu geral", saida.getvalue())
        self.assertFalse(resultado)

    def test_encerramento_no_menu_da_atividade_fecha_o_programa(self) -> None:
        saida = StringIO()
        with patch("menu_principal.ATIVIDADES", {1: lambda: True}):
            with patch("builtins.input", return_value="1"):
                with redirect_stdout(saida):
                    executar_menu_principal()
        self.assertIn("Programa encerrado.", saida.getvalue())

    def test_menu_avisa_se_tentarem_listar_sem_cadastro(self) -> None:
        saida = StringIO()
        with patch("builtins.input", side_effect=["2", "0"]):
            with redirect_stdout(saida):
                executar_menu_temporario("Atividade de teste", "Registro", (), lambda _: [])
        self.assertIn("Cadastre os cinco registros antes de usar esta opção.", saida.getvalue())

    def test_menu_persiste_edicao_e_exclusao_de_registro(self) -> None:
        with TemporaryDirectory() as diretorio:
            caminho_banco = Path(diretorio) / "teste.xlsx"
            saida = StringIO()
            entradas = [
                "5", "Nome inicial",
                "6", "1", "0", "Nome editado",
                "7", "1", "1",
                "0",
            ]
            with patch("builtins.input", side_effect=entradas):
                with redirect_stdout(saida):
                    executar_menu_atividade(
                        "Atividade de teste",
                        "Registro",
                        (),
                        lambda _: [],
                        caminho_banco=caminho_banco,
                    )

            self.assertIn("Registro atualizado.", saida.getvalue())
            self.assertIn("Registro eliminado.", saida.getvalue())
            self.assertEqual(carregar_registros("Atividade de teste", caminho_banco), [])

    def test_registros_ficam_separados_por_atividade(self) -> None:
        with TemporaryDirectory() as diretorio:
            caminho_banco = Path(diretorio) / "teste.xlsx"
            for titulo in ("Atividade A", "Atividade B"):
                with patch("builtins.input", side_effect=["5", "Mesmo nome", "8"]):
                    executar_menu_atividade(
                        titulo,
                        "Registro",
                        (),
                        lambda _: [],
                        caminho_banco=caminho_banco,
                    )
            self.assertEqual(
                [registro["nome"] for registro in carregar_registros("Atividade A", caminho_banco)],
                ["Mesmo nome"],
            )
            self.assertEqual(
                [registro["nome"] for registro in carregar_registros("Atividade B", caminho_banco)],
                ["Mesmo nome"],
            )

    def test_reserva_salva_a_quantidade_atualizada_de_assentos(self) -> None:
        with TemporaryDirectory() as diretorio:
            caminho_banco = Path(diretorio) / "teste.xlsx"
            entradas = [
                "5", "Porto", "V1", "12", "100",
                "8", "Porto", "3",
                "9",
            ]
            with patch("builtins.input", side_effect=entradas):
                executar_menu_atividade(
                    TITULO,
                    ENTIDADE,
                    CAMPOS,
                    classificar,
                    acao_extra=reservar_passagens,
                    caminho_banco=caminho_banco,
                )

            registro = carregar_registros(TITULO, caminho_banco)[0]
            self.assertEqual(registro["assentos"], 9)


if __name__ == "__main__":
    unittest.main()
