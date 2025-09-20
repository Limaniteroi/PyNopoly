import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.Jogador import Jogador

class TestJogadorMovimentacao(unittest.TestCase):

    def setUp(self):
        self.jogador = Jogador("Testador")

    def test_mover_simples(self):
        """Test basic movement."""
        self.jogador.mover(5)
        self.assertEqual(self.jogador.posicao, 5)

    def test_mover_com_wrap_around(self):
        """Test movement that wraps around the board."""
        self.jogador.posicao = 38
        self.jogador.mover(5) # 38 + 5 = 43 -> 43 % 40 = 3
        self.assertEqual(self.jogador.posicao, 3)
        
    def test_mover_exato_para_inicio(self):
        """Test landing exactly on the start position."""
        self.jogador.posicao = 30
        self.jogador.mover(10) # 30 + 10 = 40 -> 40 % 40 = 0
        self.assertEqual(self.jogador.posicao, 0)

if __name__ == '__main__':
    unittest.main()
