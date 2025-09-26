from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .Jogador import Jogador
    from .Tabuleiro.Terreno import Terreno

class Leilao:

    def realizar_leilao(self, imovel: Terreno, jogadores: List[Jogador]) -> None:
        lance_minimo: int = 0.2 * imovel.preco
        maior_lance: int = 0

        print(f"\n--- LEILÃO INICIADO PARA: {imovel.nome} ---")
        
        while (len(jogadores) > 1):
            for i in range(len(jogadores)):
                print(f"Jogando: {jogadores[i].peca}")
                opt = int(input("\t1. Dar lance\n\t2.Desistir"))
                if (opt == 1):
                    jogadores[i].set_lance_leilao(int(input("Valor: ")))
                    if (jogadores[i].lance_leilao >= lance_minimo and 
                        jogadores[i].lance_leilao > maior_lance):
                        maior_lance = jogadores[i].lance_leilao
                else:
                    jogadores.pop(i)

        print(f"Leilão concluído. O vencedor foi: {jogadores[0]}")
        jogadores[0].comprar_imovel_leilao(imovel, maior_lance)