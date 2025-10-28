import pygame
import sys
import os
from pygame._sdl2.video import Window, Renderer, Texture, Image

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from ui.button import Button


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

        # Load menu background
        self.menu_surface = pygame.image.load(os.path.join("assets", "bg-placeholder.jpeg"))
        self.menu_surface = pygame.transform.scale(self.menu_surface, (1280, 720))

        # Create a working surface for drawing buttons
        self.working_surface = self.menu_surface.copy()

        # Converting surface into texture
        self.menu_texture = Texture.from_surface(self.renderer, self.menu_surface)
        self.clock = pygame.time.Clock()

        # Load button images
        start_button_image = pygame.image.load(os.path.join("assets", "botao-jogar.png"))
        credits_button_image = pygame.image.load(os.path.join("assets", "botao-creditos.png"))
        exit_button_image = pygame.image.load(os.path.join("assets", "botao-sair.png"))

        # Load title
        self.title = pygame.image.load(os.path.join("assets", "titulo.png"))

        # Create buttons at specified position
        self.start_button = Button(524, 375, start_button_image, self.start_game)
        self.credits_button = Button(524, 465, credits_button_image, self.show_credits)
        self.exit_button = Button(524, 555, exit_button_image, self.exit_game)

    def start_game(self):
        print("game started")
    
    def show_credits(self):
        modal_surface = self.menu_surface.copy()
        modal_image = pygame.image.load(os.path.join("assets", "modal-creditos.png"))
        modal_rect = modal_image.get_rect(topleft=(240, 86))   

        back_button_image = pygame.image.load(os.path.join("assets", "botao-voltar-roxo.png"))  
        back_button = Button(807, 564, back_button_image)   

        showing = True
        while showing:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if back_button.handle_event(event):
                    showing = False 
            
            back_button.update_hover(mouse_pos)

            modal_surface = self.menu_surface.copy()
            back_button.draw_to_surface(modal_surface)
            modal_surface.blit(modal_image, modal_rect)
            
            modal_texture = Texture.from_surface(self.renderer, modal_surface)
            self.renderer.clear()
            self.renderer.blit(modal_texture)
            self.renderer.present()

            self.clock.tick(60)
    
    def exit_game(self):
        print("saindo do jogo")

    def run(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Handle button events
                self.start_button.handle_event(event)
                self.credits_button.handle_event(event)
                self.exit_button.handle_event(event)

                if event.type == pygame.KEYDOWN:
                    pass

            # Update button hover states
            self.start_button.update_hover(mouse_pos)
            self.credits_button.update_hover(mouse_pos)
            self.exit_button.update_hover(mouse_pos)

            # Prepare the surface with menu background
            menu_surface = self.menu_surface.copy()

            title_rect = self.title.get_rect(center=(1280 // 2, 200))
            menu_surface.blit(self.title, title_rect)

            # Draw buttons on the surface
            self.start_button.draw_to_surface(menu_surface)
            self.credits_button.draw_to_surface(menu_surface)
            self.exit_button.draw_to_surface(menu_surface)

            # Convert surface to texture and render
            self.menu_texture = Texture.from_surface(self.renderer, menu_surface)

            self.renderer.clear()
            self.renderer.blit(self.menu_texture)
            self.renderer.present()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Menu()
    game.run()
