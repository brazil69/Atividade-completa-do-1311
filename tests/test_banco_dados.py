import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from comum.banco_dados import (
    atualizar_registro,
    carregar_registros,
    excluir_registro,
    inserir_registros,
)


class BancoDadosTest(unittest.TestCase):
    def test_insere_atualiza_e_exclui_registros(self) -> None:
        with TemporaryDirectory() as diretorio:
            caminho_banco = Path(diretorio) / "teste.xlsx"
            inserir_registros(
                "Estoque",
                [{"nome": "Parafuso", "quantidade": 10, "preco": 1.5}],
                caminho_banco,
            )
            registro = carregar_registros("Estoque", caminho_banco)[0]
            registro["quantidade"] = 20
            atualizar_registro("Estoque", registro, caminho_banco)
            self.assertEqual(
                carregar_registros("Estoque", caminho_banco)[0]["quantidade"],
                20,
            )

            excluir_registro("Estoque", int(registro["id"]), caminho_banco)
            self.assertEqual(carregar_registros("Estoque", caminho_banco), [])

    def test_nao_permite_nome_duplicado_na_mesma_atividade(self) -> None:
        with TemporaryDirectory() as diretorio:
            caminho_banco = Path(diretorio) / "teste.xlsx"
            inserir_registros("Estoque", [{"nome": "Parafuso"}], caminho_banco)
            with self.assertRaises(ValueError):
                inserir_registros("Estoque", [{"nome": "PARAFUSO"}], caminho_banco)


if __name__ == "__main__":
    unittest.main()
