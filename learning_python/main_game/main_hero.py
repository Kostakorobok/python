import pygame

class Hero:
    def __init__ (self, x, y, character_class = "wizard"):
        self.image = pygame.image.load("wizard_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (220,150))
        self.x = x
        self.y = y
        self.speed = 5

        if character_class == "wizard":
            self.image = pygame.image.load("wizard_1.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (220,150))
        elif character_class == "warrior":
            self.image = pygame.image.load("warrior_1.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (220,150))
        else:
            raise ValueError("Invalid character_class")

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))