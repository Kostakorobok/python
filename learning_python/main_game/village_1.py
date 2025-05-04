
# creating a village for my project game

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen  = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Village")

GREEN = (34, 139, 34)

village_house_1 = pygame.image.load('village_house_1.png').convert_alpha()
# village_house_1 = pygame.transform.scale(village_house_1, (48, 48))

def draw_village_1(screen):
    screen.fill(GREEN)
    screen.blit(village_house_1, (100, 100))