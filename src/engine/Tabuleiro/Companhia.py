from __future__ import annotations
from typing import TYPE_CHECKING
from .Terreno import Terreno

if TYPE_CHECKING:
    from ..Jogador import Jogador

class Companhia(Terreno):
    def __init__(self, nome: str, posicao: int, preco: int, hipoteca: int):
        super().__init__(nome, posicao, preco, "")
        self.hipoteca = hipoteca

    def calcular_aluguel(self, val_dados: int = 0) -> int:
        if self.dono is None:
            return 0
        companhias = [p for p in self.dono.propriedades if isinstance(p, Companhia)]
        quantidade = len(companhias)
        if quantidade == 1:
            return 4 * val_dados
        elif quantidade == 2:
            return 10 * val_dados
        else:
            return 0
    
    def executar_acao(self, jogador: Jogador, val_dados: int = 0):
        pass