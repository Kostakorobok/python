import pygame
import sys
import main_screen
from village_1 import draw_village_1
from main_hero import Hero

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Main Game')

clock = pygame.time.Clock()

selected = main_screen.selected_character

if selected == "wizard":
    hero = Hero(100, 100, "wizard")
elif selected == "warrior":
    hero = Hero(100, 100, "warrior")

game_on = True
while game_on:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    keys = pygame.key.get_pressed()
    hero.move(keys)

    draw_village_1(screen)
    hero.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()


