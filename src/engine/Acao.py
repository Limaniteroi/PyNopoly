from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from .Jogador import Jogador

if TYPE_CHECKING:
    from .Tabuleiro.Cadeia import Cadeia

class Acao(ABC):
    @abstractmethod
    def executar(self, jogador: Jogador):
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

    def executar(self, jogador: Jogador):
        jogador.mover(self._numero_de_casas)


# TO DO Preciso que as funções abaixo sejam implementadas em Jogador.py
# ir_para_cadeia, pagar_a_jogadores, ir_para_posicao

class AcaoIrParaCadeia(Acao):
    def executar(self, jogador: Jogador, cadeia: Cadeia):
        jogador.ir_para_cadeia(cadeia)


class AcaoPagarJogadores(Acao):
    def __init__(self, valor: int):
        self._valor = valor

    def executar(self, jogador_paga: Jogador, jogador_recebe: Jogador):
        jogador_paga.pagar_a_jogadores(self._valor, jogador_recebe)


class AcaoSaiaDaCadeia(Acao):
    def executar(self, jogador: Jogador):
        print(f"{jogador.nome} recebeu uma carta de 'Saia da Cadeia'.")


class AcaoAvanceParaInicio(Acao):
    def executar(self, jogador: Jogador):
        jogador.ir_para_posicao(0)