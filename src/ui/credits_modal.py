import os
from src.ui.button import Button
from src.ui.modal_interface import Modal
from pygame._sdl2.video import Texture
import pygame, sys

class CreditsModal(Modal):
    def __init__(self, x, y, modal_surface, modal_image, renderer, clock):
        super().__init__(x, y, modal_surface, modal_image, renderer, clock)
        back_button_image = pygame.image.load(os.path.join("assets", "botao-voltar-roxo.png"))  
        self.back_button = Button(807, 564, back_button_image) 
    
    def show(self):
        showing = True
        while showing:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.back_button.handle_event(event):
                    showing = False 
            
            self.back_button.update_hover(mouse_pos)

            frame_surface = self.modal_surface.copy()
            frame_surface.blit(self.modal_image, self.modal_rect)
            self.back_button.draw_to_surface(self.modal_surface)
            
            modal_texture = Texture.from_surface(self.renderer, frame_surface)
            self.renderer.clear()
            self.renderer.blit(modal_texture)
            self.renderer.present()

            self.clock.tick(60)