import os
from src.ui.character_card import CharacterCard
from src.ui.modal_interface import Modal
from pygame._sdl2.video import Texture
import pygame, sys


class SelectCharacterModal(Modal):
    def __init__(self, x, y, modal_surface, modal_image, renderer, clock):
        super().__init__(x, y, modal_surface, modal_image, renderer, clock)
        self.character_cards = {}
        self.create_character_cards()
    
    def create_character_cards(self):
        assets_dir = os.path.join("assets", "characters")

        characters = [
            ("hello-kitty", 300, 250),
            ("kuromi", 500, 250),
            ("cinnamoroll", 700, 250),
            ("my-melody", 300, 500),
            ("pompompurin", 500, 500),
            ("keroppi", 700, 500),
        ]

        for name, x, y in characters:
            normal_img = pygame.image.load(
                os.path.join(assets_dir, f"card-{name}.png")
            ).convert_alpha()

            hover_img = pygame.image.load(
                os.path.join(assets_dir, f"card-{name}-hover.png")
            ).convert_alpha()

            self.character_cards[name] = CharacterCard(
                x, y,
                normal_img,
                hover_img,
            )

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