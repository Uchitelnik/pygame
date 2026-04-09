import pygame
import sys

#создавание
pygame.init()
weight = 1024
height = 768
okno = pygame.display.set_mode((weight , height))
pygame.display.set_caption("Tregubenko Vladimir")

#цвета
BLUEGREEN = (30, 147, 123)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
TURQUOISE = (0, 255, 255)
RED = (255, 0, 0)

#основной код
console = True
while console:
    for event in pygame.event.get():       #pygame.event.get() = события, которые мы не успели рассмотреть
        if pygame.QUIT == event.type:
            console = False
    okno.fill(TURQUOISE)
    pygame.display.flip()
    pygame.time.Clock().tick(100)
pygame.quit()
sys.exit()