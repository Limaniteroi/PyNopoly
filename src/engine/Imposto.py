from __future__ import annotations
from typing import TYPE_CHECKING
from .Tabuleiro.CasaTabuleiro import CasaTabuleiro

if TYPE_CHECKING:
    from .Jogador import Jogador

class Imposto(CasaTabuleiro):
    def __init__(self, nome: str, posicao: int, valor_imposto: int):
        super().__init__(nome, posicao)
        self.valor_imposto = valor_imposto

    def executar_acao(self, jogador: Jogador, val_dados: int = 0):
        pass