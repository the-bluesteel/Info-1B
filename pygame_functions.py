import pygame, sys
from pygame.locals import *


def draw_triangle(a, b, c, screen, color, width=1):
    """
    :param a: position
    :param b: position
    :param c: position
    :param screen: screen
    :param color: color
    :param width: width
    :return: None
    """
    pygame.draw.line(screen, color, a, b, width)
    pygame.draw.line(screen, color, b, c, width)
    pygame.draw.line(screen, color, c, a, width)


def draw_line(a, b, screen, color, width=1):
    pygame.draw.line(screen, color, a, b, width)


def draw_point(x, y, screen, color):
    screen.set_at((x, y), color)


def draw_rect(x, y, height, width, screen, color, w):
    pygame.draw.rect(screen, color, (x, y, width, height), w)


def draw_circle(x, y, screen, color, radius, w):
    pygame.draw.circle(screen, color, (x, y), radius, w)
