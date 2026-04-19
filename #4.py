import pygame
import sys
import os

from pygame.examples.sprite_texture import renderer

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

def draw(weight , height , color , text = ''):
    okno = pygame.Surface((weight , height))
    okno.fill(WHITE)
    if text:
        txt = pygame.font.Font(None , 36)
        renedrer_text = txt.render(text , True , BLUEGREEN)
        cord_text = renedrer_text.get_rect(center = (weight // 2 , height // 2))
        okno.blit(renedrer_text , cord_text)
    return okno

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
    except FileNotFoundError as e:
        print(f"Неудалось загрузить изображение {filename}: {e}")
        return None
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

phon = protect_file("images.jpg" , (1024 , 768))
if phon is None:
    phon = draw(150 , 150 , PURPLE , "phon")
person = protect_file("pngwing.com (1).png" , (100, 100))
if person is None:
    pesron = draw(150 , 150 , PURPLE , "person")
enemy = protect_file("pngwing.com.png" , (250 , 250))
if enemy is None:
    enemy = draw(150 , 150 , PURPLE , "person")
music = music_file("Plants_vs._Zombies_OST_-_Roof_Theme_(SkySound.cc).mp3")
load_music = loading("28 Days Later Main Theme (From 28 Days Later).mp3")

if load_music:
    load_music.set_volume(0.7)
pygame.mixer.music.set_volume(0.4)


console = True
clock = pygame.time.Clock().tick(120)

cord_person = [128 , 300]
scale_person = 1.0

while console:
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            console = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                cord_person[1] -= 10
            elif event.key == pygame.K_s:
                cord_person[1] += 10
            elif event.key == pygame.K_a:
                cord_person[0] -= 10
            elif event.key == pygame.K_d:
                cord_person[0] += 10
            elif event.key == pygame.K_e:
                if scale_person == 1.0:
                    scale_person = 0.5
                else:
                    scale_person = 1.0
            elif event.key == pygame.K_m:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
    if cord_person[0] >= weight - 100:
    if cord_person[1] >= height - 100:

    if phon:
        okno.blit(phon , (0 , 0))
    if person:
        okno.blit(person , (128 , 300))
    if enemy:
        okno.blit(enemy , (600 , 165))
    pygame.display.flip()




pygame.quit()
sys.exit()