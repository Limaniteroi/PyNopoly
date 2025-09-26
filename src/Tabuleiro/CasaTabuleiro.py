from .Jogador import Jogador
from abc import ABC, abstractmethod

class CasaTabuleiro(ABC):
    def __init__(self, nome: str, pos: int):
        self.nome = nome
        self.pos = pos

    @abstractmethod
    def action(self, jogador: Jogador, val_dados: int = 0):
        pass
