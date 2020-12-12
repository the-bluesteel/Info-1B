from pygame.locals import *
import pygame
import sys
from random import randrange, randint

"""
Initialisation:
1) Windows Key -> CMD -> pip install pygame
"""
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 200
LYCEE = "ATHENEE"
NUMERO = 12345


def main():
    # initialize pygame library
    pygame.init()
    # create new screen with indicated dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0, 0, 0))
    # set title of the windows
    pygame.display.set_caption(f"Grenouille - {LYCEE} - {NUMERO}")
    done = False
    game_stopped = False

    # initializing key objects
    clock = pygame.time.Clock()
    frog = Frog()
    street = Street()
    sens = 0  # 0 - standing still | 1 - up | 2 - down | 3 - left | 4 - right
    changement_de_vitesse = 0  # | 0 - nothing | 1 - slow down | 2 - speed up
    for i in [40, 80, 120, 160]:
        street.append_car(Car(y=i, speed=randint(-20, 20)))

    while not done:

        # Repeated actions
        screen.fill((0, 0, 0))
        frog.draw_frog(screen)
        street.drive_cars()
        street.draw_cars(screen)
        pygame.display.update()
        if street.check_collision(frog):
            street.stop_cars()
            frog.color = Color("red")
            game_stopped = True
        elif frog.y - 3 < 0:
            game_stopped = True
            frog.color = Color("green")
            street.stop_cars()

        # moving frog respectively
        if sens != 0 and not game_stopped:
            if sens == 1:
                frog.y -= 2
            elif sens == 2:
                frog.y += 2
            elif sens == 3:
                frog.x -= 2
            elif sens == 4:
                frog.x += 2

        # slowing down or speeding up
        if changement_de_vitesse != 0 and not game_stopped:
            if changement_de_vitesse == 1:
                street.slow_down_cars(1)
            elif changement_de_vitesse == 2:
                street.speed_up_cars(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Terminate program if program is being quitted
                done = True
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.fill((0, 0, 0))  # Not necessary, but demanded
                    frog.reset_frog()
                    street.reset_cars()
                    game_stopped = False

                elif event.key == pygame.K_UP:
                    sens = 1
                elif event.key == pygame.K_DOWN:
                    sens = 2
                elif event.key == pygame.K_LEFT:
                    sens = 3
                elif event.key == pygame.K_RIGHT:
                    sens = 4
                elif event.key == pygame.K_a:
                    changement_de_vitesse = 2
                elif event.key == pygame.K_s:
                    changement_de_vitesse = 1
            if event.type == pygame.KEYUP:
                if (event.key, sens) in zip([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT], [1, 2, 3, 4]):
                    sens = 0
                if event.key in [pygame.K_a, pygame.K_s]:
                    changement_de_vitesse = 0
        # Setting FPS to 25 -> 25 times per Second
        clock.tick(25)

    pygame.quit()


class Frog:
    def __init__(self, x=300, y=180, color=Color("white")):
        self.x, self.y = x, y
        self.color = color

    def reset_frog(self):
        self.x, self.y = 300, 180
        self.color = Color("white")
        print("frog reset done")

    def draw_frog(self, screen):
        pygame.draw.circle(screen, color=self.color, center=(self.x, self.y), radius=3, width=1)


class Car:
    def __init__(self, x=0, y=200, width=20, height=10, speed=randint(-20, 20)):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.speed = speed

    def reset_car(self):
        self.x = 0
        self.speed = randint(-20, 20)
        print("car reset done")

    def drive_car(self):
        global SCREEN_WIDTH
        self.x += self.speed
        if self.x > SCREEN_WIDTH:
            self.x = -self.width
        elif self.x + self.width < 0:
            self.x = SCREEN_WIDTH

    def contains_pixel(self, x, y):
        car_shape = pygame.Rect(self.x, self.y, self.width, self.height)
        return car_shape.collidepoint(x, y)

    def draw_car(self, screen):
        car_shape = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, color=Color("yellow"), rect=car_shape, width=1)


class Street:
    def __init__(self):
        self.list_of_cars = []

    def append_car(self, car):
        assert isinstance(car, Car), "Invalid Car appended to street"
        self.list_of_cars.append(car)

    def speed_up_cars(self, amount):
        assert amount > 0, "Increase of speed must be a positive integer"
        for car in self.list_of_cars:
            if car.speed != 0:
                car.speed += amount if car.speed > 0 else -amount
            else:
                sens = randint(0, 1) * 2 - 1
                car.speed = sens * amount

    def slow_down_cars(self, amount):
        assert amount > 0, "Decrease of speed must be a positive integer"
        for car in self.list_of_cars:
            if abs(car.speed) > amount:
                car.speed -= amount if car.speed > 0 else -amount
            else:
                car.speed = 0

    def stop_cars(self):
        for car in self.list_of_cars:
            car.speed = 0

    def drive_cars(self):
        for car in self.list_of_cars:
            car.drive_car()

    def draw_cars(self, screen):
        for car in self.list_of_cars:
            car.draw_car(screen)

    def reset_cars(self):
        for car in self.list_of_cars:
            car.reset_car()

    def check_collision(self, frog):
        pixels = [(frog.x, frog.y + 3), (frog.x, frog.y - 3), (frog.x - 3, frog.y), (frog.x + 3, frog.y)]
        for car in self.list_of_cars:
            for pixel in pixels:
                if car.contains_pixel(pixel[0], pixel[1]):
                    return True

        return False


if __name__ == "__main__":
    main()
    sys.exit()
