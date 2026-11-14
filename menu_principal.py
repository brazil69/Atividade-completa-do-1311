from comum.entrada import ler_inteiro
from atividades.atividade_01_estoque import executar as atividade_01
from atividades.atividade_02_hospital import executar as atividade_02
from atividades.atividade_03_escola import executar as atividade_03
from atividades.atividade_04_financas import executar as atividade_04
from atividades.atividade_05_frota import executar as atividade_05
from atividades.atividade_06_passagens import executar as atividade_06
from atividades.atividade_07_servidores import executar as atividade_07
from atividades.atividade_08_jogos import executar as atividade_08
from atividades.atividade_09_imobiliaria import executar as atividade_09
from atividades.atividade_10_lotes import executar as atividade_10


ATIVIDADES = {
    1: atividade_01,
    2: atividade_02,
    3: atividade_03,
    4: atividade_04,
    5: atividade_05,
    6: atividade_06,
    7: atividade_07,
    8: atividade_08,
    9: atividade_09,
    10: atividade_10,
}


def executar_menu_principal() -> None:
    while True:
        print("\n========== MENU DE ATIVIDADES ==========")
        print("1 - Gestão de estoque de autopeças")
        print("2 - Monitoramento clínico hospitalar")
        print("3 - Controle de notas e frequência escolar")
        print("4 - Gerenciador de finanças e despesas")
        print("5 - Cadastro e logística de frota")
        print("6 - Reservas de passagens aéreas")
        print("7 - Desempenho de servidores de TI")
        print("8 - Catálogo e aluguel de jogos")
        print("9 - Vendas de corretores de imóveis")
        print("10 - Qualidade de lotes de alimentos")
        print("0 - Sair")

        opcao = ler_inteiro("Escolha uma atividade: ", 0, 10)
        if opcao == 0:
            print("Programa encerrado.")
            return
        if ATIVIDADES[opcao]():
            print("Programa encerrado.")
            return
