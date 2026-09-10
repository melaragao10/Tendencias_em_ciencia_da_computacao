"""Ponto de entrada do jogo da forca (versao 2 - DEPOIS).

Este arquivo cuida apenas de I/O (ler input, imprimir tela) e chama as
funcoes puras de forca.py, desenho.py e palavras.py. Essa separacao foi
uma sugestao da IA durante a refatoracao, para que a logica do jogo
pudesse ser testada sem precisar simular teclado/tela.
"""

from desenho import desenhar_forca
from forca import (
    EstadoDoJogo,
    jogo_terminado,
    normalizar_letra,
    palavra_revelada,
    registrar_tentativa,
    venceu,
)
from palavras import escolher_palavra


def imprimir_estado(estado: EstadoDoJogo) -> None:
    print(desenhar_forca(estado.numero_de_erros))
    print("Palavra:", palavra_revelada(estado))
    print("Tentativas restantes:", estado.tentativas_restantes)
    if estado.letras_erradas:
        letras = ", ".join(sorted(estado.letras_erradas))
        print("Letras erradas:", letras)
    print()


def ler_letra_do_jogador(estado: EstadoDoJogo) -> str:
    """Pede uma letra ao jogador ate receber uma entrada valida e nova."""
    while True:
        entrada = input("Digite uma letra: ")
        try:
            letra = normalizar_letra(entrada)
        except ValueError as erro:
            print(f"Entrada invalida: {erro}")
            continue

        if letra in estado.letras_tentadas:
            print("Voce ja tentou essa letra, escolha outra.")
            continue

        return letra


def jogar_uma_partida(categoria: str | None = None) -> None:
    desafio = escolher_palavra(categoria)
    estado = EstadoDoJogo(palavra=desafio.palavra)

    print("=" * 40)
    print("JOGO DA FORCA")
    print(f"Categoria sorteada: {desafio.categoria}")
    print("=" * 40)

    while not jogo_terminado(estado):
        imprimir_estado(estado)
        letra = ler_letra_do_jogador(estado)
        estado = registrar_tentativa(estado, letra)

    imprimir_estado(estado)
    if venceu(estado):
        print(f"Parabens! Voce venceu! A palavra era '{estado.palavra}'.")
    else:
        print(f"Voce perdeu! A palavra era '{estado.palavra}'.")


def main() -> None:
    continuar = True
    while continuar:
        jogar_uma_partida()
        resposta = input("\nJogar novamente? (s/n): ").strip().lower()
        continuar = resposta.startswith("s")
    print("Ate a proxima!")


if __name__ == "__main__":
    main()
