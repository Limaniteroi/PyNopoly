import sys
import os
import unittest

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.engine.Partida import Partida
from src.engine.Fabricas import TabuleiroPadraoFactory

class TestIntegracao(unittest.TestCase):

    def test_simulacao_partida(self):
        """Testa a simulação de uma partida com 4 jogadores por 20 rodadas."""
        print("\n--- Iniciando teste de simulação de partida ---")
        
        # Configuração da partida
        pecas = ["Carro", "Chapéu", "Cachorro", "Navio"]
        fabrica_tabuleiro = TabuleiroPadraoFactory()
        partida = Partida(pecas, fabrica_tabuleiro)

        # Verifica a configuração inicial
        self.assertEqual(len(partida.jogadores), 4)
        self.assertEqual(partida.jogadores[0].peca, "Carro")
        self.assertEqual(partida.jogadores[1].peca, "Chapéu")
        self.assertEqual(partida.jogadores[2].peca, "Cachorro")
        self.assertEqual(partida.jogadores[3].peca, "Navio")
        self.assertFalse(partida.em_andamento)

        # Inicia o jogo
        partida.iniciar_jogo()
        self.assertTrue(partida.em_andamento)

        # Simula 20 rodadas completas (80 turnos)
        for i in range(80):
            print(f"\n--- Rodada {i//4 + 1}, Turno {i%4 + 1} ---")
            jogador_antes = partida.jogadores[partida.jogador_atual_idx]
            posicao_antes = jogador_antes.posicao
            dinheiro_antes = jogador_antes.dinheiro

            partida.jogar_rodada()

            jogador_depois = partida.jogadores[partida.jogador_atual_idx-1] # O jogador que acabou de jogar

            print(f"Jogador: {jogador_depois.peca}")
            print(f"Posição: {posicao_antes} -> {jogador_depois.posicao}")
            print(f"Dinheiro: {dinheiro_antes} -> {jogador_depois.dinheiro}")
            print(f"Propriedades: {len(jogador_depois.propriedades)}")

            # Verifica se o estado do jogo mudou
            self.assertTrue(partida.em_andamento, "O jogo não deveria ter acabado ainda.")

        print("\n--- Teste de simulação de partida concluído ---")

if __name__ == '__main__':
    unittest.main()
