from __future__ import annotations
from abc import ABC, abstractmethod
import random  # exemplo de baralho
from Jogador.py import Jogador


class Acao(ABC):
    @abstractmethod
    def executar(self, jogador: Jogador):
        pass


class AcaoReceberDinheiro(Acao):
    def __init__(self, valor: int):
        self._valor = valor

    def executar(self, jogador: Jogador):
        jogador.receber_dinheiro(self._valor)


class AcaoVaParaCadeia(Acao):
    def executar(self, jogador: Jogador):
        # Implementar com uma logica de pegar a posicao atual e subtrair/somar ate a cadeia
        pass


class AcaoAvanceParaInicio(Acao):
    def executar(self, jogador: Jogador):
        # Implementar com uma logica de pegar a posicao atual e subtrair/somar ate o incio
        pass


class Carta(ABC):
    def __init__(self, nome: str, acao: Acao):
        self.nome = nome
        self.acao = acao  # Composição: A Carta "tem uma" Acao

    def executar_acao(self, jogador: Jogador):
        print(f"Carta tirada: '{self.nome}'")
        self.acao.executar(jogador)


class CartaSorte(Carta):
    def __init__(self, nome: str, acao: Acao):
        super().__init__(nome, acao)


class CartaCofre(Carta):
    def __init__(self, nome: str, acao: Acao):
        super().__init__(nome, acao)


if __name__ == "__main__":
    # Criando um baralho de Sorte exemplo (not final)
    baralho_sorte = [
        CartaSorte("Seu aniversário! Receba $100.", AcaoReceberDinheiro(100)),
        CartaSorte(
            "Vá para a cadeia. Vá diretamente para a cadeia.", AcaoVaParaCadeia()
        ),
        CartaSorte("Avance para o Ponto de Partida.", AcaoAvanceParaInicio()),
    ]
    random.shuffle(baralho_sorte)

    # Criando um jogador para o teste
    jogador_teste = Jogador("Fernando")
    print(f"--- Turno de {jogador_teste.nome} ---")
    print("Jogador parou na casa Sorte!")

    # Simulação de tirar uma carta
    carta_puxada = baralho_sorte.pop(0)  # Pega a primeira carta do baralho

    # Executando a ação da carta
    carta_puxada.executar_acao(jogador_teste)

    # Coloca a carta de volta no final do baralho
    baralho_sorte.append(carta_puxada)

    print("\n--- Próximo Turno ---")
    # ... e o processo se repetiria
