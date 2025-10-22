from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .Jogador import Jogador
    from .Tabuleiro.Cadeia import Cadeia

class Acao(ABC):
    @abstractmethod
    def executar(self, jogador: Jogador, jogadores: Optional[List[Jogador]] = None):
        pass


class AcaoReceberDinheiro(Acao):
    def __init__(self, valor: int):
        self._valor = valor

    def executar(self, jogador: Jogador):
        jogador.receber_dinheiro(self._valor)


class AcaoPagarDinheiro(Acao):
    def __init__(self, valor: int):
        self._valor = valor

    def executar(self, jogador: Jogador):
        jogador.enviar_dinheiro(self._valor)


class AcaoMoverCasas(Acao):
    def __init__(self, numero_de_casas: int):
        self._numero_de_casas = numero_de_casas

    def executar(self, jogador: Jogador, jogadores: Optional[List[Jogador]] = None):
        jogador.mover(self._numero_de_casas)


# TO DO Preciso que as funções abaixo sejam implementadas em Jogador.py
# ir_para_cadeia, pagar_a_jogadores, ir_para_posicao

class AcaoIrParaCadeia(Acao):
    def executar(self, jogador: Jogador):
        jogador.ir_para_cadeia()


class AcaoPagarJogadores(Acao):
    def __init__(self, valor: int):
        self._valor = valor

    def executar(self, jogador: Jogador, jogadores: List[Jogador]):
        jogador.pagar_a_jogadores(jogadores, self._valor)


class AcaoSaiaDaCadeia(Acao):
    def executar(self, jogador: Jogador):
        jogador.receber_carta_saia_da_cadeia()


class AcaoAvanceParaInicio(Acao):
    def executar(self, jogador: Jogador):
        jogador.ir_para_posicao(0)