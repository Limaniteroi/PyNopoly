from __future__ import annotations
import random
from typing import List

class Dados:
    def __init__(self):
        self.dados: List[int] = []

    def lancar(self) -> List[int]:
        """
        Lança dois dados de 6 lados e retorna uma lista com os resultados.
        """
        self.dados = [random.randint(1, 6), random.randint(1, 6)]
        print(f"Dados lançados: {self.dados}")
        return self.dados
