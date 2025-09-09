from abc import ABC, abstractmethod
from typing import List, Optional

class CasaTabuleiro(ABC):
    def __init__(self, nome: str, pos: int):
        self.nome = nome
        self.pos = pos

    @abstractmethod
    def action(self, jogador: Jogador, val_dados: int = 0):
        pass

class Terreno(CasaTabuleiro):
    def __init__(self, nome: str, pos: int ,preco: int, valAluguelInicial: int, cor: String, hipotecado: Bool):
        super.__init__(nome, pos)
        self.preco = preco
        self.valAluguelInicial = valAluguelInicial
        self.cor = cor
        self.dono = Optional[Jogador] = None
        self.hipotecado: Bool = False

    @abstractmethod
    def calcularAluguel(self, val_dados: int = 0) -> int:
        TODO
        pass

    def action(self, jogador: Jogador):
        TODO
        pass

class Imovel(Terreno):
    def __init__(self, nome: str, posicao: int, preco: int, hipoteca: int, cor: str):
        super().__init__(nome, posicao, preco, hipoteca)
        self.cor = cor
        self.casas = 0
    
    def calcular_aluguel(self, valor_dados: int = 0) -> int:
        aluguel_base = self.preco // 10
        return aluguel_base * (self.casas + 1)

class Estacao(Terreno):
    def calcular_aluguel(self, valor_dados: int = 0) -> int:
        if self.dono is None: return 0
        num_estacoes = sum(1 for prop in self.dono.propriedades if isinstance(prop, Estacao))
        return 25 * (2 ** (num_estacoes - 1)) # 25, 50, 100, 200

class Companhia(Terreno):
    def calcular_aluguel(self, valor_dados: int = 0) -> int:
        if self.dono is None or valor_dados == 0: return 0
        num_companhias = sum(1 for prop in self.dono.propriedades if isinstance(prop, Companhia))
        multiplicador = 10 if num_companhias <= 2 else 4
        return valor_dados * multiplicador

class PontoDePartida(CasaTabuleiro):
    def executar_acao(self, jogador: Jogador, valor_dados: int = 0):
        print(f"{jogador.nome} está no Ponto de Partida.")

class CasaSorte(CasaTabuleiro):
    def executar_acao(self, jogador: Jogador, valor_dados: int = 0):
        print(f"{jogador.nome} parou em 'Sorte'. Tire uma carta!")
        # Futuramente, aqui chamaremos o baralho para puxar uma carta

class CasaCofre(CasaTabuleiro):
    def executar_acao(self, jogador: Jogador, valor_dados: int = 0):
        print(f"{jogador.nome} parou em 'Cofre Comunitário'. Tire uma carta!")
        # Futuramente, aqui chamaremos o baralho para puxar uma carta

class Cadeia(CasaTabuleiro):
    def executar_acao(self, jogador: Jogador, valor_dados: int = 0):
        print(f"{jogador.nome} está apenas visitando a cadeia.")

class VaParaCadeia(CasaTabuleiro):
    def executar_acao(self, jogador: Jogador, valor_dados: int = 0):
        pass

class EstacionamentoLivre(CasaTabuleiro):
    def executar_acao(self, jogador: Jogador, valor_dados: int = 0):
        pass

class Imposto(CasaTabuleiro):
    def __init__(self, nome: str, posicao: int, valor_imposto: int):
        super().__init__(nome, posicao)
        self.valor_imposto = valor_imposto

    def executar_acao(self, jogador: Jogador, valor_dados: int = 0):
        # Futuramente, aqui chamaremos um método como jogador.pagar_ao_banco(valor)

class Tabuleiro:
    def __init__(self, casas: List[CasaTabuleiro]):
        # O tabuleiro é criado já recebendo as casas prontas da Factory.
        self.casas = casas

    def get_casa_na_posicao(self, posicao: int) -> CasaTabuleiro:
        # O operador % garante que a posição seja circular (de 0 a 39)
        # mas tambpm podemos deixar com que if pos > 40 fazer uma lógica para mudar.
        posicao_real = posicao % len(self.casas)
        return self.casas[posicao_real]

