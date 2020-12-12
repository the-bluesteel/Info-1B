import pygame, sys
from pygame.locals import *
from pygame_functions import *
from string import ascii_uppercase

pygame.init()

done = False
SIZE_X = 420
SIZE_Y = 440
size = (SIZE_X, SIZE_Y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Player 1 can play!")


class Board:
    global SIZE_Y
    global SIZE_X

    def __init__(self):
        self.columns = []
        for i in range(7):
            c = Column(30 + 60 * i, ascii_uppercase[i])
            self.columns.append(c)
        self.moves = []  # Stores all of the moves -> One Move = [player, column]
        self.player = 1
        self.won = False
        self.moves_player_one = []
        self.moves_player_two = []

    def play(self, c):
        """
        :param player: 1 - 2
        :param pos: clicked position
        :return: True if successful, else False
        """
        if not self.won:
            if c is None or c.is_full():
                return False
            row = c.add_jeton(self.player)
            m = f"{c.get_name()}{row}"
            self.moves.append([self.player, c])
            if self.player == 1:
                self.moves_player_one.append(m)
            else:
                self.moves_player_two.append(m)

            check = self.check_outcome()
            self.switch_players()
            if check == 1:
                pygame.display.set_caption("Player 1 has won!")
                self.won = True
            elif check == 2:
                pygame.display.set_caption("Player 2 has won!")
                self.won = True
            elif check == 3:
                pygame.display.set_caption("Stalemate!")
                self.won = True

            return True
        return False

    def switch_players(self):
        self.player = 1 if self.player == 2 else 2
        pygame.display.set_caption(f"Player {self.player} can play!")

    def get_column(self, pos):
        for c in self.columns:
            if c.is_in_column(pos):
                return c
        return None

    def remove_last_move(self):
        if len(self.moves) > 0:
            player, c = self.moves[-1][0], self.moves[-1][1]
            self.moves.pop()
            row = c.remove_jeton()
            m = f"{c.get_name()}{row}"
            self.switch_players()
            if m in self.moves_player_two:
                self.moves_player_two.remove(m)
            else:
                self.moves_player_one.remove(m)
            if self.won:
                self.won = False

    def check_outcome(self):
        """
        :return: 1 - player one won, 2 - player 2 won, 3 - remise, 0 - nothing
        """
        solutions = [["A0", "B0", "C0", "D0"], ["B0", "C0", "D0", "E0"], ["C0", "D0", "E0", "F0"],
                     ["D0", "E0", "F0", "G0"],
                     ["A1", "B1", "C1", "D1"], ["B1", "C1", "D1", "E1"], ["C1", "D1", "E1", "F1"],
                     ["D1", "E1", "F1", "G1"],
                     ["A2", "B2", "C2", "D2"], ["B2", "C2", "D2", "E2"], ["C2", "D2", "E2", "F2"],
                     ["D2", "E2", "F2", "G2"],
                     ["A3", "B3", "C3", "D3"], ["B3", "C3", "D3", "E3"], ["C3", "D3", "E3", "F3"],
                     ["D3", "E3", "F3", "G3"],
                     ["A4", "B4", "C4", "D4"], ["B4", "C4", "D4", "E4"], ["C4", "D4", "E4", "F4"],
                     ["D4", "E4", "F4", "G4"],
                     ["A5", "B5", "C5", "D5"], ["B5", "C5", "D5", "E5"], ["C5", "D5", "E5", "F5"],
                     ["D5", "E5", "F5", "G5"],
                     ["A3", "B2", "C1", "D0"], ["A4", "B3", "C2", "D1"], ["B3", "C2", "D1", "E0"],
                     ["A5", "B4", "C3", "D2"],
                     ["B4", "C3", "D2", "E1"], ["C3", "D2", "E1", "F0"], ["B5", "C4", "D3", "E2"],
                     ["C4", "D3", "E2", "F1"],
                     ["D3", "E2", "F1", "G0"], ["C5", "D4", "E3", "F2"], ["D4", "E3", "F2", "G1"],
                     ["D5", "E4", "F3", "G2"],
                     ["D0", "E1", "F2", "G3"], ["C0", "D1", "E2", "F3"], ["D1", "E2", "F3", "G4"],
                     ["B0", "C1", "D2", "E3"],
                     ["C1", "D2", "E3", "F4"], ["D2", "E3", "F4", "G5"], ["A0", "B1", "C2", "D3"],
                     ["B1", "C2", "D3", "E4"],
                     ["B1", "C2", "D3", "E4"], ["C2", "D3", "E4", "F5"], ["A1", "B2", "C3", "D4"],
                     ["B2", "C3", "D4", "E5"],
                     ["A2", "B3", "C4", "D5"], ["A0", "A1", "A2", "A3"], ["A1", "A2", "A3", "A4"],
                     ["A2", "A3", "A4", "A5"],
                     ["B0", "B1", "B2", "B3"], ["B1", "B2", "B3", "B4"], ["B2", "B3", "B4", "B5"],
                     ["C0", "C1", "C2", "C3"], ["C1", "C2", "C3", "C4"], ["C2", "C3", "C4", "C5"],
                     ["D0", "D1", "D2", "D3"], ["D1", "D2", "D3", "D4"], ["D2", "D3", "D4", "D5"],
                     ["E0", "E1", "E2", "E3"], ["E1", "E2", "E3", "E4"], ["E2", "E3", "E4", "E5"],
                     ["F0", "F1", "F2", "F3"], ["F1", "F2", "F3", "F4"], ["F2", "F3", "F4", "F5"],
                     ["G0", "G1", "G2", "G3"], ["G1", "G2", "G3", "G4"], ["G2", "G3", "G4", "G5"]]
        for sol in solutions:
            if all(y in self.moves_player_one for y in sol):
                return 1
            if all(y in self.moves_player_two for y in sol):
                return 2
        if len(self.moves_player_two) + len(self.moves_player_one) >= 42:
            return 3
        return 0

    def draw_board(self, screen):
        screen.fill(Color("blue"))
        draw_rect(0, SIZE_Y - 80, 80, SIZE_X, screen, Color("white"), 0)
        # Draw circles with corresponding colors
        for c in self.columns:
            x = c.get_x()
            for row in range(6):
                color = Color("grey")
                check = c.get_row(row)
                if check is not None:
                    color = Color("yellow") if check == 1 else Color("red")
                draw_circle(x, SIZE_Y - (110 + 60 * row), screen, color, 25, 0)

        # Draw green restart button
        draw_rect(50, SIZE_Y - 60, 40, 120, screen, Color("green"), 0)
        # Draw pink restart button
        draw_rect(250, SIZE_Y - 60, 40, 120, screen, Color("pink"), 0)


class Column:
    global SIZE_Y

    def __init__(self, x, name):
        self.x = x
        self.jetons = []
        self.name = name

    def get_name(self):
        return self.name

    def is_in_column(self, pos):
        return True if self.x - 30 < pos[0] < self.x + 30 and pos[1] < SIZE_Y - 80 else False

    def is_full(self):
        return len(self.jetons) >= 6

    def add_jeton(self, player):
        self.jetons.append(player)
        return len(self.jetons) - 1

    def remove_jeton(self):
        self.jetons.pop()
        return len(self.jetons)

    def get_jetons(self):
        return reversed(self.jetons)

    def get_x(self):
        return self.x

    def get_row(self, i):
        if len(self.jetons) < i + 1:
            return None
        return self.jetons[i]


board = Board()
restart_rec = Rect(50, SIZE_Y - 60, 120, 40)
undo_move = Rect(250, SIZE_Y - 60, 120, 40)

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (True, False, False):
                # check if restart button is being pressed
                c = board.get_column(pygame.mouse.get_pos())
                if c is not None:
                    board.play(c)
                else:
                    if restart_rec.collidepoint(pygame.mouse.get_pos()):
                        board = Board()
                        pygame.display.set_caption("New Game!")
                    if undo_move.collidepoint(pygame.mouse.get_pos()):
                        board.remove_last_move()
    board.draw_board(screen)

    pygame.display.update()

pygame.quit()
sys.exit()
