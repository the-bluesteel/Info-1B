import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 20
pygame.display.set_caption("Moving Square")
SIZE_X = 400
SIZE_Y = 300
size = (SIZE_X, SIZE_Y)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
done = False
screen.fill(Color("blue"))


class Square(pygame.sprite.Sprite):
    def __init__(self, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([height, height])
        self.image.fill(color)
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.topleft = ((SIZE_X // 2) - (height // 2), (SIZE_Y - 1) - height)

    def update(self, m):
        """
        :param m: 1 = Left, 2 = Right, 3 = Still
        :return:
        """
        if m == 1:
            if self.rect.x > 5:
                self.rect.x -= 5
            else:
                self.rect.x = 0

        elif m == 2:
            if self.rect.x < SIZE_X-6 -self.height:
                self.rect.x += 5
            else:
                self.rect.x = SIZE_X - 1 - self.height


m = 3
all_sprites = pygame.sprite.Group()

square = Square(20, Color("red"))
all_sprites.add(square)


while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == KEYUP:
            if event.key == K_LEFT and m == 1 or event.key == K_RIGHT and m == 2:
                m = 3
        if event.type == KEYDOWN:
            if event.key == K_LEFT and m == 3:
                m = 1
            if event.key == K_RIGHT and m == 3:
                m = 2


    all_sprites.update(m)
    screen.fill(Color("blue"))
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
