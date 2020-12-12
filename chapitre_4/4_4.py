import pygame, sys
from pygame.locals import *
from pygame_functions import draw_point

pygame.init()
SIZE_X = 1200
SIZE_Y = 900
size = (SIZE_X, SIZE_Y)
screen = pygame.display.set_mode(size)
screen.fill(Color(255, 255, 0))
pygame.display.set_caption("Fractale de Mandelbrot")

clock = pygame.time.Clock()

xmin = -2.2
xmax = 1.0
ymin = -1.2
ymax = 1.2
maxinterations = 255
maxradius = 10  # ??? Why would you use this

CENTER_X = SIZE_X // 2
CENTER_Y = SIZE_Y // 2


def genCompCoord(x, y):
    cx = (x * (xmax - xmin) / SIZE_X + xmin)
    cy = (y * (ymax - ymin) / SIZE_Y + ymin)
    return complex(cx, cy)


def suite_z(a, p):
    c = genCompCoord(p[0], p[1])
    z = complex(0, 0)
    if a <= 0:
        return z
    for i in range(a):
        z = z ** 2 + c
        if z.real ** 2 + z.imag ** 2 >= 4:
            return Color(255 - i, max(255 - 2 * i, 0), 0)
    return Color("black")


iy = SIZE_Y // 2




done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

    if not iy < 0:
        for ix in range(SIZE_X):
            p = (ix, iy)
            color = suite_z(maxinterations, p)
            draw_point(ix, iy, screen, color)
            draw_point(ix, SIZE_Y - iy, screen, color)
        iy -= 1
    pygame.display.update()

pygame.quit()
sys.exit()
