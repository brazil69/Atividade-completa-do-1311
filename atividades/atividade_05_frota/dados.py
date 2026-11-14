from comum.entrada import Campo


TITULO = "Atividade 5 - Cadastro e Logística de Frota"
ENTIDADE = "Veículo"
CAMPOS = (
    Campo("quilometragem", "Quilometragem atual (km)", "inteiro", 0),
    Campo("consumo", "Consumo médio (km/L)", "decimal", 0),
    Campo("capacidade", "Capacidade de carga (kg)", "decimal", 0),
)
