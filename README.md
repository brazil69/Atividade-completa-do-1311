# Atividades de Algoritmos em Python

Projeto único com um menu geral para escolher entre as dez atividades das imagens.
Cada atividade abre seu próprio menu principal. A interface e as mensagens estão
em português.

## Requisitos

- Python 3.10 ou superior.
- Dependência: `openpyxl` (instale com `python -m pip install -r requirements.txt`).
- Um terminal aberto na pasta do projeto.

## Como executar

```text
python main.py
```

Escolha uma opção de **1 a 10** no menu geral para abrir imediatamente o menu
principal daquela atividade. Nesse menu, escolha **1** para cadastrar os cinco
registros ou **5** para cadastrar um registro. Os dados ficam salvos em
`banco_dados.xlsx`, em uma planilha separada por atividade, mesmo depois de
encerrar o programa. Use as opções **6** e **7** para editar ou eliminar um registro; as
opções de listagem, ordenação e pesquisa continuam disponíveis. A opção **0**
em qualquer menu encerra o programa. Nos menus das atividades, a última opção
retorna ao menu geral.

Na pesquisa, os registros são ordenados com Bubble Sort antes de a Busca Binária
ser aplicada. Os nomes são únicos dentro de cada cadastro. Valores decimais
aceitam ponto ou vírgula.

Na atividade 6, o menu próprio também oferece a opção **8** para reservar
passagens. A quantidade reservada não pode ultrapassar os assentos disponíveis e
o saldo é atualizado durante a execução. As opções que dependem de registros
avisam quando é necessário cadastrá-los primeiro.

## Organização

- `main.py`: ponto de entrada do programa.
- `menu_principal.py`: menu geral e seleção das atividades.
- `comum/entrada.py`: funções reutilizadas para ler e validar os dados.
- `comum/banco_dados.py`: persistência dos registros em planilhas Excel.
- `comum/algoritmos.py`: Bubble Sort e Busca Binária compartilhados.
- `comum/menu_atividade.py`: fluxo do menu individual de cada atividade.
- `comum/procedimentos.py`: procedimentos compartilhados de cadastro, listagem,
  ordenação, pesquisa e exibição dos registros.
- `atividades/atividade_XX_*/menu.py`: menu principal separado de cada atividade.
- `atividades/atividade_XX_*/dados.py`: campos e limites de entrada.
- `atividades/atividade_XX_*/regras.py`: funções de classificação próprias de
  cada atividade.
- `atividades/atividade_06_passagens/procedimentos.py`: procedimento específico
  para reservar passagens.
- `atividades/atividade_XX_*/__init__.py`: disponibiliza o menu próprio para o
  menu geral.
- `tests/`: testes das regras e dos algoritmos compartilhados.

## Executar os testes

```text
python -m unittest discover -v
```

## Observações sobre regras incompletas nas imagens

- Na atividade 8, classificações indicativas 16 e 17 não têm uma categoria
  definida na imagem; o sistema informa isso sem inventar uma regra.
- Na atividade 9, exatamente cinco imóveis vendidos não se encaixam nas faixas
  descritas; o sistema informa que a meta não foi definida.
- Na atividade 10, o total produzido deve ser maior que zero para que o
  percentual de defeitos possa ser calculado.
