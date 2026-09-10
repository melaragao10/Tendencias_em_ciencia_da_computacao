"""Logica central (pura) do jogo da forca.

Refatoracao pedida via prompt: "separe a verificacao de letras em uma
funcao especifica" e "evite mutacao de estado desnecessaria". Por isso
as funcoes abaixo nao usam variaveis globais e, sempre que possivel,
recebem o estado e devolvem um novo resultado, em vez de alterar listas
"por fora". Isso tambem e o que torna essas funcoes faceis de testar
(ver tests/test_forca.py).
"""

from dataclasses import dataclass, field


@dataclass
class EstadoDoJogo:
    """Guarda todo o estado de uma partida em um unico lugar.

    Comparado a versao 1 (que usava 4 variaveis soltas: palavra,
    letras_certas, letras_erradas, tentativas), agrupar tudo em uma
    dataclass deixa explicito o que pertence ao "estado do jogo" e
    evita passar 4 parametros para cada funcao.
    """

    palavra: str
    letras_tentadas: set[str] = field(default_factory=set)
    max_erros: int = 6

    @property
    def letras_erradas(self) -> set[str]:
        return {letra for letra in self.letras_tentadas if letra not in self.palavra}

    @property
    def numero_de_erros(self) -> int:
        return len(self.letras_erradas)

    @property
    def tentativas_restantes(self) -> int:
        return self.max_erros - self.numero_de_erros


def normalizar_letra(entrada: str) -> str:
    """Normaliza a entrada do usuario para uma unica letra minuscula.

    Levanta ValueError com uma mensagem clara quando a entrada nao e
    uma unica letra do alfabeto -- a versao 1 nao validava nada disso
    e quebrava (ou se comportava de forma estranha) com entradas como
    "" ou "ab" ou "5".
    """
    letra = entrada.strip().lower()
    if len(letra) != 1 or not letra.isalpha():
        raise ValueError("Digite exatamente uma letra (a-z).")
    return letra


def registrar_tentativa(estado: EstadoDoJogo, letra: str) -> EstadoDoJogo:
    """Retorna um novo estado com a letra registrada como tentada.

    Levanta ValueError se a letra ja tiver sido tentada antes, para que
    quem chama a funcao possa avisar o jogador sem gastar uma tentativa.
    """
    if letra in estado.letras_tentadas:
        raise ValueError(f"A letra {letra!r} ja foi tentada.")
    novas_letras = estado.letras_tentadas | {letra}
    return EstadoDoJogo(
        palavra=estado.palavra,
        letras_tentadas=novas_letras,
        max_erros=estado.max_erros,
    )


def _precisa_ser_adivinhada(caractere: str) -> bool:
    """So letras (a-z) precisam ser adivinhadas.

    Bug encontrado durante o teste manual: a palavra "guarda-chuva"
    tem um hifen, e `normalizar_letra` corretamente rejeita "-" como
    palpite invalido (nao e uma letra do alfabeto). Sem esta funcao,
    o hifen nunca entraria em `letras_tentadas` e o jogo ficava preso
    para sempre esperando um palpite que nunca poderia ser aceito.
    Qualquer caractere que nao seja letra (hifen, espaco, apostrofo...)
    e tratado como ja revelado, igual a maioria das implementacoes de
    forca com palavras compostas.
    """
    return caractere.isalpha()


def palavra_revelada(estado: EstadoDoJogo) -> str:
    """Monta a palavra com '_' nas letras ainda nao descobertas.

    Caracteres que nao sao letras (ex.: o hifen de "guarda-chuva")
    aparecem sempre, pois nao fazem parte do desafio de adivinhacao.
    """
    return " ".join(
        letra
        if not _precisa_ser_adivinhada(letra) or letra in estado.letras_tentadas
        else "_"
        for letra in estado.palavra
    )


def venceu(estado: EstadoDoJogo) -> bool:
    """True quando todas as letras (a-z) da palavra ja foram tentadas."""
    return all(
        letra in estado.letras_tentadas
        for letra in estado.palavra
        if _precisa_ser_adivinhada(letra)
    )


def perdeu(estado: EstadoDoJogo) -> bool:
    """True quando o numero de erros atingiu o limite da forca."""
    return estado.numero_de_erros >= estado.max_erros


def jogo_terminado(estado: EstadoDoJogo) -> bool:
    return venceu(estado) or perdeu(estado)
