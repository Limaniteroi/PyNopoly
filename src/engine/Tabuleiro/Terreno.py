from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from .CasaTabuleiro import CasaTabuleiro

if TYPE_CHECKING:
    from ..Jogador import Jogador


class Terreno(CasaTabuleiro, ABC):
    def __init__(self, nome: str, pos: int, preco: int, cor: str):
        super().__init__(nome, pos)
        self.preco = preco
        self.dono = None
        self.hipotecado: bool = False

    @abstractmethod
    def calcular_aluguel(self, val_dados: int = 0) -> int:
        pass

    def set_dono(self, jogador: Jogador):
        self.dono = jogador

    def action(self, jogador: Jogador, val_dados: int = 0):
        pass
