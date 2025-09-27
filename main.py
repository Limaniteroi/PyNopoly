import pygame
import sys
import os
from pygame._sdl2.video import Window, Renderer, Texture


class Menu:
    def __init__(self):
        pygame.init()

        try:
            self.window = Window("PyNopoly", size=(1280, 720))
            self.renderer = Renderer(self.window)
        except Exception as e:
            print(f"Error creating window or renderer: {e}")
            pygame.quit()
            exit()

        #Load arts
        menu_surface = pygame.image.load(os.path.join('arts', 'menu_placeholder.jpeg'))
        #Converting intto textures
        self.menu_texture = Texture.from_surface(self.renderer, menu_surface)
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pass

            self.renderer.clear()
            self.renderer.blit(self.menu_texture)
            self.renderer.present()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Menu()
    game.run()
