import pygame
import random
class Stone(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/objetos/stone.png")
        self.image = pygame.transform.scale(self.image, [175, 175])
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.rect.y = random.randint(0, 5)
        self.rect.x = random.randint(30, 550)
        self.speed = -11
    def update(self, *args):
        self.rect.y -= self.speed
        if self.rect.right < 0:
            self.kill()