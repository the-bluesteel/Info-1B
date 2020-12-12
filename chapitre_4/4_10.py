import pygame, sys
from pygame.locals import *
from random import randint
from math import sqrt
from pygame_functions import draw_circle, draw_rect

pygame.init()
FPS = 60
clock = pygame.time.Clock()
done = False
SIZE_X = 500
SIZE_Y = 600
size = (SIZE_X, SIZE_Y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Damage 0 - Score 0")
score = 0
damage = 0
screen.fill(Color("black"))
message_displayed = False
number_of_torpedos = 0


class StarShip(pygame.sprite.Sprite):
    global SIZE_Y
    global SIZE_X
    global speed
    global m

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = SIZE_X // 2
        self.y = SIZE_Y - 30
        self.image = pygame.Surface([41, 41])
        self.rect = self.image.get_rect()
        self.image.fill(Color("white"))
        self.rect.center = (self.x, self.y)

    def get_rect(self):
        return self.rect

    def update(self):
        if m != 3:
            dx = (-1) * speed if m == 1 else speed
            if self.x + dx <= 0:
                self.x = 0
            elif self.x + dx >= SIZE_X - 41:
                self.x = SIZE_X - 41
            else:
                self.x += dx
        self.rect.x = self.x


def final_message(msg, screen):
    global SIZE_X
    global message_displayed
    font = pygame.font.SysFont("Palatino", 62)
    text = font.render(msg, True, Color(212, 44, 2))
    draw_rect(0, 0, text.get_height(), text.get_width(), text, Color(133, 0, 0), 3)
    screen.blit(text, ((SIZE_X - text.get_width()) // 2, 20))
    message_displayed = True
    pygame.display.update()


class Torpedo(pygame.sprite.Sprite):
    global SIZE_Y
    global SIZE_X
    global FPS

    def __init__(self, starship: StarShip, group, group2):
        pygame.sprite.Sprite.__init__(self)
        self.y = starship.y - 20
        self.x = starship.x
        self.image = pygame.Surface([3, 11])
        self.image.fill(Color("cyan"))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.group = group
        self.group2 = group2

    def update(self):
        self.rect.y -= int(400 / FPS)
        if self.rect.y <= -11:
            self.group.remove(self)
            self.group2.remove(self)
            self.kill()

    def destroy(self):
        self.group.remove(self)
        self.group2.remove(self)
        self.kill()

    def get_rect(self):
        return self.rect


def get_amount_of_torpedos(l):
    count = 0
    for i in l:
        if type(i) == Torpedo:
            count += 1
    return count


class Alien(pygame.sprite.Sprite):
    global SIZE_Y
    global SIZE_X
    global FPS

    def __init__(self, group, group2, v=-1):
        pygame.sprite.Sprite.__init__(self)
        self.x = randint(12, 487)
        self.y = 12
        r, g, b = randint(128, 255), randint(0, 255), 0
        self.color = Color(r, g, b)
        self.v = randint(100, 199) if v == -1 else v
        self.vy = randint(50, self.v - 1)
        self.vx = int(sqrt(self.v ** 2 - self.vy ** 2))
        self.image = pygame.Surface([24, 24])
        self.rect = self.image.get_rect()
        draw_circle(12, 12, self.image, self.color, 12, 0)
        self.group = group
        self.group2 = group2
        self.ov = self.v
        self.v //= FPS
        self.vy //= FPS
        self.vx //= FPS

    def update(self):
        if self.x + self.vx >= SIZE_X or self.x + self.vx <= 0:
            self.vx *= -1

        self.x += self.vx
        self.y += self.vy
        if self.y >= SIZE_Y + 25:
            self.y = -12

        self.rect.x = self.x
        self.rect.y = self.y

    def collision(self, starship: StarShip):
        return self.rect.colliderect(starship.get_rect())

    def hit(self, torpedo: Torpedo):
        return self.rect.colliderect(torpedo.get_rect())

    def destroy(self):
        self.group.remove(self)
        self.group2.remove(self)
        v = self.ov
        self.kill()
        return v


speed = int(200 / FPS)
all_sprites = pygame.sprite.Group()
all_torpedos = pygame.sprite.Group()
all_aliens = pygame.sprite.Group()
starship = StarShip()
all_sprites.add(starship)
m = 3  # 3 = Still, 1 = Left, 2 = Right -> Movement of starship

for _ in range(10):
    alien = Alien(all_sprites, all_aliens)
    all_sprites.add(alien)
    all_aliens.add(alien)

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (True, False, False):
                if message_displayed:
                    done = True
                elif m == 3:
                    m = 1
            if pygame.mouse.get_pressed() == (False, False, True):
                if not message_displayed and m == 3:
                    m = 2
        if event.type == MOUSEBUTTONUP and not message_displayed:
            if m == 1 and not pygame.mouse.get_pressed()[0] or m == 2 and not pygame.mouse.get_pressed()[2]:
                m = 3
        if event.type == KEYDOWN and not message_displayed:
            if event.key == K_SPACE:
                if get_amount_of_torpedos(all_sprites) < 6:
                    torpedo = Torpedo(starship, all_sprites, all_torpedos)
                    all_sprites.add(torpedo)
                    all_torpedos.add(torpedo)

    for alien in all_aliens:
        if alien.collision(starship):
            damage += 1
            if damage >= 3:
                final_message(f"Game Over - Score {score}", screen)
            else:
                v = alien.destroy()
                a = Alien(all_sprites, all_aliens, int(v * 1.1))
                all_sprites.add(a)
                all_aliens.add(a)
                score += 1
                pygame.display.set_caption(f"Damage {damage} - Score {score}")
        else:
            for torpedo in all_torpedos:
                if alien.hit(torpedo):
                    torpedo.destroy()
                    v = alien.destroy()

                    a = Alien(all_sprites, all_aliens, int(v * 1.1))
                    all_sprites.add(a)
                    all_aliens.add(a)
                    score += 1
                    pygame.display.set_caption(f"Damage {damage} - Score {score}")



    if not message_displayed:
        all_sprites.update()
        screen.fill(Color("black"))
        all_sprites.draw(screen)
        pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
