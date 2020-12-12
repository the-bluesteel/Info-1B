import pygame, sys
from pygame.locals import *
from pygame_functions import draw_circle, draw_rect
from random import randint

pygame.init()
SIZE_X = 400
SIZE_Y = 400
size = (SIZE_X, SIZE_Y)
pygame.display.set_caption("Balls")
screen = pygame.display.set_mode(size)
rayon_des_balls = 5
amount_of_balls = 20
all_balls = pygame.sprite.Group()


def verify_mouse(pos, center, radius):
    return True if (pos[0] - center[0]) ** 2 + (pos[1] - center[1]) ** 2 <= radius ** 2 else False


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([radius * 2, radius * 2])
        draw_circle(radius, radius, self.image, Color("white"), radius, 0)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.group = group
        self.radius = radius

    def update(self, pos):
        if verify_mouse(pos, self.rect.center, self.radius):
            self.group.remove(self)
            self.kill()


done = False
for b in range(amount_of_balls):
    ball = Ball(randint(0, SIZE_X - 1), randint(0, SIZE_Y - 1), rayon_des_balls, all_balls)
    all_balls.add(ball)

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (True, False, False):
                all_balls.update(pygame.mouse.get_pos())

    screen.fill(Color("black"))
    all_balls.draw(screen)
    pygame.display.update()

pygame.quit()
sys.exit()
