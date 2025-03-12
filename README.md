# Gabo_MoureDev_1
Saludos a quienes participaron en mi primer taller

codigo base de pygame

```python
import pygame
from pygame.locals import *


WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# constants


# variables


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

    # code here

    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(30)
```
