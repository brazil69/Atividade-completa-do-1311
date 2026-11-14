from comum.entrada import Campo


TITULO = "Atividade 10 - Controle de Qualidade de Lotes de Alimentos"
ENTIDADE = "Lote"
CAMPOS = (
    Campo("produzido", "Total produzido", "inteiro", 1),
    Campo("defeitos", "Quantidade com defeito", "inteiro", 0),
    Campo("setor", "Código do setor", "inteiro", 1, 3),
)
