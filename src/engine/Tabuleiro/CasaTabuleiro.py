from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from ..Jogador import Jogador


class CasaTabuleiro(ABC):
    def __init__(self, nome: str, pos: int):
        self.nome = nome
        self.pos = pos

    @abstractmethod
    def executar_acao(self, jogador: Jogador, val_dados: int = 0):
        pass
