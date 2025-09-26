from __future__ import annotations
from typing import List, TYPE_CHECKING
from .CasaTabuleiro import CasaTabuleiro

if TYPE_CHECKING:
    from .Jogador import Jogador

class Tabuleiro:
    def __init__(self, casas: List[CasaTabuleiro]):
        self.casas = casas

    def get_casa_na_posicao(self, posicao: int) -> CasaTabuleiro:
        posicao_real = posicao % len(self.casas)
        return self.casas[posicao_real]
