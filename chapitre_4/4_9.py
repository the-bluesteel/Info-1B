import pygame, sys
from pygame.locals import *
from pygame_functions import draw_line, draw_circle

pygame.init()
SIZE_X = 350
SIZE_Y = 350
size = (SIZE_X, SIZE_Y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Joueur 1 peut jouer...")
done = False


def draw_board(s):
    global SIZE_Y, SIZE_X
    third_of_x = int(SIZE_X * (1 / 3))
    third_of_y = int(SIZE_Y * (1 / 3))
    bord_x = int((1 / 20) * SIZE_X)
    bord_y = int((1 / 20) * SIZE_Y)
    s.fill(Color("white"))
    draw_line((third_of_x, bord_y), (third_of_x, SIZE_Y - bord_y), s, Color("black"), 5)
    draw_line((third_of_x * 2, bord_y), (third_of_x * 2, SIZE_Y - bord_y), s, Color("black"), 5)
    draw_line((bord_x, third_of_y), (SIZE_X - bord_x, third_of_y), s, Color("black"), 5)
    draw_line((bord_x, third_of_y * 2), (SIZE_X - bord_x, third_of_y * 2), s, Color("black"), 5)


def define_rectangles():
    size = 100
    rects = []

    bord_x = 10
    bord_y = 10
    board = 5
    for b in range(3):
        for a in range(3):
            rect = Rect((bord_x + (size * a) + (bord_x + board) * a,
                         bord_y + (size * b) + (bord_y + board) * b), (size, size))
            rects.append(rect)
    return rects


def draw_coin(player, rectangle, screen):
    center = rectangle.center
    if player == 1:
        draw_line((center[0] - 40, center[1] + 40), (center[0] + 40, center[1] - 40), screen, Color("blue"), 5)
        draw_line((center[0] - 40, center[1] - 40), (center[0] + 40, center[1] + 40), screen, Color("blue"), 5)
    elif player == 2:
        draw_circle(center[0], center[1], screen, Color("red"), 40, 5)


pos_1 = []
pos_2 = []

rectangles = define_rectangles()
position_of_rectangles = {}
for index, rec in enumerate(rectangles):
    position_of_rectangles.update({index+1: rec})


def check_if_won(pos):
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for x in soln:
        if all(y in pos for y in x):
            print(pos)
            return True
    return False


def check_draw():
    global pos_1, pos_2
    return len(pos_1) + len(pos_2) >= 9


player = 1
won = False
draw_board(screen)
while not done:
    if not won:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (True, False, False):
                    b = True
                    for rectangle in rectangles:
                        if b:

                            if rectangle.collidepoint(pygame.mouse.get_pos()):
                                draw_coin(player, rectangle, screen)
                                rectangles.remove(rectangle)
                                if player == 1:
                                    for key, value in position_of_rectangles.items():
                                        if value == rectangle:
                                            pos_1.append(key)
                                    player = 2
                                    pygame.display.set_caption("Joueur 2 peut jouer...")
                                    if check_if_won(pos_1):
                                        won = True
                                        pygame.display.set_caption("Joueur 1 a gagne!")
                                    elif check_draw():
                                        won = True
                                        player = 0
                                        pygame.display.set_caption("Partie remise")

                                else:
                                    for key, value in position_of_rectangles.items():
                                        if value == rectangle:
                                            pos_2.append(key)
                                    player = 1
                                    pygame.display.set_caption("Joueur 1 peut jouer...")
                                    if check_if_won(pos_2):
                                        won = True
                                        player = 2
                                        pygame.display.set_caption("Joueur 2 a gagne!")
                                    elif check_draw():
                                        won = True
                                        player = 0
                                        pygame.display.set_caption("Partie remise")

                                b = False
    else:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
    pygame.display.update()

pygame.quit()
sys.exit()
