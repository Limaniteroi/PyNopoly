from .CasaTabuleiro import CasaTabuleiro
from .Jogador import Jogador    

class Imposto(CasaTabuleiro):
    def __init__(self, nome: str, posicao: int, valor_imposto: int):
        super().__init__(nome, posicao)
        self.valor_imposto = valor_imposto

    def action(self, jogador: Jogador, val_dados: int = 0):
        pass