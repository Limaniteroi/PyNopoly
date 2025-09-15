from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from .Jogador import Jogador

class CasaTabuleiro(ABC):
    def __init__(self, nome: str, pos: int):
        self.nome = nome
        self.pos = pos

    @abstractmethod
    def action(self, jogador: Jogador, val_dados: int = 0):
        pass

class Terreno(CasaTabuleiro):
    def __init__(self, nome: str, pos: int ,preco: int, cor: str):
        super().__init__(nome, pos)
        self.preco = preco
        self.cor = cor
        self.dono: Optional[Jogador] = None
        self.hipotecado: bool = False

    @abstractmethod
    def calcularAluguel(self, val_dados: int = 0) -> int:
        pass

    def action(self, jogador: Jogador, val_dados: int = 0):
        pass

class Imovel(Terreno):
    def __init__(self, nome: str, posicao: int, preco: int, hipoteca: int, cor: str, alugueis: List[int]):
        super().__init__(nome, posicao, preco, cor)
        self.hipoteca = hipoteca
        self.alugueis = alugueis
        self.casas = 0
    
    def calcularAluguel(self, valor_dados: int = 0) -> int:
        # A lógica do aluguel foi simplificada para o teste
        return 0

class Estacao(Terreno):
    def __init__(self, nome: str, posicao: int, preco: int, hipoteca: int):
        super().__init__(nome, posicao, preco, "")
        self.hipoteca = hipoteca

    def calcularAluguel(self, val_dados: int = 0) -> int:
        # A lógica do aluguel foi simplificada para o teste
        return 0

class Companhia(Terreno):
    def __init__(self, nome: str, posicao: int, preco: int, hipoteca: int):
        super().__init__(nome, posicao, preco, "")
        self.hipoteca = hipoteca

    def calcularAluguel(self, val_dados: int = 0) -> int:
        # A lógica do aluguel foi simplificada para o teste
        return 0

class PontoDePartida(CasaTabuleiro):
    def action(self, jogador: Jogador, val_dados: int = 0):
        pass

class CasaSorte(CasaTabuleiro):
    def action(self, jogador: Jogador, val_dados: int = 0):
        pass

class CasaCofre(CasaTabuleiro):
    def action(self, jogador: Jogador, val_dados: int = 0):
        pass

class Cadeia(CasaTabuleiro):
    def action(self, jogador: Jogador, val_dados: int = 0):
        pass

class VaParaCadeia(CasaTabuleiro):
    def action(self, jogador: Jogador, val_dados: int = 0):
        pass

class EstacionamentoLivre(CasaTabuleiro):
    def action(self, jogador: Jogador, val_dados: int = 0):
        pass

class Imposto(CasaTabuleiro):
    def __init__(self, nome: str, posicao: int, valor_imposto: int):
        super().__init__(nome, posicao)
        self.valor_imposto = valor_imposto

    def action(self, jogador: Jogador, val_dados: int = 0):
        pass

class Tabuleiro:
    def __init__(self, casas: List[CasaTabuleiro]):
        self.casas = casas

    def get_casa_na_posicao(self, posicao: int) -> CasaTabuleiro:
        posicao_real = posicao % len(self.casas)
        return self.casas[posicao_real]
