import pygame

class Archer:
    def __init__(self, archer):
        self.screen = archer.screen
        self.screen_rect = archer.screen.get_rect()

        self.image = pygame.image.load('images/archer.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)