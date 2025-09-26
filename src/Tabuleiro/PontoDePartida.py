from __future__ import annotations
from typing import TYPE_CHECKING
from .CasaTabuleiro import CasaTabuleiro

if TYPE_CHECKING:
    from ..Jogador import Jogador

class PontoDePartida(CasaTabuleiro):
    def executar_acao(self, jogador: Jogador, val_dados: int = 0):
        pass

