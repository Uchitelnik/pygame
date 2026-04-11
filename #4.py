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
        print(imagepath)
        image = pygame.image.load(imagepath)
        if size:
            image = pygame.transform.scale(image , size)
        print("1")
        return image
    except pygame.error as e:
        print(f"Неудалось загрузить изображение {filename}: {e}")
        return None

def music_file(filename):
    try:
        script = os.path.dirname(os.path.abspath(__file__))
        soundpath = os.path.join(script , filename)
        pygame.mixer.music.load(soundpath)
        pygame.mixer.music.play(-1)
        return True
    except pygame.error as e:
        print(e)
        return False

def loading(filename):
    try:
        script = os.path.dirname(os.path.abspath(__file__))
        loadpath = os.path.join(script , filename)
        sound = pygame.mixer.Sound(loadpath)
        return sound
    except pygame.error as e:
        print(e)
        return None

person = protect_file("ninja_warrior.png" , (512 , 512))
music = music_file("Plants_vs._Zombies_OST_-_Roof_Theme_(SkySound.cc).mp3")
load_music = loading("28 Days Later Main Theme (From 28 Days Later).mp3")

if load_music:
    load_music.set_volume(0.7)
pygame.mixer.music.set_volume(0.4)


console = True
clock = pygame.time.Clock().tick(120)

while console:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            console = False
    okno.fill(GREEN)
    if person:
        okno.blit(person , (128 , 128))
    pygame.display.flip()


pygame.quit()
sys.exit()