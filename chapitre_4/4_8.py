import pygame, sys
from pygame.locals import *


class Message(pygame.sprite.Sprite):
    def __init__(self, msg, duration, SIZE_X, SIZE_Y, FPS):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Palationo", 72)
        self.image = self.font.render(msg, True, Color("red"))
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.midleft = (0, SIZE_Y // 2)
        assert self.width <= SIZE_Y, "Message too big"
        self.movement = 1  # 1 = right, 0 = left
        self.speed = int((SIZE_X - self.width) / (duration*FPS))

    def update(self, SIZE_X, SIZE_Y):

        if self.movement == 1:
            if self.rect.x + self.speed >= SIZE_X - self.width:
                self.rect.x = SIZE_X - self.width
                self.movement = 0
            else:
                self.rect.x += self.speed
        if self.movement == 0:
            if self.rect.x - self.speed <= 0:
                self.rect.x = 0
                self.movement = 1
            else:
                self.rect.x -= self.speed


def flytext(msg, duration):
    pygame.init()
    done = False
    FPS = 30
    clock = pygame.time.Clock()

    SIZE_X = 600
    SIZE_Y = 200
    size = (SIZE_X, SIZE_Y)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Flytext")
    text = Message(msg, duration, SIZE_X, SIZE_Y, FPS)
    all_texts = pygame.sprite.Group()
    all_texts.add(text)
    while not done:

        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
        all_texts.update(SIZE_X, SIZE_Y)
        screen.fill(Color("white"))
        all_texts.draw(screen)
        pygame.display.update()
        clock.tick(FPS)


msg = input("Enter a message: ")
duration = int(input("Enter a duration in seconds: "))
flytext(msg, duration)

pygame.quit()
sys.exit()
