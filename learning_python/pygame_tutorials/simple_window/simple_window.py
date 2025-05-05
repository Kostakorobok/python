import pygame
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400

    def on_init:
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, py)