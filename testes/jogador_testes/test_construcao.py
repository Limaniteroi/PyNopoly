import sys
import os
import unittest

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.Jogador import Jogador
from src.Tabuleiro import Imovel

class TestJogadorConstruirCasa(unittest.TestCase):

    def setUp(self):
        """Set up a player and some properties for testing."""
        self.jogador = Jogador("Testador")
        self.imovel_marrom1 = Imovel("Leblon", 1, 60, 30, "Marrom", [], 50)
        self.imovel_marrom2 = Imovel("Av. Presidente Vargas", 3, 60, 30, "Marrom", [], 50)
        self.imovel_azul = Imovel("Av. Rebouças", 9, 120, 60, "Azul-Claro", [], 50)
        
        # Player owns all brown properties
        self.jogador.propriedades = [self.imovel_marrom1, self.imovel_marrom2]

    def test_construir_casa_sucesso(self):
        """Test successful house construction."""
        self.jogador.dinheiro = 200
        self.jogador.construir_casa(self.imovel_marrom1)
        self.assertEqual(self.imovel_marrom1.casas, 1)
        self.assertEqual(self.jogador.dinheiro, 150)

    def test_construir_casa_sem_dinheiro(self):
        """Test building a house with insufficient funds."""
        self.jogador.dinheiro = 40  # Less than house cost of 50
        self.jogador.construir_casa(self.imovel_marrom1)
        self.assertEqual(self.imovel_marrom1.casas, 0)
        self.assertEqual(self.jogador.dinheiro, 40)

    def test_construir_de_forma_nao_uniforme(self):
        """Test uneven building is prevented."""
        self.jogador.dinheiro = 200
        # Build one house on the first property
        self.imovel_marrom1.casas = 1
        # Try to build a second on the same property before building on the other
        self.jogador.construir_casa(self.imovel_marrom1)
        # Should fail, houses should remain 1
        self.assertEqual(self.imovel_marrom1.casas, 1)
        self.assertEqual(self.jogador.dinheiro, 200) # Money should not be deducted

    def test_construir_hotel(self):
        """Test building up to a hotel (5 houses)."""
        self.jogador.dinheiro = 300
        self.imovel_marrom1.casas = 4
        self.imovel_marrom2.casas = 4
        # Build the 5th house (hotel)
        self.jogador.construir_casa(self.imovel_marrom1)
        self.assertEqual(self.imovel_marrom1.casas, 5)
        self.assertEqual(self.jogador.dinheiro, 250)

    def test_construir_alem_do_hotel(self):
        """Test trying to build beyond a hotel."""
        self.jogador.dinheiro = 100
        self.imovel_marrom1.casas = 5 # Already has a hotel
        self.imovel_marrom2.casas = 5
        self.jogador.construir_casa(self.imovel_marrom1)
        self.assertEqual(self.imovel_marrom1.casas, 5)
        self.assertEqual(self.jogador.dinheiro, 100)

if __name__ == '__main__':
    unittest.main()
