from comum.entrada import Campo


TITULO = "Atividade 2 - Monitoramento Clínico Hospitalar"
ENTIDADE = "Paciente"
CAMPOS = (
    Campo("temperatura", "Temperatura (°C)", "decimal", 0),
    Campo("frequencia", "Frequência cardíaca (bpm)", "inteiro", 0),
    Campo("pressao", "Pressão arterial sistólica (mmHg)", "inteiro", 0),
)
