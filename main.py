import pygame
from pygame.locals import *


WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# constants


# variables
cuadrado = pygame.Rect(0,HEIGHT//2,60,60)
velocidad = -8
gravedad = 0.4


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

    # code here
    #cuadrado.x += velocidad[0]
    cuadrado.y += velocidad
    velocidad += gravedad
    pygame.draw.rect(screen, (255, 255, 255), cuadrado)

    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(30)