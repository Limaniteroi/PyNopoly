from src.ui.modal_interface import Modal
from pygame._sdl2.video import Texture
import pygame, sys


class SelectCharacterModal(Modal):
    def __init__(self, x, y, modal_surface, modal_image, renderer, clock):
        super().__init__(x, y, modal_surface, modal_image, renderer, clock)

    def show(self):
        showing = True
        while showing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                        showing = False

            self.modal_surface.blit(self.modal_image, self.modal_rect)
            
            modal_texture = Texture.from_surface(self.renderer, self.modal_surface)
            self.renderer.clear()
            self.renderer.blit(modal_texture)
            self.renderer.present()

            self.clock.tick(60)