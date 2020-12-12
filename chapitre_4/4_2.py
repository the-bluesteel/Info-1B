import pygame, sys
from pygame.locals import *
from random import randint
from pygame_functions import draw_point
from math import pi

pygame.init()
size = (400, 400)
screen = pygame.display.set_mode(size)
FPS = 1500
clock = pygame.time.Clock()
pygame.display.set_caption("Methode de Monte-Carlo")
screen.fill(Color("white"))

done = False

"""
Possibilities for a point to be inside the disc -> pi*r**2 / 4
Possibilities for a point overall-> r**2
Rapport: pi / 4
"""

amount_of_points = 0
inside_the_disc = 0

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

    p = (randint(0, 399), randint(0, 399))
    color = "red"
    if p[0] ** 2 + p[1] ** 2 <= size[0] ** 2:
        inside_the_disc += 1
        color = "green"
    amount_of_points += 1
    draw_point(p[0], p[1], screen, Color(color))
    if pygame.time.get_ticks() % 2000 == 0:
        pi_found = (inside_the_disc / amount_of_points) * 4
        print(f"pi is around {pi_found}")
        print(f"difference to actual pi: {abs(pi - pi_found)}")
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
