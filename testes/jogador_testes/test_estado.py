import sys
import os
import unittest
from unittest.mock import Mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.Jogador import Jogador, JogadorJogandoState, JogadorPresoState

class TestJogadorEstado(unittest.TestCase):

    def setUp(self):
        self.jogador = Jogador("Testador")

    def test_mudar_estado(self):
        """Test changing the player's state."""
        novo_estado = JogadorPresoState()
        self.jogador.mudar_estado(novo_estado)
        self.assertIsInstance(self.jogador.estado_atual, JogadorPresoState)

    def test_jogar_round_delega_para_estado(self):
        """Test that jogar_round() calls the current state's method."""
        # Create a mock state
        mock_estado = Mock()
        
        # Assign the mock state to the player
        self.jogador.estado_atual = mock_estado
        
        # Call the method that should delegate to the state
        self.jogador.jogar_round()
        
        # Assert that the state's method was called exactly once with the player object
        mock_estado.executar_acao_do_turno.assert_called_once_with(self.jogador)

if __name__ == '__main__':
    unittest.main()
