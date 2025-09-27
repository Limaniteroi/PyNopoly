import sys
import os
import unittest

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.engine.Partida import Partida
from src.engine.Fabricas import TabuleiroPadraoFactory

class TestIntegracao(unittest.TestCase):

    def test_simulacao_partida(self):
        """Testa a simulação de uma partida com 2 jogadores por 5 rodadas."""
        print("\n--- Iniciando teste de simulação de partida ---")
        
        # Configuração da partida
        pecas = ["Carro", "Chapéu"]
        fabrica_tabuleiro = TabuleiroPadraoFactory()
        partida = Partida(pecas, fabrica_tabuleiro)

        # Verifica a configuração inicial
        self.assertEqual(len(partida.jogadores), 2)
        self.assertEqual(partida.jogadores[0].peca, "Carro")
        self.assertEqual(partida.jogadores[1].peca, "Chapéu")
        self.assertFalse(partida.em_andamento)

        # Inicia o jogo
        partida.iniciar_jogo()
        self.assertTrue(partida.em_andamento)

        # Simula 5 rodadas completas (10 turnos)
        for i in range(10):
            print(f"\n--- Rodada {i//2 + 1}, Turno {i%2 + 1} ---")
            jogador_antes = partida.jogadores[partida.jogador_atual_idx]
            posicao_antes = jogador_antes.posicao
            dinheiro_antes = jogador_antes.dinheiro

            partida.jogar_rodada()

            # Verifica se o estado do jogo mudou
            self.assertTrue(partida.em_andamento, "O jogo não deveria ter acabado ainda.")
            # É possível que a posição não mude se o jogador estiver preso
            # Por isso, não há um assert direto na posição

        print("\n--- Teste de simulação de partida concluído ---")

if __name__ == '__main__':
    unittest.main()
