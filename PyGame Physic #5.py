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
        self.trail.append((int(self.x), int(self.y)))
        if len(self.trail) >= self.trail_len:
            self.trail.pop(0)
        self.check_adg()

    def check_adg(self):  # функция для проверки столкновение с границей
        if self.y + self.radius > height:
            self.y = height - self.radius
            self.vy = -self.vy * DAMPING
            self.vx *= FRIKTION
        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy = -self.vy * DAMPING
        if self.x + self.radius > width:
            self.x = width - self.radius
            self.vx = -self.vx * DAMPING
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx = -self.vx * DAMPING

    def trail_draw(self, surface):
        for i, pos in enumerate(self.trail):
            alpha = int(255 * (i / len(self.trail))) if self.trail else 255
            color = (*self.color, alpha)
            pygame.draw.circle(surface, self.color, pos, max(1, self.radius // 4))
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(surface, BLACK, (int(self.x), int(self.y)), self.radius, 6)
        if abs(self.vx) > 1 or abs(self.vy) > 1:
            end_x = self.x + self.vx * 0.1
            end_y = self.y + self.vy * 0.1
            pygame.draw.line(surface, GREEN, (self.x, self.y), (end_x, end_y), 5)


class Particle:
    def __init__(self, x, y, vx, vy, color, lifetime=3):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.lifetime = lifetime
        self.size = random.randint(5, 15)
        self.age = 0

    def is_alive(self):
        return self.age < self.lifetime

    def draw(self, surface):
        alpha = max(0, 1 - (self.age / self.lifetime))
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vy += GRAVITY * 0.5 * dt
        self.age += dt


class Physic_Sim:
    def __init__(self):
        self.balls = []
        self.particales = []
        self.gravity_enabled = True
        self.show_vector = True
        self.paused = False
        self.create_balls()

    def create_balls(self):
        ball1 = Ball(200, 150, 40, ORANGE)
        ball1.vy = 120
        self.balls.append(ball1)
        ball2 = Ball(100, 400, 30, DARKBLUE)
        ball2.vx = 85
        ball2.vy = -50
        self.balls.append(ball2)
        ball3 = Ball(30, 300, 50, RED)
        self.balls.append(ball3)

    def add_balls(self, x, y):
        radius = random.randint(20, 80)
        color = random.choice([WHITE, ORANGE, TURQUOISE, RED, BLACK, DARKBLUE, BLUE, PURPLE, WHITEGREEN, GREEN])
        ball = Ball(x, y, radius, color)
        ball.vx = random.randint(-300, 300)
        ball.vy = random.randint(-200, 300)
        self.balls.append(ball)

    def create_particales(self, x, y):
        for i in range(100):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(40, 180)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            color = random.choice([WHITE, ORANGE, TURQUOISE, RED, BLACK, DARKBLUE, BLUE, PURPLE, WHITEGREEN, GREEN])
            self.particales.append(Particle(x, y, vx, vy, color))

    def update(self, dt):
        if self.paused:
            return
        for i in self.balls:
            if self.gravity_enabled:
                i.apply_force(0, GRAVITY * i.mass)
            i.update(dt)
        self.ball_collision()
        self.particales = [j for j in self.particales if j.is_alive()]
        for g in self.particales:
            g.update(dt)
    def ball_collision(self):
