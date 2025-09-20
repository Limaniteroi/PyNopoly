import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.Jogador import Jogador, JogadorFalidoState
from src.Tabuleiro import Imovel

class TestJogadorFinancas(unittest.TestCase):

    def setUp(self):
        self.jogador1 = Jogador("Jogador 1")
        self.jogador2 = Jogador("Jogador 2")
        self.imovel = Imovel("Propriedade Cara", 1, 200, 100, "Azul", [20], 100)

    def test_comprar_imovel_sucesso(self):
        """Test successful property purchase."""
        self.jogador1.dinheiro = 300
        self.jogador1.comprar_imovel(self.imovel)
        self.assertEqual(self.jogador1.dinheiro, 100)
        self.assertIn(self.imovel, self.jogador1.propriedades)
        self.assertEqual(self.imovel.dono, self.jogador1)

    def test_comprar_imovel_sem_dinheiro(self):
        """Test buying with insufficient funds."""
        self.jogador1.dinheiro = 100
        self.jogador1.comprar_imovel(self.imovel)
        self.assertEqual(self.jogador1.dinheiro, 100)
        self.assertNotIn(self.imovel, self.jogador1.propriedades)
        self.assertIsNone(self.imovel.dono)

    def test_pagar_aluguel_sucesso(self):
        """Test successful rent payment."""
        self.jogador1.dinheiro = 250
        self.jogador2.dinheiro = 50
        self.jogador1.pagar_aluguel(self.jogador2, 50)
        self.assertEqual(self.jogador1.dinheiro, 200)
        self.assertEqual(self.jogador2.dinheiro, 100)

    def test_pagar_aluguel_falencia(self):
        """Test rent payment leading to bankruptcy."""
        self.jogador1.dinheiro = 30
        self.jogador1.pagar_aluguel(self.jogador2, 50)
        self.assertIsInstance(self.jogador1.estado_atual, JogadorFalidoState)

    def test_receber_dinheiro(self):
        """Test receiving money."""
        self.jogador1.dinheiro = 100
        self.jogador1.receber_dinheiro(50)
        self.assertEqual(self.jogador1.dinheiro, 150)

    def test_calcular_valor_total(self):
        """Test calculation of total assets."""
        self.jogador1.dinheiro = 500
        imovel1 = Imovel("Prop1", 1, 200, 100, "Verde", [], 150)
        imovel2 = Imovel("Prop2", 2, 300, 150, "Azul", [], 200)
        imovel2.casas = 2
        self.jogador1.propriedades = [imovel1, imovel2]
        # NOTE: This test depends on the hardcoded `custo_casa = 100` in the `calcular_valor_total` method.
        # valor_total = 500 (dinheiro) + 200 (prop1) + 300 (prop2) + 2 * 100 (casas) = 1200
        self.assertEqual(self.jogador1.calcular_valor_total(), 1200)

    def test_calcular_imposto(self):
        """Test tax calculation."""
        # Case 1: 10% is less than 200
        self.jogador1.dinheiro = 1500
        self.jogador1.propriedades = []
        # valor_total = 1500, 10% = 150. min(200, 150) = 150
        self.assertEqual(self.jogador1.calcular_imposto(), 150)

        # Case 2: 10% is more than 200
        self.jogador1.dinheiro = 2500
        # valor_total = 2500, 10% = 250. min(200, 250) = 200
        self.assertEqual(self.jogador1.calcular_imposto(), 200)

if __name__ == '__main__':
    unittest.main()
