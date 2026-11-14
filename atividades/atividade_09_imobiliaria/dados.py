from comum.entrada import Campo


TITULO = "Atividade 9 - Monitoramento de Vendas de Corretores de Imóveis"
ENTIDADE = "Corretor"
CAMPOS = (
    Campo("total_vendido", "Valor total vendido (R$)", "decimal", 0),
    Campo("imoveis", "Quantidade de imóveis vendidos", "inteiro", 0),
    Campo("satisfacao", "Índice de satisfação (1 a 5)", "decimal", 1, 5),
)
