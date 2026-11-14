from comum.menu_atividade import executar_menu_atividade
from .dados import CAMPOS, ENTIDADE, TITULO
from .procedimentos import reservar_passagens
from .regras import classificar


def principal() -> bool:
    return executar_menu_atividade(
        TITULO,
        ENTIDADE,
        CAMPOS,
        classificar,
        acao_extra=reservar_passagens,
    )
