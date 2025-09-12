from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod
from Terreno.py import Terreno, Imovel


class JogadorState(ABC):
    @abstractmethod
    def executar_acao_do_turno(self, jogador: Jogador):
        pass


class JogadorJogandoState(JogadorState):
    def executar_acao_do_turno(self, jogador: Jogador):
        print(f"Estado de {jogador.nome}: Jogando Normalmente. Rolando dados...")
        # Lógica de rolar dados e chamar o método mover() do jogador.


class JogadorPresoState(JogadorState):
    def executar_acao_do_turno(self, jogador: Jogador):
        print(f"Estado de {jogador.nome}: Preso. Tentando sair da cadeia...")
        # Lógica de tentar rolar dupla, pagar ou usar carta.


class JogadorFalidoState(JogadorState):
    def executar_acao_do_turno(self, jogador: Jogador):
        print(
            f"Estado de {jogador.nome}: Falido. Tal metodo não deveria ter sido chamado, erro de lógica."
        )


class Jogador:
    def __init__(self, nome: str, peca: str):
        self.nome = nome
        self.peca = peca
        self.dinheiro: int = 1500
        self.posicao: int = 0

        # Terrenos
        self.propriedades: List[Terreno] = []
        self.estado_atual: JogadorState = JogadorJogandoState()  # Padrão State
        self.cartas: int = 0

    def jogar_round(self):
        """
        Executa a rodada do jogador.
        Este método aplica o Padrão de Projeto State, delegando a ação
        para o objeto de estado atual do jogador.
        """
        self.estado_atual.executar_acao_do_turno(self)

    def mover(self, passos: int):
        # O operador % 40 garante que o tabuleiro seja circular (posições 0 a 39)
        self.posicao = (self.posicao + passos) % 40
        print(f"{self.nome} moveu-se {passos} casas e está na posição {self.posicao}.")

    def comprar_imovel(self, imovel: Terreno):
        """Tenta comprar um imóvel. O jogador deve ter dinheiro suficiente."""
        if self.dinheiro >= imovel.preco:
            self.dinheiro -= imovel.preco
            self.propriedades.append(imovel)
            imovel.set_dono(self)
            print(f"{self.nome} comprou {imovel.nome} por ${imovel.preco}.")
        else:
            print(f"{self.nome} não tem dinheiro para comprar {imovel.nome}.")

    def pagar_aluguel(self, dono: Jogador, valor: int):
        """Paga um valor de aluguel para outro jogador."""
        if self.dinheiro >= valor:
            self.dinheiro -= valor
            dono.receber_dinheiro(valor)
            print(f"{self.nome} pagou ${valor} de aluguel para {dono.nome}.")
        else:
            print(f"{self.nome} não tem dinheiro para pagar o aluguel e faliu!")
            self.mudar_estado(JogadorFalidoState())
            # Lógica de falência viria aqui tirar imoveis? apagar peca?

    def receber_dinheiro(self, valor: int):
        self.dinheiro += valor

    def construir_casa(self, imovel: Imovel):
        """Constrói uma casa em um imóvel."""
        # A lógica aqui é complexa:
        # 1. Verificar se o jogador tem o monopólio da cor do imóvel.
        # 2. Verificar a regra de construção uniforme (não pode ter 2 casas em um
        #    se outro tiver 0) <- N sei se faremos isso ou n.
        # 3. Verificar se o jogador tem dinheiro.
        # 4. Debitar o valor e incrementar o número de casas no imóvel.
        print(f"{self.nome} tentando construir casa em {imovel.nome}...")
        pass

    def calcular_imposto(self) -> int:
        """Calcula o imposto a ser pago. Pode ter lógicas diferentes."""
        # A regra do Imposto de Renda permite escolher entre $200 ou 10% do seu valor total.
        # Isso exigiria um método para calcular o valor total (dinheiro + propriedades + construções).
        pass

    def ir_para_cadeia(self):
        """Muda o estado do jogador para 'Preso' e o move para a cadeia."""
        self.posicao = 10  # Posição da cadeia no tabuleiro padrão
        self.mudar_estado(JogadorPresoState())
        print(f"{self.nome} foi para a cadeia!")

    def mudar_estado(self, novo_estado: JogadorState):
        """Altera o objeto de estado do jogador."""
        self.estado_atual = novo_estado
