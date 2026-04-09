import pygame
import sys
import os

pygame.init()
pygame.mixer.init()
weight = 1024
height = 768
okno = pygame.display.set_mode((weight , height))
pygame.display.set_caption("OKNO")

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

def protect_file(filename , size = None):
    try:
        script = os.path.dirname(os.path.abspath(__file__))
        imagepath = os.path.join(script , filename)
        image = pygame.image.load(imagepath)
        if size:
            image = pygame.transform.scale(image , size)
        print("1")
        return image
    except pygame.error as e:
        print(f"Неудалось загрузить изображение {filename}: {e}")
        return None
person = protect_file("1121.jpg")

console = True
clock = pygame.time.Clock().tick(120)

while console:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            console = False
    okno.fill(GREEN)
    pygame.display.flip()


pygame.quit()
sys.exit()