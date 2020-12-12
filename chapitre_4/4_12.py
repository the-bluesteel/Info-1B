import pygame, sys
from pygame.locals import *
from pygame_functions import *

pygame.init()
SIZE_X = 800
SIZE_Y = 660
size = (SIZE_X, SIZE_Y)
screen = pygame.display.set_mode(size)
screen.fill(Color("black"))


class Board:
    def __init__(self):
        self.generation = 0
        self.population()
        for row in range(100):
            for column in range(75):
                pass

    def draw_board(self, screen):
        screen.fill(Color("black"))
        draw_rect(0, 600, 60, 800, screen, Color("white"), 0)


board = Board()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

    board.draw_board(screen)
    pygame.display.update()

pygame.quit()
sys.exit()
