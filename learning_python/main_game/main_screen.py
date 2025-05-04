import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character Select")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)

# Fonts
font = pygame.font.SysFont("arial", 36)

# Button rects
wizard_button = pygame.Rect(200, 250, 150, 80)
warrior_button = pygame.Rect(450, 250, 150, 80)

# Game state
selected_character = None

running = True
while running:
    screen.fill(GREY)

    # Draw title
    title_text = font.render("Choose Your Character", True, BLACK)
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 100))

    # Draw buttons
    pygame.draw.rect(screen, WHITE, wizard_button)
    pygame.draw.rect(screen, WHITE, warrior_button)

    wizard_text = font.render("Wizard", True, BLACK)
    warrior_text = font.render("Warrior", True, BLACK)
    screen.blit(wizard_text, (wizard_button.x + 20, wizard_button.y + 20))
    screen.blit(warrior_text, (warrior_button.x + 20, warrior_button.y + 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if wizard_button.collidepoint(mouse_pos):
                selected_character = "wizard"
                running = False  # Proceed to game
            elif warrior_button.collidepoint(mouse_pos):
                selected_character = "warrior"
                running = False  # Proceed to game

    pygame.display.flip()

# After this script ends, pass selected_character to main_game.py
