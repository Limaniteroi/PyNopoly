import pygame

class CharacterCard:
    def __init__(self, x, y, image, hover_image, callback=None):
        self.image = image
        self.hover_image = hover_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.callback = callback
        self.is_hovered = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback()
                return True
        return False

    def update_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def draw_to_surface(self, surface):
        surface.blit(self.image, self.rect)
        if self.is_hovered:
            surface.blit(self.hover_image, self.rect)