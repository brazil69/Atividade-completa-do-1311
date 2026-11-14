from comum.entrada import Campo


TITULO = "Atividade 1 - Gestão de Estoque de Autopeças"
ENTIDADE = "Autopeça"
CAMPOS = (
    Campo("quantidade", "Quantidade em estoque", "inteiro", 0),
    Campo("custo", "Preço de custo (R$)", "decimal", 0),
    Campo("venda", "Preço de venda (R$)", "decimal", 0),
)
