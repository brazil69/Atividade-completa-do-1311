from datetime import date

from comum.entrada import Campo


TITULO = "Atividade 8 - Catálogo e Aluguel de Jogos de Videogame"
ENTIDADE = "Jogo"
CAMPOS = (
    Campo("ano", "Ano de lançamento", "inteiro", 1900, date.today().year),
    Campo("classificacao", "Classificação indicativa", "inteiro", 0, 18),
    Campo("diaria", "Preço base da diária (R$)", "decimal", 0),
)
