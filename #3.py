import sys
import pygame

#создавание
pygame.init()
weight = 1024
height = 1024
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
PURPLE = (106, 90, 205)
WHITEGREEN = (0 , 255 , 0)
GREEN = (60, 179, 113)

console = True
clock = pygame.time.Clock().tick(120)

while console:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            console = False
        okno.fill(GREEN)
        pygame.draw.circle(okno , PURPLE , (512 , 512) , 120)
        pygame.draw.circle(okno, BLUE, (512, 332), 60)
        pygame.draw.line(okno , BLACK, (430 , 582) , (400 , 800) , 20)
        pygame.draw.line(okno, BLACK, (590, 582), (624, 800), 20)
        pygame.draw.line(okno, BLACK, (592, 512), (650, 350), 15)
        pygame.draw.line(okno, BLACK, (432, 512), (374, 350), 15)
        pygame.display.flip()
pygame.quit()
sys.exit()