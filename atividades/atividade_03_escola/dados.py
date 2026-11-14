from comum.entrada import Campo


TITULO = "Atividade 3 - Controle de Notas e Frequência Escolar"
ENTIDADE = "Aluno"
CAMPOS = (
    Campo("nota1", "Nota 1", "decimal", 0, 10),
    Campo("nota2", "Nota 2", "decimal", 0, 10),
    Campo("faltas", "Total de faltas", "inteiro", 0),
)
