from comum.entrada import Campo


TITULO = "Atividade 6 - Sistema de Reservas de Passagens Aéreas"
ENTIDADE = "Destino"
CAMPOS = (
    Campo("codigo", "Código do voo", "texto"),
    Campo("assentos", "Assentos disponíveis (máximo 50)", "inteiro", 0, 50),
    Campo("preco", "Preço da passagem (R$)", "decimal", 0),
)
