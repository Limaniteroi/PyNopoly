import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import src.Tabuleiro

class Jogador:
    def __init__(self):
        self.dinheiro: int = 0
        self.peca: str = ""
        self.pos: int = 0
        self.nome: str = "Test"

src.Tabuleiro.Jogador = Jogador

from src.Fabricas import TabuleiroPadraoFactoryFactory

def main():
    # Cria um tabuleiro padrão usando a fábrica
    tabuleiro = TabuleiroPadraoFactory.criar_tabuleiro()

    # Imprime todas as casas do tabuleiro em ordem
    print("Casas do Tabuleiro:")
    for casa in tabuleiro.casas:
        print(f"Posição {casa.pos}: {casa.nome}")

if __name__ == "__main__":
    main()
