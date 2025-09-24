from __future__ import annotations
from typing import List, TYPE_CHECKING
from Leilao import Leilao

# Usamos TYPE_CHECKING para evitar importações circulares com Jogador e Terreno
if TYPE_CHECKING:
    from .Jogador import Jogador
    from .Terreno import Terreno

class Banco:
    def __init__(self):
        # Podemos mudar o numero aqui depois, mas tem algo de casas disponiveis no .pdf das regras.
        self._casas_disponiveis: int = 32
        self._hoteis_disponiveis: int = 12
        self._leilao = Leilao()

    @property
    def get_casas_disponiveis(self) -> int:
        return self._casas_disponiveis

    @property
    def get_hoteis_disponiveis(self) -> int:
        return self._hoteis_disponiveis

    def pagar_salario(self, jogador: Jogador):
        """Paga o salário de $200 ao jogador por passar pelo Ponto de Partida."""
        print(f"Banco pagou $200 de salário para {jogador.nome}.")
        jogador.receber_dinheiro(200)

    def hipotecar_imovel(self, imovel: Terreno, jogador: Jogador):
        """
        Empresta dinheiro ao jogador com base no valor de hipoteca do imóvel.
        """
        jogador.receber_dinheiro(imovel.preco)
        imovel.set_hipotecado(True)
        # To-do: adicionar verificação se o imóvel tem construções e recalcular o preço da hipoteca se tiver

    def resgatar_hipoteca(self, imovel: Terreno, jogador: Jogador):
        """
        Recebe o pagamento do jogador para liberar a hipoteca de um imóvel, ou seja, 
        depois disso o imóvel não está mais hipotecado.
        A regra é o valor da hipoteca + 10% de juros.
        """
        jogador.enviar_dinheiro(imovel.preco * 1.1)
        imovel.set_hipotecado(False)

    def iniciar_leilao(self, imovel: Terreno, jogadores: List[Jogador]):
        """
        Inicia um leilão para uma propriedade não comprada. [cite: 1555]
        Delega a responsabilidade para o objeto Leilao.
        """
        self._leilao.realizar_leilao(imovel, jogadores)
