from __future__ import annotations
from typing import List
import random
from .Jogador import Jogador
from .Fabricas import TabuleiroAbstractFactory, TabuleiroPadraoFactory
from .Banco import Banco
from .Tabuleiro import Tabuleiro


class Partida:
    """
    GRASP CONTROLLER: Esta classe é responsável por gerenciar o fluxo e o estado
    geral do jogo Monopoly. Ela orquestra as interações entre os jogadores,
    o tabuleiro e o banco.
    """

    def __init__(self, pecas_jogadores: List[str], factory: TabuleiroAbstractFactory):
        print("Uma nova partida está sendo criada...")

        # GRASP CREATOR: A Partida cria os objetos que ela agrega e usa intensamente.
        self.banco = Banco()
        self.tabuleiro = factory.criar_tabuleiro()
        self.jogadores = [Jogador(peca) for peca in pecas_jogadores]

        # Atributos para controlar o estado do jogo
        self.jogador_atual_idx: int = 0
        self.em_andamento: bool = False

        print(f"Partida criada com {len(self.jogadores)} jogadores.")

    def iniciar_jogo(self):
        """Prepara e inicia o loop principal do jogo."""
        if not self.jogadores:
            print("Não há jogadores suficientes para iniciar a partida.")
            return

        self.em_andamento = True
        print("\n--- O JOGO COMEÇOU! ---")
        self.jogar_rodada()  # Inicia a primeira rodada

    def jogar_rodada(self):
        """Executa um turno completo para o jogador atual."""

        #Não sei se esse if seria necessário, conferir dps
        if not self.em_andamento:
            print("O jogo já terminou!")
            return

        jogador_da_vez = self.jogadores[self.jogador_atual_idx]

        # O método jogar_round do jogador lida com a lógica de estado (preso ou jogando)
        # e retorna o valor dos dados.
        valor_dados = jogador_da_vez.jogar_round()

        if valor_dados > 0:
            posicao_anterior = jogador_da_vez.posicao
            jogador_da_vez.mover(sum(valor_dados))

            # Lógica para pagar salário ao passar pelo Ponto de Partida
            if jogador_da_vez.posicao < posicao_anterior:
                print(f"{jogador_da_vez.peca} completou uma volta!")
                self.banco.pagar_salario(jogador_da_vez)

            # Obtém a casa onde o jogador parou e executa sua ação
            casa_atual = self.tabuleiro.get_casa_na_posicao(jogador_da_vez.posicao)
            casa_atual.executar_acao(jogador_da_vez, valor_dados)

        # Lógica para verificar se o jogo acabou
        self.verificar_fim_de_jogo()

        # Passa a vez para o próximo jogador
        self.proximo_jogador()

    def proximo_jogador(self):
        """Avança o turno para o próximo jogador na lista."""
        self.jogador_atual_idx = (self.jogador_atual_idx + 1) % len(self.jogadores)
        print("-" * 25)

