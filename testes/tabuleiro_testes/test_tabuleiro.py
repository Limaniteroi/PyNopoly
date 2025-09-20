import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import unittest
from src.Tabuleiro import Terreno, Imovel
from src.Jogador import Jogador

class TestTerreno(unittest.TestCase):
    def test_set_dono(self):
        terreno = Imovel("Leblon", 0, 1000, 100, "Azul", [10, 20, 30, 40, 50, 60], 50)
        jogador = Jogador("Jogador 1")
        terreno.set_dono(jogador)
        self.assertEqual(terreno.dono, jogador)

if __name__ == '__main__':
    unittest.main()