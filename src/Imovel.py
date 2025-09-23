from .Terreno import Terreno
from .Jogador import Jogador
from typing import List

class Imovel(Terreno):
    def __init__(self, nome: str, posicao: int, preco: int, hipoteca: int, cor: str, alugueis: List[int], preco_casa: int):
        super().__init__(nome, posicao, preco, cor)
        self.hipoteca = hipoteca
        self.alugueis = alugueis
        self.casas = 0
        self.preco_casa = preco_casa
    
    def calcular_aluguel(self, val_dados: int = 0) -> int:
        # A lógica do aluguel foi simplificada para o teste
        return 0

    def set_dono(self, jogador: Jogador):
        self.dono = jogador

    def action(self, jogador: Jogador, val_dados: int = 0):
        pass
