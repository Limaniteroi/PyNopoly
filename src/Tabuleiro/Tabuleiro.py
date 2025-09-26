from __future__ import annotations
from typing import List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .CasaTabuleiro import CasaTabuleiro
    from ..Jogador import Jogador

class Tabuleiro:
    def __init__(self, casas: List[CasaTabuleiro]):
        self.casas = casas

    def get_casa_na_posicao(self, posicao: int) -> Optional[CasaTabuleiro]:
        if 0 <= posicao < len(self.casas):
            return self.casas[posicao]
        return None
