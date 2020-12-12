import pygame, sys, random
from sys import maxsize


s = pygame.display.set_mode((600, 400))
pygame.init()

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for evt in pygame.event.get():
        if evt.type is pygame.QUIT:
            pygame.quit()
            sys.exit()
    for i in range(400):
        for j in range(600):
            r = s.get_rect(size=(1,1))
            r.x = j
            r.y = i
            s.fill(tuple(random.randint(0, 255) for _ in range(3)), r, )

    pygame.display.update(r)

zn_1 = 0




print(str(dir(pygame)).replace("',", "\n"))