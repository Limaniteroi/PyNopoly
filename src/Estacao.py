from .Terreno import Terreno
from .Jogador import Jogador    

class Estacao(Terreno):
    def __init__(self, nome: str, posicao: int, preco: int, hipoteca: int):
        super().__init__(nome, posicao, preco, "")
        self.hipoteca = hipoteca

    def calcular_aluguel(self, val_dados: int = 0) -> int:
        ferrovias = [p for p in self.dono.propriedades if isinstance(p, Estacao)]
        quantidade = len(ferrovias)
        if quantidade == 1:
            return 25
        elif quantidade == 2:
            return 50
        elif quantidade == 3:
            return 100
        elif quantidade == 4:
            return 200
        else:
            return 0
    
    def action(self, jogador: Jogador, val_dados: int = 0):
        pass