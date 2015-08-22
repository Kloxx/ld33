import pygame
from main import size
from pygame.surface import Surface

class DialogInterface:
    def __init__(self, name, size, ):
        self.name = name
        self.size = size

    def draw_portraits(self, Surface):
        self.fond = pygame.image.load("Portraits/bg_dialog.png")
        self.portrait1 = pygame.image.load("Portraits/hero.png")
        self.portrait2 = pygame.image.load("Portraits/encounter1.png")
#        Surface.blit(self.portrait1, (size*2/3, 0))
#    def load_dialog(self):
        