from __future__ import annotations
from abc import ABC
import json
import random
from typing import List, TYPE_CHECKING
from .CasaTabuleiro import CasaTabuleiro
from .Tabuleiro import Tabuleiro
from .PontoDePartida import PontoDePartida
from .Cadeia import Cadeia
from .Imovel import Imovel
from .CasaSorte import CasaSorte
from .CasaCofre import CasaCofre
from .Estacao import Estacao
from .Companhia import Companhia
from .EstacionamentoLivre import EstacionamentoLivre
from .VaParaCadeia import VaParaCadeia


if TYPE_CHECKING:
    from .Jogador import Jogador

        
def selecionar_itens_aleatorios(caminho_arquivo: str, quantidade: int):
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            casas_json = json.load(f)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não é um JSON válido.")
        return []

    item = [item for item in casas_json]

    if len(item) < quantidade:
        print(f"Aviso: O arquivo tem apenas {len(item)} imóveis, mas você pediu {quantidade}.")
        return item
    
    itens_selecionados = random.sample(item, quantidade)
    
    return itens_selecionados


class TabuleiroAleatorioFactory(ABC):
    def criar_tabuleiro(self) -> Tabuleiro:

        casas_fixas = {
            0: PontoDePartida("Ponto de Partida", 0),
            10: Cadeia("Cadeia (Apenas Visitando)", 10),
            20: EstacionamentoLivre("Estacionamento Livre", 20),
            30: VaParaCadeia("Vá para a Cadeia", 30)
        }

        # Define a quantidades de casas variáveis
        quantidade_casas_moveis = 22
        quantidade_estacoes = 4
        quantidade_companhias = 2 
        quantidade_casas_sorte_cofre = 3  # São 3 de cada tipo

        # Seleciona itens aleatórios de arquivos JSON
        path_imoveis_aleatorios = 'CasasAleatoriasImoveis.json'
        path_estacoes_aleatorias = 'CasasAleatoriasEstacoes.json'
        path_companhias_aleatorias = 'CasasAleatoriasCompanhias.json'

        imoveis_selecionados = selecionar_itens_aleatorios(path_imoveis_aleatorios, quantidade_casas_moveis)
        estacoes_selecionadas = selecionar_itens_aleatorios(path_estacoes_aleatorias, quantidade_estacoes)
        companhias_selecionadas = selecionar_itens_aleatorios(path_companhias_aleatorias, quantidade_companhias)
        

        todas_casas_moveis_selecionadas = []
    
        for item in imoveis_selecionados:
            todas_casas_moveis_selecionadas.append(Imovel(
                nome=item['nome'],
                posicao=item['posicao'], 
                preco=item['preco'],
                hipoteca=item['hipoteca'],
                cor=item['cor'],
                alugueis=item['alugueis'],
                preco_casa=item['preco_casa']
            ))
        
        for item in estacoes_selecionadas:
            todas_casas_moveis_selecionadas.append(Estacao(
                nome=item['nome'],
                posicao=item['posicao'],
                preco=item['preco'],
                hipoteca=item['hipoteca']
            ))
            
        for item in companhias_selecionadas:
            todas_casas_moveis_selecionadas.append(Companhia(
                nome=item['nome'],
                posicao=item['posicao'],
                preco=item['preco'],
                hipoteca=item['hipoteca']
            ))

        for i in range(quantidade_casas_sorte_cofre):
            todas_casas_moveis_selecionadas.append(CasaSorte(f"Sorte {i+1}", None))
            todas_casas_moveis_selecionadas.append(CasaCofre(f"Cofre {i+1}", None))

        # Cria uma lista de todas as posições do tabuleiro (40 casas)
        casas_tabuleiro: List[CasaTabuleiro] = [None] * 40
        
        # Adiciona as casas fixas nas posições corretas
        for pos, casa in casas_fixas.items():
            casas_tabuleiro[pos] = casa

        # Obtém as posições vazias e as embaralha
        posicoes_disponiveis = [i for i in range(40) if casas_tabuleiro[i] is None]
        random.shuffle(posicoes_disponiveis)

        # Atribui uma posição aleatória para cada casa móvel selecionada
        for i, casa_movel in enumerate(todas_casas_moveis_selecionadas):
            posicao_aleatoria = posicoes_disponiveis[i]
            casa_movel.posicao = posicao_aleatoria
            casas_tabuleiro[posicao_aleatoria] = casa_movel


        # Retorna o tabuleiro completo
        return Tabuleiro(casas=casas_tabuleiro)




