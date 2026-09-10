# Jogo da Forca - Versao 1 (ANTES)
# Primeira versao escrita manualmente, sem apoio de IA.
# Objetivo: apenas fazer o jogo funcionar (logica central).

palavras = ["python", "computador", "faculdade", "programacao", "internet"]

import random

palavra = random.choice(palavras)
letras_certas = []
letras_erradas = []
tentativas = 6

print("Bem vindo ao jogo da forca!")

fim = False
while fim == False:
    print("")
    palavra_mostrada = ""
    i = 0
    while i < len(palavra):
        letra = palavra[i]
        if letra in letras_certas:
            palavra_mostrada = palavra_mostrada + letra
        else:
            palavra_mostrada = palavra_mostrada + "_"
        i = i + 1
    print(palavra_mostrada)
    print("Tentativas restantes: " + str(tentativas))
    print("Letras erradas: " + str(letras_erradas))

    chute = input("Digite uma letra: ")

    if chute in palavra:
        if chute not in letras_certas:
            letras_certas.append(chute)
    else:
        if chute not in letras_erradas:
            letras_erradas.append(chute)
            tentativas = tentativas - 1

    ganhou = True
    for letra in palavra:
        if letra not in letras_certas:
            ganhou = False

    if ganhou == True:
        print("")
        print("Parabens, voce venceu! A palavra era: " + palavra)
        fim = True

    if tentativas == 0:
        print("")
        print("Voce perdeu! A palavra era: " + palavra)
        fim = True
