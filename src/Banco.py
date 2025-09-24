from __future__ import annotations
from typing import List, TYPE_CHECKING

# Usamos TYPE_CHECKING para evitar importações circulares com Jogador e Terreno
if TYPE_CHECKING:
    from .jogador import Jogador
    from .tabuleiro import Terreno

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

    def hipotecar_imovel(self, imovel: Terreno):
        """
        Empresta dinheiro ao jogador com base no valor de hipoteca do imóvel.
        """
        # Futuramente, adicionar verificação se o imóvel tem construções e fazer logica.
        pass

    def resgatar_hipoteca(self, imovel: Terreno):
        """
        Recebe o pagamento do jogador para liberar a hipoteca de um imóvel.
        A regra é o valor da hipoteca + 10% de juros.
        """
        pass

    def iniciar_leilao(self, imovel: Terreno, jogadores: List[Jogador]):
        """
        Inicia um leilão para uma propriedade não comprada. [cite: 1555]
        Delega a responsabilidade para o objeto Leilao.
        """
        self._leilao.realizar_leilao(imovel, jogadores)
