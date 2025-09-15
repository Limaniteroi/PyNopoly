# Arquivo: main.py

from src.Fabricas import TabuleiroPadraoFactory
from src.Jogador import Jogador
from src.Partida import Partida
from src.Tabuleiro import Imovel, Estacao, PontoDePartida

def main():
    """
    Função principal para testar a inicialização e a interação
    entre as classes do projeto PyNopoly.
    """
    print("--- INICIANDO TESTE GERAL DO PYNOPOLY ---")

    # --- 1. Testando a Fábrica e o Tabuleiro ---
    print("\n[TESTE 1: Fábrica e Tabuleiro]")
    try:
        # Instancia a fábrica concreta para o tabuleiro padrão
        fabrica = TabuleiroPadraoFactory()
        print(" -> TabuleiroPadraoFactory criada com sucesso.")

        # Usa a fábrica para criar uma instância do tabuleiro
        # (Nota: o método na sua fábrica está como 'criar_tabuleiro' estático, vamos chamá-lo assim)
        tabuleiro = fabrica.criar_tabuleiro()
        print(f" -> Tabuleiro criado com {len(tabuleiro.casas)} casas.")

        # Verifica se algumas casas foram criadas corretamente
        casa_0 = tabuleiro.get_casa_na_posicao(0)
        casa_1 = tabuleiro.get_casa_na_posicao(1)
        casa_5 = tabuleiro.get_casa_na_posicao(5)

        print(f" -> Casa na posição 0: '{casa_0.nome}' (Tipo: {type(casa_0).__name__})")
        print(f" -> Casa na posição 1: '{casa_1.nome}' (Tipo: {type(casa_1).__name__})")
        print(f" -> Casa na posição 5: '{casa_5.nome}' (Tipo: {type(casa_5).__name__})")

        assert isinstance(casa_0, PontoDePartida)
        assert isinstance(casa_1, Imovel)
        assert isinstance(casa_5, Estacao)
        print(" -> Verificação de tipos de casas passou com sucesso!")

    except Exception as e:
        print(f"ERRO no Teste 1: {e}")


    # --- 2. Testando a Classe Jogador ---
    print("\n[TESTE 2: Jogador]")
    try:
        # Instancia um jogador
        jogador1 = Jogador("Herói")
        print(f" -> Jogador '{jogador1.peca}' criado com sucesso.")
        print(f"    - Dinheiro inicial: ${jogador1.dinheiro}")
        print(f"    - Posição inicial: {jogador1.posicao}")
        
    except Exception as e:
        print(f"ERRO no Teste 2: {e}")


    # --- 3. Testando a Classe Partida (Controller) ---
    print("\n[TESTE 3: Partida]")
    try:
        
        # (O __init__ da sua Partida atual só recebe a lista de nomes)

        pecas_jogadores = ["Vara", "Kuromi"]
        partida = Partida(pecas_jogadores, fabrica)
        print(f" -> Partida criada com sucesso para os jogadores: {pecas_jogadores}.")
        
        print(f" -> {len(partida.jogadores)} objetos Jogador criados na partida.")

    except Exception as e:
        print(f"ERRO no Teste 3: {e}")

    print("\n--- TESTE CONCLUÍDO ---")


if __name__ == "__main__":
    main()