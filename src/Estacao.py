from .Terreno import Terreno
from .Jogador import Jogador    

class Estacao(Terreno):
    def __init__(self, nome: str, posicao: int, preco: int, hipoteca: int):
        super().__init__(nome, posicao, preco, "")
        self.hipoteca = hipoteca

    def calcular_aluguel(self, val_dados: int = 0) -> int:
        # A lógica do aluguel foi simplificada para o teste
        return 0
    
    def set_dono(self, jogador: Jogador):
        self.dono = jogador

    def action(self, jogador: Jogador, val_dados: int = 0):
        pass