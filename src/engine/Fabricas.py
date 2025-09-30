from __future__ import annotations
from abc import abstractmethod, ABC
from typing import List, TYPE_CHECKING
from .Tabuleiro.Tabuleiro import Tabuleiro
from .Tabuleiro.CasaTabuleiro import CasaTabuleiro
from .Tabuleiro.PontoDePartida import PontoDePartida
from .Imovel import Imovel
from .Tabuleiro.CasaCofre import CasaCofre
from .Imposto import Imposto
from .Tabuleiro.Estacao import Estacao
from .Tabuleiro.CasaSorte import CasaSorte
from .Tabuleiro.Cadeia import Cadeia
from .Tabuleiro.Companhia import Companhia
from .Tabuleiro.EstacionamentoLivre import EstacionamentoLivre
from .Tabuleiro.VaParaCadeia import VaParaCadeia

if TYPE_CHECKING:
    from .Jogador import Jogador

class TabuleiroAbstractFactory(ABC):
    @abstractmethod
    def criar_tabuleiro(self) -> Tabuleiro:
        pass

class TabuleiroPadraoFactory(TabuleiroAbstractFactory):
    def criar_tabuleiro(self) -> Tabuleiro:
        casas: List[CasaTabuleiro] = []

        # Lado 1 do Tabuleiro (Do Ponto de Partida à Cadeia)
        casas.append(PontoDePartida("Ponto de Partida", 0))
        casas.append(Imovel("Leblon", 1, 60, 30, "Marrom", [2, 10, 30, 90, 160, 250], 50))
        casas.append(CasaCofre("Cofre Comunitário", 2))
        casas.append(Imovel("Av. Presidente Vargas", 3, 60, 30, "Marrom", [4, 20, 60, 180, 320, 450], 50))
        casas.append(Imposto("Imposto de Renda", 4, 200))
        casas.append(Estacao("Estação de Metrô da Central do Brasil", 5, 200, 100))
        casas.append(Imovel("Av. Nossa S. de Copacabana", 6, 100, 50, "Azul-Claro", [6, 30, 90, 270, 400, 550], 50))
        casas.append(CasaSorte("Sorte", 7))
        casas.append(Imovel("Av. Brigadeiro Faria Lima", 8, 100, 50, "Azul-Claro", [6, 30, 90, 270, 400, 550], 50))
        casas.append(Imovel("Av. Rebouças", 9, 120, 60, "Azul-Claro", [8, 40, 100, 300, 450, 600], 50))
        casas.append(Cadeia("Cadeia (Apenas Visitando)", 10))

        # Lado 2 do Tabuleiro
        casas.append(Imovel("Av. 9 de Julho", 11, 140, 70, "Rosa", [10, 50, 150, 450, 625, 750], 100))
        casas.append(Companhia("Companhia de Eletricidade", 12, 150, 75))
        casas.append(Imovel("Rua Augusta", 13, 140, 70, "Rosa", [10, 50, 150, 450, 625, 750], 100))
        casas.append(Imovel("Av. Pacaembu", 14, 160, 80, "Rosa", [12, 60, 180, 500, 700, 900], 100))
        casas.append(Estacao("Estação de Metrô da Sé", 15, 200, 100))
        casas.append(Imovel("Interlagos", 16, 180, 90, "Laranja", [14, 70, 200, 550, 750, 950], 100))
        casas.append(CasaCofre("Cofre Comunitário", 17))
        casas.append(Imovel("Morumbi", 18, 180, 90, "Laranja", [14, 70, 200, 550, 750, 950], 100))
        casas.append(Imovel("Ibirapuera", 19, 200, 100, "Laranja", [16, 80, 220, 600, 800, 1000], 100))
        casas.append(EstacionamentoLivre("Estacionamento Livre", 20))

        # Lado 3 do Tabuleiro
        casas.append(Imovel("Copacabana", 21, 220, 110, "Vermelho", [18, 90, 250, 700, 875, 1050], 150))
        casas.append(CasaSorte("Sorte", 22))
        casas.append(Imovel("Barra da Tijuca", 23, 220, 110, "Vermelho", [18, 90, 250, 700, 875, 1050], 150))
        casas.append(Imovel("Jardim Botânico", 24, 240, 120, "Vermelho", [20, 100, 300, 750, 925, 1100], 150))
        casas.append(Estacao("Estação de Metrô de Botafogo", 25, 200, 100))
        casas.append(Imovel("Av. Brasil", 26, 260, 130, "Amarelo", [22, 110, 330, 800, 975, 1150], 150))
        casas.append(Imovel("Av. Ipiranga", 27, 260, 130, "Amarelo", [22, 110, 330, 800, 975, 1150], 150))
        casas.append(Companhia("Companhia de Água", 28, 150, 75))
        casas.append(Imovel("Av. Paulista", 29, 280, 140, "Amarelo", [24, 120, 360, 850, 1025, 1200], 150))
        casas.append(VaParaCadeia("Vá para a Cadeia", 30))

        # Lado 4 do Tabuleiro
        casas.append(Imovel("Jardins", 31, 300, 150, "Verde", [26, 130, 390, 900, 1100, 1275], 200))
        casas.append(Imovel("Av. Vieira Souto", 32, 300, 150, "Verde", [26, 130, 390, 900, 1100, 1275], 200))
        casas.append(CasaCofre("Cofre Comunitário", 33))
        casas.append(Imovel("Av. Atlântica", 34, 320, 160, "Verde", [28, 150, 450, 1000, 1200, 1400], 200))
        casas.append(Estacao("Estação de Metrô da Luz", 35, 200, 100))
        casas.append(CasaSorte("Sorte", 36))
        casas.append(Imovel("Rua Oscar Freire", 37, 350, 175, "Azul-Escuro", [35, 175, 500, 1100, 1300, 1500], 200))
        casas.append(Imposto("Taxa de Riqueza", 38, 75))
        casas.append(Imovel("Ipanema", 39, 400, 200, "Azul-Escuro", [50, 200, 600, 1400, 1700, 2000], 200))
        
        return Tabuleiro(casas)
