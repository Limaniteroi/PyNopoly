import pygame

class Modal:
    def __init__(self, x,y, modal_surface, modal_image, renderer, clock):
        self.modal_surface = modal_surface
        self.modal_image = modal_image
        self.modal_rect = modal_image.get_rect(topleft=(x, y))  
        self.renderer = renderer
        self.clock = clock
    
    def show(self):
        raise NotImplementedError("Subclasses devem implementar o método show()")