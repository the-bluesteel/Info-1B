import pygame, sys
from pygame_functions import *
from pygame.locals import *
from random import randint

pygame.init()
size = (1000, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mouvement brownien")
FPS = 20
screen.fill(Color("black"))
clock = pygame.time.Clock()
done = False
p = (randint(0, size[0] - 1), randint(0, size[1] - 1))


def get_cross(point, pixels):
    pixels -= 0 if pixels % 2 == 0 else 1
    assert pixels > 0, "Error, amount of pixels bigger than 0"
    amount = pixels // 2
    a = (point[0] - amount, point[1] - amount)
    b = (point[0] + amount, point[1] - amount)
    c = (point[0] - amount, point[1] + amount)
    d = (point[0] + amount, point[1] + amount)
    return a, d, b, c


def deplacement(point):
    x, y = randint(-100, 100), randint(-100, 100)
    p = [point[0] + x, point[1] + y]
    if p[0] <= 0:
        p[0] = 0
    if p[0] >= size[0] - 1:
        p[0] = 999
    if p[1] <= 0:
        p[1] = 0
    if p[1] >= size[1] - 1:
        p[1] = 999
    draw_line(point, p, screen, Color("red"))
    return p


def draw_cross(point):
    cross = get_cross(point, 11)
    a, b, c, d = cross[0], cross[1], cross[2], cross[3]
    draw_line(a, b, screen, Color("cyan"), 1)
    draw_line(c, d, screen, Color("cyan"), 1)


while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

    a = deplacement(p)
    p = (a[0], a[1])
    draw_cross(p)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
