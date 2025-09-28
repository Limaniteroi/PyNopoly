import pygame

class Button:
    def __init__(self, x, y, image, callback=None):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.callback = callback
        self.is_hovered = False

    def handle_event(self, event):
        """Handle mouse click events"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback()
                return True
        return False

    def update_hover(self, mouse_pos):
        """Update hover state for visual feedback"""
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def draw_to_surface(self, surface):
        """Draw button to a pygame surface"""
        surface.blit(self.image, self.rect)
        if self.is_hovered:
            # Simple hover effect: darken the button slightly
            darken_surface = pygame.Surface(self.rect.size, flags=pygame.SRCALPHA)
            darken_surface.fill((0, 0, 0, 50))  # Black with 50 alpha
            surface.blit(darken_surface, self.rect.topleft)