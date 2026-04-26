import pygame
import sys
import math
import random

pygame.init()
width = 1024
height = 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("screen")

# color

BLUEGREEN = (30, 147, 123)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
TURQUOISE = (0, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
DARKBLUE = (65, 79, 113)
BLUE = (0, 0, 255)
PURPLE = (106, 90, 205)
WHITEGREEN = (0, 255, 0)
GREEN = (60, 179, 113)

# global

GRAVITY = 500
DAMPING = 0.8
FRIKTION = 0.97
AIR_RES = 0.99


class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.mass = radius / 10
        self.trail = []
        self.trail_len = 30

    def apply_force(self, fx, fy):
        self.ax += fx / self.mass
        self.ay += fy / self.mass

    def update(self, dt):
        self.vx += self.ax * dt
        self.vy += self.ay * dt
        self.vx *= AIR_RES
        self.vy += AIR_RES
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.ax = 0
        self.ay = 0