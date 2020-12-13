import pygame
from pygame.locals import *
import sys
from random import randint

BUTTON_BOX_HEIGHT = 60
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 30
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 + BUTTON_BOX_HEIGHT
CELL_WIDTH, CELL_HEIGHT = 8, 8
AMOUNT_CELLS_X, AMOUNT_CELLS_Y = 100, 75
GENERATION = 0

red_button_clicked = False


def draw_cell(screen, i, j, color):
    x, y = (i + 1 / 2) * CELL_WIDTH, (j + 1 / 2) * CELL_HEIGHT
    rect = pygame.Rect(0, 0, 6, 6)
    rect.center = (x, y)
    pygame.draw.rect(screen, color=color, rect=rect)


def draw_buttons(screen):
    def draw_button(screen, x, y, width, height, color):
        button = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, color=Color(color), rect=button)
        return button

    # draw white box
    draw_button(screen, 0, AMOUNT_CELLS_Y * CELL_HEIGHT, SCREEN_WIDTH, BUTTON_BOX_HEIGHT, (255, 255, 255))

    # draw buttons
    space = int((1 / 4) * (SCREEN_WIDTH - 3 * BUTTON_WIDTH))

    buttons = []
    space_height = ((BUTTON_BOX_HEIGHT - BUTTON_HEIGHT) // 2) + CELL_HEIGHT * AMOUNT_CELLS_Y
    buttons.append(draw_button(screen, space, space_height, BUTTON_WIDTH, BUTTON_HEIGHT,
                               "green"))
    buttons.append(
        draw_button(screen, space * 2 + BUTTON_WIDTH, space_height, BUTTON_WIDTH, BUTTON_HEIGHT, "red"))
    buttons.append(
        draw_button(screen, space * 3 + 2 * BUTTON_WIDTH, space_height, BUTTON_WIDTH, BUTTON_HEIGHT, "blue"))
    return buttons  # rect


def draw_board(screen, population):
    """
    :param screen: /
    :param population: list of dimensions AMOUNT_CELLS_X * AMOUNT_CELLS_Y with True for living cell otherwise False
    """

    # fill lattice black
    pygame.draw.rect(screen, color=(0, 0, 0), rect=pygame.Rect(0, 0, SCREEN_WIDTH, AMOUNT_CELLS_Y * CELL_HEIGHT))
    for i in range(AMOUNT_CELLS_X):
        for j in range(AMOUNT_CELLS_Y):
            draw_cell(screen, i, j, Color("yellow") if population[j][i] else Color("black"))


def count_population(population):
    counter = 0
    for _ in population:
        counter += _.count(True)
    return counter


def evolution(population):
    def count_living_neighbours(population, i, j):
        counter = 0
        for x in [i - 1, i, i + 1]:
            for y in [j - 1, j, j + 1]:
                if (x, y) != (i, j) and AMOUNT_CELLS_X > x > 0 and AMOUNT_CELLS_Y > y > 0:
                    counter += 1 if population[y][x] else 0
        return counter

    living_neighbours = [[count_living_neighbours(population, i, j) for i in range(AMOUNT_CELLS_X)]
                         for j in range(AMOUNT_CELLS_Y)]
    for i in range(AMOUNT_CELLS_X):
        for j in range(AMOUNT_CELLS_Y):
            if not population[j][i] and living_neighbours[j][i] == 3:
                population[j][i] = True
            elif population[j][i]:
                if living_neighbours[j][i] in [2, 3]:
                    continue
                else:
                    population[j][i] = False


def invert_cells(population, coordinates, screen):
    def get_cell(i, j):
        return pygame.Rect((i + 1 / 2) * CELL_WIDTH, (j + 1 / 2) * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)

    x1, y1, x2, y2 = coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1]
    if y1 > SCREEN_HEIGHT - BUTTON_BOX_HEIGHT:
        y1 = SCREEN_HEIGHT - BUTTON_BOX_HEIGHT
    if y2 > SCREEN_HEIGHT - BUTTON_BOX_HEIGHT:
        y2 = SCREEN_HEIGHT - BUTTON_BOX_HEIGHT

    x = x1 if x2 - x1 > 0 else x2
    y = y1 if y2 - y1 > 0 else y2
    rect = pygame.Rect(x, y, abs(x1 - x2), abs(y1 - y2))
    for i in range(AMOUNT_CELLS_X):
        for j in range(AMOUNT_CELLS_Y):
            rect1 = get_cell(i, j)

            if rect1.colliderect(rect):
                population[j][i] = True if not population[j][i] else False

    pygame.display.set_caption(f"Génération {GENERATION}; population {count_population(population)}")
    draw_board(screen, population)
    pygame.display.update()


def green_button(screen, population):
    global GENERATION
    GENERATION += 1
    evolution(population)
    draw_board(screen, population)
    pygame.display.set_caption(f"Génération {GENERATION}; population {count_population(population)}")
    pygame.display.update()


def red_button(screen, population):
    if red_button_clicked:
        global GENERATION
        GENERATION += 1
        evolution(population)
        draw_board(screen, population)
        pygame.display.set_caption(f"Génération {GENERATION}; population {count_population(population)}")
        pygame.display.update()


def main():
    global red_button_clicked, GENERATION
    pygame.init()
    population = [[False] * AMOUNT_CELLS_X for _ in range(AMOUNT_CELLS_Y)]

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(f"Génération {GENERATION}; population 0")
    screen.fill((0, 0, 0))
    buttons = draw_buttons(screen)
    draw_board(screen, population)
    pygame.display.update()
    clock = pygame.time.Clock()
    done = False
    x1, y1, x2, y2 = -1, 0, 0, 0
    while not done:
        red_button(screen, population)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    lattice = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT - BUTTON_BOX_HEIGHT)
                    if lattice.collidepoint(pygame.mouse.get_pos()):
                        x1, y1 = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                    elif buttons[0].collidepoint(pygame.mouse.get_pos()):
                        green_button(screen, population)

                    elif buttons[1].collidepoint(pygame.mouse.get_pos()):
                        red_button_clicked = True
                    elif buttons[2].collidepoint(pygame.mouse.get_pos()):
                        population = [[False] * AMOUNT_CELLS_X for _ in range(AMOUNT_CELLS_Y)]
                        GENERATION = 0
                        draw_board(screen, population)
                        pygame.display.set_caption(f"Génération {GENERATION}; population 0")
                        pygame.display.update()

            if event.type == pygame.MOUSEBUTTONUP:
                if red_button_clicked:
                    red_button_clicked = False
                if x1 != -1:
                    x2, y2 = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                    invert_cells(population, ((x1, y1), (x2, y2)), screen)
                    x1 = -1
    clock.tick(30)
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
