"""Desenho ASCII da forca.

Sugestao da IA: extrair os estagios do desenho para uma constante
(lista de strings), em vez de vários prints espalhados pelo loop do
jogo. Isso deixa a exibicao facil de testar e de trocar de estilo.
"""

ESTAGIOS_DA_FORCA: list[str] = [
    r"""
      ------
      |    |
      |
      |
      |
      |
    --------
    """,
    r"""
      ------
      |    |
      |    O
      |
      |
      |
    --------
    """,
    r"""
      ------
      |    |
      |    O
      |    |
      |
      |
    --------
    """,
    r"""
      ------
      |    |
      |    O
      |   /|
      |
      |
    --------
    """,
    r"""
      ------
      |    |
      |    O
      |   /|\
      |
      |
    --------
    """,
    r"""
      ------
      |    |
      |    O
      |   /|\
      |   /
      |
    --------
    """,
    r"""
      ------
      |    |
      |    O
      |   /|\
      |   / \
      |
    --------
    """,
]

MAX_ERROS: int = len(ESTAGIOS_DA_FORCA) - 1


def desenhar_forca(numero_de_erros: int) -> str:
    """Retorna a arte ASCII correspondente ao numero de erros cometidos.

    O valor e limitado (clamp) entre 0 e MAX_ERROS para nunca estourar
    a lista, mesmo se o chamador passar um numero fora da faixa.
    """
    indice = max(0, min(numero_de_erros, MAX_ERROS))
    return ESTAGIOS_DA_FORCA[indice]
