import pygame
from car import Car
from random import randint
from stone import Stone
pygame.init()
y1 = -15
v1 = -5
y2 = -15
v2 = -5
timer  = 0
timer += 1
tempo_segundo = 0
largura, altura = 750, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tsunami Run")
img = pygame.image.load("data/objetos/pistaCERTA.png")
nova_img = pygame.transform.scale(img, (largura, altura))
pedaco = pygame.image.load("data/objetos/pedaco-pista.png")
pedra = pygame.image.load("data/objetos/stone.png")
objectGroup = pygame.sprite.Group()
car = Car(objectGroup)
car.rect.center = [90, 350]
final = True
timer = 0
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial black",30)
texto = font.render("Score: ", True, (255,255,255))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)

while final:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            final = False
            pygame.quit()
    y1 -= v1
    if(y1>=700):
        y1 = -50
    y2 -= v2
    if (y2 >= 700):
        y2 = -50
    if timer > 20:
        timer = 0
    if (timer < 15):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Score: "+ str(tempo_segundo), True, (255, 255, 255))
        timer = 0

    tela.blit(nova_img, (0, 0))
    tela.blit(pedaco, (-25, y1))
    tela.blit(texto, pos_texto)
    tela.blit(pedra,(150, y2))
    objectGroup.update()
    objectGroup.draw(tela)
    pygame.display.update()