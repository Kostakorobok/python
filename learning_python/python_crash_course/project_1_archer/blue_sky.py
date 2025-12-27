import pygame
import sys

from game_characters import Archer

WIDTH, HEIGHT = 800, 600
bg_color = (169, 235, 155)

class Screen:
    pygame.init()
    def __init__(self):

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.bg_color = self.screen.fill(bg_color)

        self.archer = Archer(self)

    def run_app(self):
        while True:
            self._update_screen()
            self._check_events()

    def _update_screen(self):
        pygame.display.flip()
        self.archer.blitme()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    screen1 = Screen()
    screen1.run_app()