from comum.entrada import Campo


TITULO = "Atividade 4 - Gerenciador de Finanças e Despesas"
ENTIDADE = "Categoria de despesa"
CAMPOS = (
    Campo("orcado", "Valor orçado (R$)", "decimal", 0),
    Campo("gasto", "Valor gasto (R$)", "decimal", 0),
    Campo("prioridade", "Código de prioridade (1, 2 ou 3)", "inteiro", 1, 3),
)
