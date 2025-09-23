from .Terreno import Terreno

class Companhia(Terreno):
    def __init__(self, nome: str, posicao: int, preco: int, hipoteca: int):
        super().__init__(nome, posicao, preco, "")
        self.hipoteca = hipoteca

    def calcularAluguel(self, val_dados: int = 0) -> int:
        # A lógica do aluguel foi simplificada para o teste
        return 0