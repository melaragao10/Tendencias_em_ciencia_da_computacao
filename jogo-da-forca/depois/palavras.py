"""Banco de palavras do jogo da forca.

Sugestao da IA: separar o banco de palavras da logica do jogo (Single
Responsibility) e organiza-lo por categoria/dificuldade, em vez de uma
unica lista solta misturada com o loop principal (como na versao 1).
"""

from dataclasses import dataclass
import random

BANCO_DE_PALAVRAS: dict[str, list[str]] = {
    "tecnologia": ["python", "algoritmo", "computador", "internet", "software"],
    "faculdade": ["faculdade", "programacao", "professor", "biblioteca", "monitoria"],
    "cotidiano": ["cachorro", "guarda-chuva", "bicicleta", "chocolate", "aeroporto"],
}


@dataclass(frozen=True)
class Desafio:
    """Representa a palavra sorteada e a categoria a que ela pertence."""

    palavra: str
    categoria: str


def escolher_palavra(categoria: str | None = None) -> Desafio:
    """Sorteia uma palavra do banco.

    Se `categoria` for informada e existir no banco, sorteia apenas
    dentro dela; caso contrario, sorteia de qualquer categoria.
    Levanta ValueError se a categoria pedida nao existir.
    """
    if categoria is not None:
        if categoria not in BANCO_DE_PALAVRAS:
            raise ValueError(f"Categoria desconhecida: {categoria!r}")
        categorias_candidatas = [categoria]
    else:
        categorias_candidatas = list(BANCO_DE_PALAVRAS.keys())

    categoria_sorteada = random.choice(categorias_candidatas)
    palavra_sorteada = random.choice(BANCO_DE_PALAVRAS[categoria_sorteada])
    return Desafio(palavra=palavra_sorteada, categoria=categoria_sorteada)
