from __future__ import annotations
import random  
from abc import ABC
from typing import List
from .Jogador import Jogador
from .Acao import Acao, AcaoReceberDinheiro, AcaoPagarDinheiro, AcaoIrParaCadeia, AcaoMoverCasas, AcaoPagarJogadores, AcaoSaiaDaCadeia


class Carta(ABC):
    def __init__(self, nome: str, acao: Acao, tipo: str):
        self.nome = nome
        self.acao = acao  
        self.tipo = tipo

    def executar_acao(self, jogador: Jogador):

        cartas_sorte = [] # TO DO adicionar os pngs
        cartas_azar = [] # TO DO Adicionar os pngs

        if self.tipo == 'Sorte':
            selecionando_png_sorte = random.choice(cartas_sorte)
            print(f"Mostrando imagem: {selecionando_png_sorte}")
        else:
            selecionando_png_azar = random.choice(cartas_azar)
            print(f"Mostrando imagem: {selecionando_png_azar}")

        print(f"Carta tirada: '{self.nome}'")
        self.acao.executar(jogador)


class Baralho:
    def __init__(self, cartas: List[Carta]):
        self._cartas = cartas
        self._cartas_descarte = []
        self.embaralhar()

    def embaralhar(self):
        random.shuffle(self._cartas)
    
    def tirar_carta(self) -> Carta:
        if not self._cartas:
            print("Baralho vazio, reembaralhando as cartas do descarte.")
            self._cartas = self._cartas_descarte
            self._cartas_descarte = []
            self.embaralhar()
        return self._cartas.pop(0)

    def devolver_carta(self, carta: Carta):
        self._cartas_descarte.append(carta)


def gerar_baralho(total_de_cartas: int) -> Baralho:
    cartas = []
        
        # Mapeando os strings para as classes de ação e valores aleatórios
    templates = [
            ("Sorte: Avance Y casas", AcaoMoverCasas, "Y", (1, 6), "Sorte"),
            ("Sorte: Receba X reais do banco", AcaoReceberDinheiro, "X", (50, 300), "Sorte"),
            ("Sorte: Receba X reais de cada jogador", AcaoPagarJogadores, "X", (20, 100), "Sorte"),
            ("Sorte: Saia da cadeia", AcaoSaiaDaCadeia, None, None, "Sorte"),
            ("Azar: Retorne Y casas", AcaoMoverCasas, "Y", (-6, -1), "Azar"),
            ("Azar: Pague X reais ao banco", AcaoPagarDinheiro, "X", (50, 300), "Azar"),
            ("Azar: Pague X reais a cada jogador", AcaoPagarJogadores, "X", (20, 100), "Azar"),
            ("Azar: Vá para a cadeia", AcaoIrParaCadeia, None, None, "Azar"),
        ]

    for _ in range(total_de_cartas):
        texto_base, acao_classe, parametro_str, valor_range, tipo_carta = random.choice(templates)
            
        # Cria a ação com ou sem valor aleatório
        if parametro_str:
            valor = random.randint(*valor_range)
            nome_carta = texto_base.replace(parametro_str, str(abs(valor)))
            acao = acao_classe(valor)

        else:
            nome_carta = texto_base
            acao = acao_classe()

        cartas.append(Carta(nome_carta, acao, tipo_carta))
        
    return Baralho(cartas)


#  TO DO As cartas de sorte e cofre tem as mesmas funcionalidades, então to achando que
# não há necessidade de classes separadas.

#class CartaSorte(Carta):
#   def __init__(self, nome: str, acao: Acao, tipo: str):
#       super().__init__(nome, acao,tipo)

#class CartaCofre(Carta):
#   def __init__(self, nome: str, acao: Acao, tipo: str):
#     super().__init__(nome, acao,tipo)


# Modifiquei a lógica um pouco
if __name__ == "__main__":
    baralho_sorte = gerar_baralho(10)
    jogador_teste = Jogador("Fernando")

    print("--- Simulação de turnos com cartas aleatórias ---")
    for i in range(5):
        print(f"\n--- Turno {i+1} ---")
        carta_puxada = baralho_sorte.tirar_carta()
        
        # A lógica para decidir qual PNG exibir está agora dentro da própria carta,
        # no método `executar_acao`.
        carta_puxada.executar_acao(jogador_teste)
        
        baralho_sorte.devolver_carta(carta_puxada)
