from comum.entrada import Campo


TITULO = "Atividade 7 - Simulador de Desempenho de Servidores (TI)"
ENTIDADE = "Servidor"
CAMPOS = (
    Campo("cpu", "Uso de CPU (%)", "decimal", 0, 100),
    Campo("ram", "Uso de memória RAM (%)", "decimal", 0, 100),
    Campo("uptime", "Uptime (horas)", "decimal", 0),
)
