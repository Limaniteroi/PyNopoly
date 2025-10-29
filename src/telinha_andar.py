import pygame
from pygame import *
from .Jogador import Jogador
import random

pygame.init()

height = 720
width = 1280

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PyNopoly")

# Baixando o fundo do tabuleiro e os ícones dos jogadores
background = pygame.image.load("arts/tabuleiro.png").convert_alpha()
icon_jogadores = {
    0: pygame.image.load("arts/active_blue.png").convert_alpha(),
    1: pygame.image.load("arts/active_green.png").convert_alpha(),
    2: pygame.image.load("arts/active_pink.png").convert_alpha(),
    3: pygame.image.load("arts/active_purple.png").convert_alpha()
}

clock = pygame.time.Clock()
running = True

# Criando jogadores
pecas = {0: "azul", 1: "verde", 2: "rosa", 3: "roxo"}
jogadores = [Jogador(pecas[i]) for i in range(len(pecas))]

# Mapeando posições das casas do tabuleiro para coordenadas x,y na tela 
# Expandido para 40 casas (tabuleiro completo do Monopoly)
casas_x_y = {
    0: (350, 310), 1: (390, 350), 2: (420, 380), 3: (445, 405), 
    4: (465, 430), 5: (490, 450), 6: (520, 480), 7: (540, 500), 
    8: (560, 520), 9: (590, 550), 10: (630, 590),
}

NUM_CASAS = len(casas_x_y)

# Controle de turno
current_player = 0

# Controle de animação
class AnimacaoMovimento:
    def __init__(self):
        self.ativa = False
        self.jogador_idx = None
        self.passos_restantes = []  # Lista de índices de casas a animar
        self.pos_inicio = (0, 0)
        self.pos_fim = (0, 0)
        self.tempo_inicio = 0
        self.casa_destino_atual = 0
        self.duracao_passo = 180  # ms por casa
    
    def iniciar(self, jogador_idx, jogador, valor_dados):
        """Inicia a animação de movimento para um jogador"""
        self.jogador_idx = jogador_idx
        self.passos_restantes = []
        
        # Calcula todas as casas intermediárias do movimento
        posicao_inicial = jogador.posicao
        for i in range(1, valor_dados + 1):
            proxima_casa = (posicao_inicial + i) % NUM_CASAS
            self.passos_restantes.append(proxima_casa)
        
        print(f"Animação iniciada: Jogador {jogador_idx} vai da casa {posicao_inicial} para {self.passos_restantes[-1]}")
    
    def proximo_passo(self, jogador):
        """Inicia a animação do próximo passo"""
        if not self.passos_restantes:
            return False
        
        self.casa_destino_atual = self.passos_restantes.pop(0)
        casa_origem = jogador.posicao
        
        self.pos_inicio = casas_x_y.get(casa_origem, casas_x_y[0])
        self.pos_fim = casas_x_y.get(self.casa_destino_atual, casas_x_y[0])
        self.tempo_inicio = pygame.time.get_ticks()
        self.ativa = True
        
        return True
    
    def atualizar(self, jogador):
        """Atualiza a animação atual e retorna a posição interpolada"""
        if not self.ativa:
            return None
        
        tempo_decorrido = pygame.time.get_ticks() - self.tempo_inicio
        t = min(1.0, tempo_decorrido / self.duracao_passo)
        
        # Interpolação linear
        x = self.pos_inicio[0] + (self.pos_fim[0] - self.pos_inicio[0]) * t
        y = self.pos_inicio[1] + (self.pos_fim[1] - self.pos_inicio[1]) * t
        
        # Se completou o passo
        if t >= 1.0:
            jogador.posicao = self.casa_destino_atual
            self.ativa = False
            print(f"Jogador {self.jogador_idx} chegou na casa {self.casa_destino_atual}")
            return None
        
        return (int(x), int(y))
    
    def tem_passos_pendentes(self):
        """Verifica se ainda há passos para animar"""
        return len(self.passos_restantes) > 0
    
    def finalizar(self):
        """Finaliza a animação"""
        self.ativa = False
        self.jogador_idx = None
        self.passos_restantes = []

animacao = AnimacaoMovimento()

def get_draw_pos(jogador_idx: int, pos_interpolada=None):
    """
    Calcula a posição de desenho do jogador na tela.
    Se pos_interpolada for fornecida, usa ela; caso contrário, usa a posição atual do jogador.
    """
    jogador = jogadores[jogador_idx]
    
    if pos_interpolada:
        base = pos_interpolada
    else:
        base = casas_x_y.get(jogador.posicao, casas_x_y[0])
    
    # Offset para que múltiplos jogadores não fiquem sobrepostos
    offset = (jogador_idx * 18, 0)
    return (base[0] + offset[0], base[1] + offset[1])

# Loop principal
while running:
    dt = clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                # Só permite rolar dados se não há animação em andamento
                if not animacao.ativa and not animacao.tem_passos_pendentes():
                    jogador_atual = jogadores[current_player]
                    
                    # Usa o método da classe Jogador para lançar os dados
                    dados = jogador_atual.lancar_dados()
                    valor_total = sum(dados)
                    
                    print(f"\n=== Turno do Jogador {current_player} ({jogador_atual.peca}) ===")
                    print(f"Dados: {dados} = {valor_total}")
                    print(f"Posição inicial: {jogador_atual.posicao}")
                    
                    # Inicia a animação de movimento
                    animacao.iniciar(current_player, jogador_atual, valor_total)
    
    # Gerencia a animação
    if not animacao.ativa and animacao.tem_passos_pendentes():
        # Inicia o próximo passo da animação
        animacao.proximo_passo(jogadores[animacao.jogador_idx])
    
    # Se não há mais passos e a animação terminou, avança o turno
    if not animacao.ativa and not animacao.tem_passos_pendentes() and animacao.jogador_idx is not None:
        jogador_atual = jogadores[current_player]
        print(f"Posição final: {jogador_atual.posicao}")
        print(f"Casa: {casas_x_y.get(jogador_atual.posicao, 'desconhecida')}")
        
        # Aqui você pode adicionar lógica para processar a casa onde o jogador parou
        # Por exemplo: verificar se é propriedade, pagar aluguel, etc.
        
        # Avança o turno
        current_player = (current_player + 1) % len(jogadores)
        animacao.finalizar()
        print(f"\n>>> Próximo turno: Jogador {current_player} ({jogadores[current_player].peca})")
    
    # Atualiza a posição interpolada se há animação ativa
    pos_interpolada = None
    if animacao.ativa:
        pos_interpolada = animacao.atualizar(jogadores[animacao.jogador_idx])
    
    # Renderização
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    # Desenha todos os jogadores
    for i, jogador in enumerate(jogadores):
        if animacao.ativa and i == animacao.jogador_idx:
            # Jogador em movimento: usa posição interpolada
            draw_pos = get_draw_pos(i, pos_interpolada)
        else:
            # Jogador parado: usa posição atual
            draw_pos = get_draw_pos(i)
        
        screen.blit(icon_jogadores[i], draw_pos)
    
    # Desenha informações do turno (opcional)
    font = pygame.font.Font(None, 36)
    turno_text = font.render(f"Turno: {jogadores[current_player].peca}", True, (255, 255, 255))
    screen.blit(turno_text, (10, 10))
    
    pygame.display.flip()

pygame.quit()