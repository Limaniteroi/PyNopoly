from __future__ import annotations
from typing import TYPE_CHECKING
from .Terreno import Terreno

if TYPE_CHECKING:
    from ..Jogador import Jogador

class Estacao(Terreno):
    def __init__(self, nome: str, posicao: int, preco: int, hipoteca: int):
        super().__init__(nome, posicao, preco, "")
        self.hipoteca = hipoteca

    def calcular_aluguel(self, val_dados: int = 0) -> int:
        if self.dono is None:
            return 0
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
    
    def executar_acao(self, jogador: Jogador, val_dados: int = 0):
        pass