from __future__ import annotations
from typing import List
import random

# Importando as classes dos outros módulos do projeto
from .jogador import Jogador
from .fabricas import TabuleiroAbstractFactory, TabuleiroPadraoFactory
from .banco import Banco
from .tabuleiro import Tabuleiro


class Partida:
    """
    GRASP CONTROLLER: Esta classe é responsável por gerenciar o fluxo e o estado
    geral do jogo Monopoly. Ela orquestra as interações entre os jogadores,
    o tabuleiro e o banco.
    """

    def __init__(self, nomes_jogadores: List[str], factory: TabuleiroAbstractFactory):
        print("Uma nova partida está sendo criada...")

        # GRASP CREATOR: A Partida cria os objetos que ela agrega e usa intensamente.
        self.banco = Banco()
        self.tabuleiro = factory.cria_tabuleiro()
        self.jogadores = [
            Jogador(nome, f"Peça {i + 1}") for i, nome in enumerate(nomes_jogadores)
        ]

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
        if not self.em_andamento:
            print("O jogo já terminou!")
            return

        jogador_da_vez = self.jogadores[self.jogador_atual_idx]

        # O método jogar_round do jogador lida com a lógica de estado (preso ou jogando)
        # e retorna o valor dos dados.
        valor_dados = jogador_da_vez.jogar_round()

        # A Partida, como Controller, pega o resultado e atualiza o estado do jogo
        if valor_dados > 0:
            posicao_anterior = jogador_da_vez.posicao
            jogador_da_vez.mover(valor_dados)

            # Lógica para pagar salário ao passar pelo Ponto de Partida
            if jogador_da_vez.posicao < posicao_anterior:
                print(f"{jogador_da_vez.nome} completou uma volta!")
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

    def verificar_fim_de_jogo(self):
        """Verifica se há apenas um jogador restante."""
        jogadores_ativos = [j for j in self.jogadores if not j.faliu]
        if len(jogadores_ativos) == 1:
            self.em_andamento = False
            print(f"\n--- FIM DE JOGO! O VENCEDOR É {jogadores_ativos[0].nome}! ---")


# --- Exemplo de como usar a classe Partida (para testes) ---
if __name__ == "__main__":
    # 1. Escolha uma fábrica
    fabrica = TabuleiroPadraoFactory()

    # 2. Crie uma instância da Partida
    nomes = ["Alice", "Beto"]
    minha_partida = Partida(nomes_jogadores=nomes, factory=fabrica)

    # 3. Inicie o jogo
    minha_partida.iniciar_jogo()

    # Em um jogo real, haveria um loop aqui controlado por input do usuário
    # que chamaria minha_partida.jogar_rodada() a cada turno.
