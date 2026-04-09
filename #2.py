import sys
import pygame

#создавание
pygame.init()
weight = 1024
height = 768
okno = pygame.display.set_mode((weight , height))
pygame.display.set_caption("okno")

#цвета
BLUEGREEN = (30, 147, 123)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
TURQUOISE = (0, 255, 255)
RED = (255, 0, 0)
BLACK = (0 , 0 , 0)
DARKBLUE = (65, 79, 113)
BLUE = (0, 0, 255)

console = True
clock = pygame.time.Clock().tick(120)

while console:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            console = False
    okno.fill(BLUEGREEN)
    pygame.draw.rect(okno, ORANGE, (50, 50, 100, 100))
    pygame.draw.rect(okno , RED , (50 , 50 , 100 , 100) , 5)
    pygame.draw.circle(okno , TURQUOISE , (230 , 100) , 50)
    pygame.draw.circle(okno , WHITE , (230 , 100) , 50 , 5)
    pygame.draw.line(okno , BLACK , (50 , 155) , (280 , 155) , 4)
    pygame.draw.ellipse(okno , DARKBLUE , (50 , 200 , 130 , 34))
    treugolnik = [(600 , 300) , (600 , 450) , (750 , 450)]
    pentagon_points = [
        (100, 450),  # верхняя вершина
        (130, 480),  # правая верхняя
        (120, 520),  # правая нижняя
        (80, 520),  # левая нижняя
        (70, 480)  # левая верхняя
    ]
    pygame.draw.polygon(okno , BLUE , treugolnik)
    pygame.draw.polygon(okno , BLUE , pentagon_points)
    duga = (100 , 600 , 400 , 300)
    duga1 = 1
    duga2 = 3
    pygame.draw.arc(okno , WHITE , duga , duga1 , duga2 , 5)
    pygame.display.flip()
pygame.quit()
sys.exit()