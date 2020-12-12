from random import randint
import pygame, sys
from pygame.locals import *
from pygame_functions import draw_rect

pygame.init()
done = False
SIZE_X = 400
SIZE_Y = 400
size = (SIZE_X, SIZE_Y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rectangles")
all_rectangles = pygame.sprite.Group()


class Rectangle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(Color("white"))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        draw_rect(0, 0, height - 1, width - 1, self.image, Color("red"), 1)
        self.group = group

    def update(self, pos):
        if self.rect.collidepoint(pos):
            self.group.remove(self)
            self.kill()


while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (True, False, False):
                rect = Rectangle(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], randint(20, 50), randint(10, 30),
                                 all_rectangles)
                all_rectangles.add(rect)
            if pygame.mouse.get_pressed() == (False, False, True):
                all_rectangles.update(pygame.mouse.get_pos())

    screen.fill(Color("white"))
    all_rectangles.draw(screen)
    pygame.display.update()

pygame.quit()
sys.exit()
