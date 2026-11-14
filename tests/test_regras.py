import unittest
from datetime import date

from atividades.atividade_01_estoque.regras import classificar as estoque
from atividades.atividade_02_hospital.regras import classificar as hospital
from atividades.atividade_03_escola.regras import classificar as escola
from atividades.atividade_04_financas.regras import classificar as financas
from atividades.atividade_05_frota.regras import classificar as frota
from atividades.atividade_06_passagens.regras import classificar as passagens
from atividades.atividade_07_servidores.regras import classificar as servidores
from atividades.atividade_08_jogos.regras import classificar as jogos
from atividades.atividade_09_imobiliaria.regras import classificar as imobiliaria
from atividades.atividade_10_lotes.regras import classificar as lotes


class RegrasDasAtividadesTest(unittest.TestCase):
    def test_estoque_limites_e_prejuizo(self) -> None:
        resultado = estoque({"quantidade": 9, "custo": 10, "venda": 9})
        self.assertIn("Alerta: Prejuízo!", resultado)
        self.assertIn("Estoque Crítico", resultado)
        self.assertIn("Indisponível" if False else "Disponível", resultado)
        self.assertIn("Estoque Normal", estoque({"quantidade": 10, "custo": 1, "venda": 1}))
        self.assertIn("Estoque Alto", estoque({"quantidade": 51, "custo": 1, "venda": 1}))

    def test_hospital_limites_inclusivos(self) -> None:
        resultado = hospital(
            {"temperatura": 37.5, "frequencia": 60, "pressao": 141}
        )
        self.assertIn("Normal", resultado)
        self.assertIn("Batimentos Regulares", resultado)
        self.assertIn("Alerta: Hipertensão", resultado)

    def test_escola_calcula_media_e_regras(self) -> None:
        resultado = escola({"nota1": 8, "nota2": 6, "faltas": 21})
        self.assertIn("Média: 7.00", resultado)
        self.assertIn("Reprovado por Faltas", resultado)
        self.assertIn("Aprovado", resultado)

    def test_financas_prioridade_e_limite_de_orcamento(self) -> None:
        resultado = financas({"orcado": 100, "gasto": 50, "prioridade": 1})
        self.assertIn("Gasto Dentro do Previsto", resultado)
        self.assertIn("Despesa Essencial", resultado)

    def test_frota_limites_de_revisao(self) -> None:
        resultado = frota(
            {"quilometragem": 20_000, "consumo": 5.9, "capacidade": 2001}
        )
        self.assertIn("Revisão Leve", resultado)
        self.assertIn("Porte: Pesado", resultado)
        self.assertIn("Aviso: Alto Custo de Combustível", resultado)

    def test_passagens_classifica_ultimas_vagas(self) -> None:
        resultado = passagens({"assentos": 9, "preco": 1501})
        self.assertIn("Últimas Vagas - Aplicar Taxa de 15%", resultado)
        self.assertIn("Tarifa Executiva / VIP", resultado)

    def test_servidores_sobrecarga_tem_precedencia(self) -> None:
        resultado = servidores({"cpu": 86, "ram": 20, "uptime": 721})
        self.assertIn("Sobrecarga Crítica", resultado)
        self.assertIn("Reinicialização Preventiva Necessária", resultado)

    def test_jogos_taxa_de_lancamento(self) -> None:
        resultado = jogos(
            {
                "ano": date.today().year,
                "classificacao": 18,
                "diaria": 16,
            }
        )
        self.assertIn("Taxa de Lançamento Aplicada: R$ 5,00", resultado)
        self.assertTrue(any("Categoria Premium" in linha for linha in resultado))
        self.assertIn("Exclusivo para Adultos", resultado)

    def test_imobiliaria_limite_de_meta_nao_especificado(self) -> None:
        resultado = imobiliaria(
            {"total_vendido": 1_000_001, "imoveis": 5, "satisfacao": 4}
        )
        self.assertIn("Meta de vendas não definida no enunciado", resultado)
        self.assertIn("Excelente Atendimento", resultado)
        self.assertTrue(any("Bônus de R$ 2.000,00" in linha for linha in resultado))

    def test_lotes_validam_percentual_e_setor(self) -> None:
        resultado = lotes({"produzido": 100, "defeitos": 6, "setor": 2})
        self.assertIn("Lote Reprovado - Descarte", resultado)
        self.assertIn("Atenção: Cadeia de Resfriamento", resultado)


if __name__ == "__main__":
    unittest.main()
