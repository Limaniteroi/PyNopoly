import pygame
import sys
from pygame._sdl2.video import Window, Renderer, Texture


class Game:
    def __init__(self):
        pygame.init()

        try:
            self.window = Window("PyNopoly", size=(1280, 720))
            self.renderer = Renderer(self.window)
        except Exception as e:
            print(f"Error creating window or renderer: {e}")
            pygame.quit()
            exit()

        self.window.title = "PyNopoly"
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pass

            self.renderer.draw_color = (10, 20, 40, 255)
            self.renderer.clear()
            self.renderer.present()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
