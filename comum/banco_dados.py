from pathlib import Path
from zipfile import BadZipFile

from openpyxl import Workbook, load_workbook
from openpyxl.utils.exceptions import InvalidFileException
from openpyxl.worksheet.worksheet import Worksheet


CAMINHO_BANCO = Path(__file__).resolve().parent.parent / "banco_dados.xlsx"


def _caminho(caminho: str | Path | None) -> Path:
    return Path(caminho) if caminho is not None else CAMINHO_BANCO


def _nome_planilha(atividade: str) -> str:
    caracteres_invalidos = '[]:*?/\\'
    nome = "".join(
        "_" if caractere in caracteres_invalidos else caractere
        for caractere in atividade
    ).strip("'")[:31]
    return nome or "Atividade"


def _abrir(caminho: Path, criar: bool = False) -> Workbook | None:
    if caminho.exists():
        try:
            return load_workbook(caminho)
        except (BadZipFile, InvalidFileException, OSError, ValueError) as erro:
            raise ValueError(f"Não foi possível ler o arquivo Excel: {erro}") from erro
    if criar:
        return Workbook()
    return None


def _obter_planilha(
    workbook: Workbook,
    atividade: str,
    chaves: list[str] | None = None,
) -> Worksheet:
    nome = _nome_planilha(atividade)
    if nome in workbook.sheetnames:
        planilha = workbook[nome]
    else:
        planilha = workbook.active
        if planilha.max_row == 1 and planilha.max_column == 1 and planilha["A1"].value is None:
            planilha.title = nome
        else:
            planilha = workbook.create_sheet(nome)

    if planilha.max_row == 1 and planilha["A1"].value is None:
        for coluna, cabecalho in enumerate(["id", "nome", *(chaves or [])], start=1):
            planilha.cell(row=1, column=coluna, value=cabecalho)
    return planilha


def _cabecalhos(planilha: Worksheet) -> list[str]:
    cabecalhos = [celula.value for celula in planilha[1]]
    if len(cabecalhos) < 2 or cabecalhos[:2] != ["id", "nome"]:
        raise ValueError(f"A planilha '{planilha.title}' não tem o cabeçalho esperado.")
    return [str(cabecalho) for cabecalho in cabecalhos]


def _adicionar_colunas(
    planilha: Worksheet,
    cabecalhos: list[str],
    registro: dict[str, object],
) -> list[str]:
    for chave in registro:
        if chave not in {"id", "nome"} and chave not in cabecalhos:
            cabecalhos.append(chave)
            planilha.cell(row=1, column=len(cabecalhos), value=chave)
    return cabecalhos


def _linha_registro(
    planilha: Worksheet,
    linha: int,
    cabecalhos: list[str],
) -> dict[str, object]:
    return {
        cabecalho: planilha.cell(row=linha, column=coluna).value
        for coluna, cabecalho in enumerate(cabecalhos, start=1)
    }


def _verificar_nome_unico(
    planilha: Worksheet,
    nome: str,
    ignorar_linha: int | None = None,
) -> None:
    nome_normalizado = nome.strip().casefold()
    for linha in range(2, planilha.max_row + 1):
        if linha == ignorar_linha:
            continue
        nome_existente = planilha.cell(row=linha, column=2).value
        if isinstance(nome_existente, str) and nome_existente.strip().casefold() == nome_normalizado:
            raise ValueError("Já existe um registro com esse nome nesta atividade.")


def _proximo_id(planilha: Worksheet) -> int:
    identificadores = [
        planilha.cell(row=linha, column=1).value
        for linha in range(2, planilha.max_row + 1)
    ]
    return max((int(valor) for valor in identificadores if valor is not None), default=0) + 1


def carregar_registros(
    atividade: str,
    caminho: str | Path | None = None,
) -> list[dict[str, object]]:
    arquivo = _caminho(caminho)
    workbook = _abrir(arquivo)
    if workbook is None:
        return []
    try:
        nome_planilha = _nome_planilha(atividade)
        if nome_planilha not in workbook.sheetnames:
            return []
        planilha = workbook[nome_planilha]
        cabecalhos = _cabecalhos(planilha)
        return [
            _linha_registro(planilha, linha, cabecalhos)
            for linha in range(2, planilha.max_row + 1)
            if planilha.cell(row=linha, column=1).value is not None
        ]
    finally:
        workbook.close()


def inserir_registros(
    atividade: str,
    registros: list[dict[str, object]],
    caminho: str | Path | None = None,
) -> None:
    arquivo = _caminho(caminho)
    workbook = _abrir(arquivo, criar=True)
    if workbook is None:
        raise OSError("Não foi possível criar o arquivo Excel.")
    try:
        planilha = _obter_planilha(
            workbook,
            atividade,
            [chave for chave in registros[0] if chave not in {"id", "nome"}]
            if registros
            else [],
        )
        cabecalhos = _cabecalhos(planilha)
        nomes = set()
        for registro in registros:
            nome = str(registro["nome"]).strip()
            if nome.casefold() in nomes:
                raise ValueError("Já existe um registro com esse nome nesta atividade.")
            nomes.add(nome.casefold())
            _verificar_nome_unico(planilha, nome)
            cabecalhos = _adicionar_colunas(planilha, cabecalhos, registro)
            novo_registro = {**registro, "id": _proximo_id(planilha), "nome": nome}
            planilha.append(
                [novo_registro.get(cabecalho) for cabecalho in cabecalhos]
            )
        workbook.save(arquivo)
    finally:
        workbook.close()


def atualizar_registro(
    atividade: str,
    registro: dict[str, object],
    caminho: str | Path | None = None,
) -> None:
    arquivo = _caminho(caminho)
    workbook = _abrir(arquivo)
    if workbook is None:
        raise LookupError("Registro não encontrado nesta atividade.")
    try:
        nome_planilha = _nome_planilha(atividade)
        if nome_planilha not in workbook.sheetnames:
            raise LookupError("Registro não encontrado nesta atividade.")
        planilha = workbook[nome_planilha]
        cabecalhos = _cabecalhos(planilha)
        linha_encontrada = next(
            (
                linha
                for linha in range(2, planilha.max_row + 1)
                if planilha.cell(row=linha, column=1).value == registro["id"]
            ),
            None,
        )
        if linha_encontrada is None:
            raise LookupError("Registro não encontrado nesta atividade.")
        nome = str(registro["nome"]).strip()
        _verificar_nome_unico(planilha, nome, linha_encontrada)
        cabecalhos = _adicionar_colunas(planilha, cabecalhos, registro)
        planilha.cell(row=linha_encontrada, column=2, value=nome)
        for coluna, cabecalho in enumerate(cabecalhos[2:], start=3):
            planilha.cell(
                row=linha_encontrada,
                column=coluna,
                value=registro.get(cabecalho),
            )
        workbook.save(arquivo)
    finally:
        workbook.close()


def excluir_registro(
    atividade: str,
    identificador: int,
    caminho: str | Path | None = None,
) -> None:
    arquivo = _caminho(caminho)
    workbook = _abrir(arquivo)
    if workbook is None:
        raise LookupError("Registro não encontrado nesta atividade.")
    try:
        nome_planilha = _nome_planilha(atividade)
        if nome_planilha not in workbook.sheetnames:
            raise LookupError("Registro não encontrado nesta atividade.")
        planilha = workbook[nome_planilha]
        linha_encontrada = next(
            (
                linha
                for linha in range(2, planilha.max_row + 1)
                if planilha.cell(row=linha, column=1).value == identificador
            ),
            None,
        )
        if linha_encontrada is None:
            raise LookupError("Registro não encontrado nesta atividade.")
        planilha.delete_rows(linha_encontrada)
        workbook.save(arquivo)
    finally:
        workbook.close()
