import pygame

pygame.init()
width = 1024
height = 1024
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Screen")

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
GRAY = (182, 182, 182)


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 64
        self.color = ORANGE
        self.dx = 0
        self.dy = 0
        self.speed = 2

    def update(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        if self.x + self.size or self.y + self.size == 1024:
            self.x, self.y = 0, 0
        elif self.x - self.size or self.y - self.size == 0:
            self.x, self.y = 0, 0

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)

    def movement(self, dx, dy):
        self.dx = dx * self.speed
        self.dy = dy * self.speed


class Keybutton:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.color_on = RED
        self.is_clicked = False
        self.is_hovered = False
        self.font = pygame.font.Font("Monospace", 10)

    def tneve(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.is_clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.is_clicked = False
        return False

    def draw(self, surface):
        color = DARKBLUE
        if self.is_clicked:
            color = PURPLE
        pygame.draw.rect(surface, color, self.rect)
        text = self.font.render(self.text, True, BLACK)
        text_form = text.get_rect(center=self.rect.center)
        surface.blit(text, text_form)


class Text:
    def __init__(self, x, y, height, width):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.active = False
        self.font = pygame.font.Font("Bold Gothic", 10)
        self.crosvis = True
        self.crosblink = 0

    def ob_events(self, event):
        if pygame.MOUSEBUTTONDOWN == event.type:
            self.active = self.rect.collidepoint(event.pos)
        elif pygame.KEYDOWN == event.type and self.active:
            if pygame.K_RETURN == event.key:
                return self.text
            elif pygame.K_BACKSPACE == event.key:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
        return None

    def draw_text(self, surface):
        color = GRAY if self.active else WHITE
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 6)
        text_renderer = self.font.render(self.text, True, BLACK)
        surface.blit(text_renderer, (self.rect.x + 5, self.rect.y + 5))
        if self.active and self.crosvis:
            crosshair_x = self.rect.x + 5 + text_renderer.get_width()
            pygame.draw.line(surface, WHITE, (crosshair_x, self.rect.y + 5), (crosshair_x, self.rect.y - 5 + self.rect.height) , 3 )
