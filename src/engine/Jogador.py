from __future__ import annotations
from typing import List, TYPE_CHECKING
from abc import ABC, abstractmethod
from .Imovel import Imovel
import random

if TYPE_CHECKING:
    from .Tabuleiro.Terreno import Terreno
    from .Tabuleiro.Tabuleiro import Tabuleiro


class JogadorState(ABC):
    @abstractmethod
    def executar_acao_do_turno(self, jogador: Jogador):
        pass


class JogadorJogandoState(JogadorState):
    def executar_acao_do_turno(self, jogador: Jogador):
        print(f"Estado de {jogador.peca}: Jogando Normalmente. Rolando dados...")
        return jogador.lancar_dados() # Retorna os dados para usar pelo pygame


class JogadorPresoState(JogadorState):
    def __init__(self):
        self.turnos_preso = 0

    def executar_acao_do_turno(self, jogador: Jogador):
        print(f"Estado de {jogador.peca}: Preso. Tentando sair da cadeia...")
        self.turnos_preso += 1
        dados = jogador.lancar_dados()
        if dados[0] == dados[1]:
            print(f"{jogador.peca} tirou dados iguais e saiu da prisão!")
            jogador.mudar_estado(JogadorJogandoState())
            return dados
        elif self.turnos_preso >= 3:
            print(f"{jogador.peca} pagou para sair da prisão.")
            jogador.enviar_dinheiro(50)
            jogador.mudar_estado(JogadorJogandoState())
            return dados
        else:
            print(f"{jogador.peca} não saiu da prisão.")
            return None


class JogadorFalidoState(JogadorState):
    def executar_acao_do_turno(self, jogador: Jogador):
        print(
            f"Estado de {jogador.peca}: Falido. Tal metodo não deveria ter sido chamado, erro de lógica."
        )


class Jogador:
    def __init__(self, peca: str, nome: str):
        self.peca = peca
        self.nome = nome
        self.dinheiro: int = 1500
        self._posicao: int = 0
        self.lance_leilao: int = 0

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
        return self.estado_atual.executar_acao_do_turno(self)

    def mover(self, passos: int):
        # O operador % 40 garante que o tabuleiro seja circular (posições 0 a 39)
        self.posicao = (self.posicao + passos) % 40
        print(f"{self.peca} moveu-se {passos} casas e está na posição {self.posicao}.")

    def comprar_imovel(self, imovel: Terreno):
        """Tenta comprar um imóvel. O jogador deve ter dinheiro suficiente."""
        if self.dinheiro >= imovel.preco:
            self.dinheiro -= imovel.preco
            self.propriedades.append(imovel)
            imovel.set_dono(self)
            print(f"{self.peca} comprou {imovel.nome} por ${imovel.preco}.")
        else:
            print(f"{self.peca} não tem dinheiro para comprar {imovel.nome}.")

    def pagar_aluguel(self, dono: Jogador, valor: int):
        """Paga um valor de aluguel para outro jogador."""
        if self.dinheiro >= valor:
            self.dinheiro -= valor
            dono.receber_dinheiro(valor)
            print(f"{self.peca} pagou ${valor} de aluguel para {dono.peca}.")
        else:
            print(f"{self.peca} não tem dinheiro para pagar o aluguel e faliu!")
            self.mudar_estado(JogadorFalidoState())
            # Lógica de falência viria aqui tirar imoveis? apagar peca?

    def receber_dinheiro(self, valor: int):
        self.dinheiro += valor
    
    def enviar_dinheiro(self, valor: int):
        self.dinheiro -= valor

    def construir_casa(self, imovel: Imovel, tabuleiro: Tabuleiro):
        """Constrói uma casa em um imóvel, seguindo as regras do Monopoly."""
        print(f"{self.peca} tentando construir casa em {imovel.nome}...")

        # 1. Verificar se o jogador tem o monopólio da cor do imóvel.
        if not self.tem_monopolio(imovel.cor, tabuleiro):
            print(f"{self.peca} não tem o monopólio da cor {imovel.cor}.")
            return

        # Get all properties of the color the player owns
        propriedades_da_cor = [p for p in self.propriedades if isinstance(p, Imovel) and p.cor == imovel.cor]
        
        # If the player doesn't own any property of this color (should not happen if called correctly)
        if not propriedades_da_cor:
            print(f"{self.peca} não possui nenhuma propriedade do grupo {imovel.cor}.")
            return

        # 2. Verificar a regra de construção uniforme (entre as propriedades que possui)
        min_casas_no_grupo = min(p.casas for p in propriedades_da_cor)
        if imovel.casas > min_casas_no_grupo:
            print(f"Construção não é uniforme. Construa primeiro em outras propriedades do grupo {imovel.cor} que você possui.")
            return
            
        if imovel.casas >= 5:
            print(f"{imovel.nome} já tem um hotel. Não é possível construir mais.")
            return

        # 3. Verificar se o jogador tem dinheiro.
        custo = imovel.preco_casa
        if self.dinheiro < custo:
            print(f"{self.peca} não tem dinheiro suficiente para construir uma casa por ${custo}.")
            return

        # 4. Debitar o valor e incrementar o número de casas no imóvel.
        self.dinheiro -= custo
        imovel.casas += 1
        
        if imovel.casas == 5:
            print(f"{self.peca} construiu um hotel em {imovel.nome} por ${custo}.")
        else:
            print(f"{self.peca} construiu uma casa em {imovel.nome} por ${custo}. Total de casas: {imovel.casas}.")

    def tem_monopolio(self, cor: str, tabuleiro: Tabuleiro) -> bool:
        propriedades_da_cor = [p for p in self.propriedades if isinstance(p, Imovel) and p.cor == cor]
        return len(propriedades_da_cor) == tabuleiro.get_propriedades_da_cor(cor)

    def calcular_valor_total(self) -> int:
        valor_total = self.dinheiro
        for propriedade in self.propriedades:
            valor_total += propriedade.preco
            if isinstance(propriedade, Imovel):
                # Custo de construção de cada casa (suposição)
                custo_casa = 100
                valor_total += propriedade.casas * custo_casa
        return valor_total

    def calcular_imposto(self) -> int:
        """Calcula o imposto a ser pago, que é o menor valor entre $200 e 10% do valor total do jogador."""
        valor_total = self.calcular_valor_total()
        imposto_percentual = int(valor_total * 0.10)
        return min(200, imposto_percentual)

    def mudar_estado(self, novo_estado: JogadorState):
        """Altera o objeto de estado do jogador."""
        self.estado_atual = novo_estado

    #Talvez vá para classe dado????
    def lancar_dados(self):
        dados = []
        for _ in range(2):
            dados.append(random.randint(1, 6))
        print(f"Jogador {self.peca}: tirou {dados} nos dados.")
        return dados
    
    def set_lance_leilao(self, valor: int):
        self.lance_leilao = valor
    
    def comprar_imovel_leilao(self, imovel: Terreno, valor: int):
        if self.dinheiro >= valor:
            self.dinheiro -= valor
            self.propriedades.append(imovel)
            imovel.set_dono(self)
            print(f"{self.peca} comprou {imovel.nome} por ${valor}.")
        else:
            print(f"{self.peca} não tem dinheiro para comprar {imovel.nome}.")

    @property
    def posicao(self):
        return self._posicao

    @posicao.setter
    def posicao(self, value):
        self._posicao = value
