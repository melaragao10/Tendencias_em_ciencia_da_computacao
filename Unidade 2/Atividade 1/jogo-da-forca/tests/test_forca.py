"""Testes automatizados da logica pura do jogo (pasta depois/).

Escrever estes testes foi parte da etapa "Avaliar Criticamente (Humano)"
do ciclo de colaboracao: em vez de confiar apenas na sugestao da IA,
validamos o comportamento com casos concretos, incluindo casos de borda
que a versao 1 nao tratava (entrada invalida, letra repetida).

Rodar com:  python -m unittest discover -s tests
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "depois"))

from forca import (  # noqa: E402
    EstadoDoJogo,
    jogo_terminado,
    normalizar_letra,
    palavra_revelada,
    perdeu,
    registrar_tentativa,
    venceu,
)


class TestNormalizarLetra(unittest.TestCase):
    def test_aceita_letra_minuscula(self):
        self.assertEqual(normalizar_letra("a"), "a")

    def test_normaliza_maiuscula_para_minuscula(self):
        self.assertEqual(normalizar_letra("A"), "a")

    def test_remove_espacos(self):
        self.assertEqual(normalizar_letra("  b  "), "b")

    def test_rejeita_string_vazia(self):
        with self.assertRaises(ValueError):
            normalizar_letra("")

    def test_rejeita_mais_de_uma_letra(self):
        with self.assertRaises(ValueError):
            normalizar_letra("ab")

    def test_rejeita_numero(self):
        with self.assertRaises(ValueError):
            normalizar_letra("5")


class TestRegistrarTentativa(unittest.TestCase):
    def test_adiciona_letra_nova(self):
        estado = EstadoDoJogo(palavra="python")
        novo_estado = registrar_tentativa(estado, "p")
        self.assertIn("p", novo_estado.letras_tentadas)

    def test_nao_muta_o_estado_original(self):
        estado = EstadoDoJogo(palavra="python")
        registrar_tentativa(estado, "p")
        self.assertEqual(estado.letras_tentadas, set())

    def test_rejeita_letra_repetida(self):
        estado = EstadoDoJogo(palavra="python", letras_tentadas={"p"})
        with self.assertRaises(ValueError):
            registrar_tentativa(estado, "p")


class TestPalavraRevelada(unittest.TestCase):
    def test_sem_tentativas_mostra_tudo_oculto(self):
        estado = EstadoDoJogo(palavra="sol")
        self.assertEqual(palavra_revelada(estado), "_ _ _")

    def test_revela_apenas_letras_tentadas(self):
        estado = EstadoDoJogo(palavra="sol", letras_tentadas={"s", "o"})
        self.assertEqual(palavra_revelada(estado), "s o _")


class TestPalavraComHifen(unittest.TestCase):
    """Regressao do bug encontrado em teste manual: 'guarda-chuva' travava
    o jogo, porque o hifen nunca podia ser adivinhado como letra."""

    def test_hifen_aparece_revelado_desde_o_inicio(self):
        estado = EstadoDoJogo(palavra="guarda-chuva")
        self.assertIn("-", palavra_revelada(estado))

    def test_vence_sem_precisar_adivinhar_o_hifen(self):
        estado = EstadoDoJogo(palavra="guarda-chuva")
        for letra in "gardchuv":
            estado = registrar_tentativa(estado, letra)
        self.assertTrue(venceu(estado))


class TestCondicoesDeFimDeJogo(unittest.TestCase):
    def test_venceu_quando_todas_as_letras_foram_tentadas(self):
        estado = EstadoDoJogo(palavra="sol", letras_tentadas={"s", "o", "l"})
        self.assertTrue(venceu(estado))
        self.assertFalse(perdeu(estado))
        self.assertTrue(jogo_terminado(estado))

    def test_perdeu_quando_atinge_max_erros(self):
        estado = EstadoDoJogo(
            palavra="sol", letras_tentadas={"x", "y"}, max_erros=2
        )
        self.assertTrue(perdeu(estado))
        self.assertFalse(venceu(estado))
        self.assertTrue(jogo_terminado(estado))

    def test_jogo_continua_em_estado_intermediario(self):
        estado = EstadoDoJogo(palavra="sol", letras_tentadas={"s"}, max_erros=6)
        self.assertFalse(jogo_terminado(estado))


if __name__ == "__main__":
    unittest.main()
