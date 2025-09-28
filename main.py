import pygame
import sys
import os
from pygame._sdl2.video import Window, Renderer, Texture

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

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

        # Load arts
        menu_surface = pygame.image.load(os.path.join('arts', 'menu_placeholder.jpeg'))
        
        # Create a working surface for drawing buttons
        self.working_surface = menu_surface.copy()
        
        # Converting into textures
        self.menu_texture = Texture.from_surface(self.renderer, menu_surface)
        self.clock = pygame.time.Clock()
        
        # Create start button image
        button_image = pygame.image.load(os.path.join('arts', 'button_placeholder.jpg'))
        button_image = pygame.transform.scale(button_image, (120, 40))

        # Create start button at specified position
        self.start_button = Button(135, 416, button_image, self.start_game)
    
    def start_game(self):
        """Callback function for the start button"""
        print("game started")
    
    def run(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Handle button events
                self.start_button.handle_event(event)
                
                if event.type == pygame.KEYDOWN:
                    pass
            
            # Update button hover state
            self.start_button.update_hover(mouse_pos)
            
            # Prepare the surface with menu background
            menu_surface = pygame.image.load(os.path.join('arts', 'menu_placeholder.jpeg'))
            
            # Draw button on the surface
            self.start_button.draw_to_surface(menu_surface)
            
            # Convert surface to texture and render
            self.menu_texture = Texture.from_surface(self.renderer, menu_surface)
            
            self.renderer.clear()
            self.renderer.blit(self.menu_texture)
            self.renderer.present()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Menu()
    game.run()
