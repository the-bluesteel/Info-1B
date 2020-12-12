import pygame, sys
from pygame.locals import *
from random import randint, choice
from pygame_functions import draw_triangle, draw_point

pygame.init()
size = (600, 480)
FPS = 1000
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Triangle de Sierpinski")
screen.fill(Color("white"))
clock = pygame.time.Clock()

done = False
A, B, C = (20, 460), (size[0] // 2, 20), (579, 460)
sommets = [A, B, C]
p = [(randint(1, 599), randint(1, 478))]
draw_triangle(A, B, C, screen, Color("black"), 3)
i = 1
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    s = choice(sommets)
    p_i = (int((s[0] + p[i - 1][0]) / 2), int((s[1] + p[i - 1][1]) / 2))
    p.append(p_i)
    color = "blue" if i > 9 else "blue"
    draw_point(p_i[0], p_i[1], screen, Color(color))
    i += 1

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
