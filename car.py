import pygame
class Car(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/objetos/carro.png")
        self.image = pygame.transform.scale(self.image, [90, 100])
        self.rect = pygame.Rect(100, 100, 100, 100)
    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += 11
        elif keys[pygame.K_a]:
            self.rect.x -= 11
        if self.rect.left < -53:
            self.rect.left = -53
        elif self.rect.right > 590:
            self.rect.right = 590