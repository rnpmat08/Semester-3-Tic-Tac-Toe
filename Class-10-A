import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))

font = pygame.font.Font("freesansbold.ttf", 50)
small_font = pygame.font.Font("freesansbold.ttf", 20)
text_x = font.render("X", True, (255, 255, 255))
text_o = font.render("O", True, (255, 255, 255))

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Board:
    def __init__(self):
        self.board_values = [["0", "0", "0"],
                             ["0", "0", "0"],
                             ["0", "0", "0"]]
        self.current_move = "X"
        self.squares = [
                        # row 1
                        pygame.Rect(200, 200, 133, 133),
                        pygame.Rect(333, 200, 134, 133),
                        pygame.Rect(467, 200, 133, 133),

                        # row 2
                        pygame.Rect(200, 333, 133, 133),
                        pygame.Rect(333, 333, 134, 133),
                        pygame.Rect(467, 333, 133, 133),

                        # row 3
                        pygame.Rect(200, 467, 133, 133),
                        pygame.Rect(333, 467, 134, 133),
                        pygame.Rect(467, 467, 133, 133),

                        ]
        self.game_over = False
        self.alternate_computer_move_value = False
        self.generate_computer_moves = False

    def draw_board(self, surface):
        white = (255, 255, 255)
        pygame.draw.line(surface, white,
                         (200 + 133, 200), (200 + 133, 600))
        pygame.draw.line(surface, white,
                         (200 + 133 + 134, 200), (200 + 133 + 134, 600))
        pygame.draw.line(surface, white,
                         (200, 200 + 133), (600, 200 + 133))
        pygame.draw.line(surface, white,
                         (200, 200 + 133 + 134), (600, 200 + 133 + 134))

    def clicked_on_box(self, coordinate):
        if self.game_over:
            return
        mouse = pygame.Rect(coordinate.x, coordinate.y, 1, 1)
        collided = mouse.collidelist(self.squares)
        if collided == -1:
            return
        else:
            x, y = self.collided_to_xy(collided)
            if self.is_empty_square(x, y):
                self.place_marker(x, y)
            else:
                return

    def collided_to_xy(self, collided):
        x = collided % 3
        y = collided // 3
        return x, y

    def is_empty_square(self, x, y):
        return self.board_values[x][y] == "0"

    def switch_move(self):
        if self.current_move == "X":
            self.current_move = "O"
        else:
            self.current_move = "X"

    def place_marker(self, x, y):
        self.board_values[x][y] = self.current_move
        self.switch_move()
        if self.alternate_computer_move_value:
            self.generate_computer_moves = not self.generate_computer_moves

    def clear_board(self):
        self.board_values = [["0", "0", "0"],
                             ["0", "0", "0"],
                             ["0", "0", "0"]]
        self.game_over = False
        self.current_move = "X"
        self.generate_computer_moves = False

    def draw_value(self, surface, collided):
        rect = self.squares[collided]
        x, y = self.collided_to_xy(collided)

        if self.board_values[x][y] == "X":
            text_rect = text_x.get_rect()
            text_rect.center = (rect.x + rect.w // 2, rect.y + rect.h // 2)
            surface.blit(text_x, text_rect)
        elif self.board_values[x][y] == "O":
            text_rect = text_o.get_rect()
            text_rect.center = (rect.x + rect.w // 2, rect.y + rect.h // 2)
            surface.blit(text_o, text_rect)

    def all_same(self, line):
        marker = line[0]
        if marker == "0":
            return False
        for i in range(3):
            if line[i] != marker:
                return False
        return True

    def get_col(self, c):
        col = []
        for i in range(3):
            col.append(self.board_values[i][c])
        return col

    def get_diag(self):
        diag1 = []
        diag2 = []
        for i in range(3):
            diag1.append(self.board_values[i][i])
            diag2.append(self.board_values[i][2 - i])
        return diag1, diag2

    def check_win(self):
        # checking rows
        for i in self.board_values:
            if self.all_same(i):
                self.game_over = True
                return i[0]

        # checking columns
        for i in range(3):
            col = self.get_col(i)
            if self.all_same(col):
                self.game_over = True
                return col[0]

        # checking diagonals
        diag1, diag2 = self.get_diag()
        if self.all_same(diag1):
            self.game_over = True
            return diag1[0]
        elif self.all_same(diag2):
            self.game_over = True
            return diag2[0]

        # check for tie
        available_space = False
        for i in range(3):
            for j in range(3):
                if self.board_values[i][j] == "0":
                    available_space = True
        if available_space:
            return None
        else:
            self.game_over = True
            return "Tie"

    def generate_computer_move(self):
        if self.game_over:
            return
        while True:
            random_square = random.randint(0, 8)
            x, y = self.collided_to_xy(random_square)
            if self.is_empty_square(x, y):
                self.place_marker(x, y)
                return

BOARD = Board()
clear_button_rect = pygame.Rect(300, 50, 200, 75)
mode_button_rect = pygame.Rect(575, 50, 175, 75)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            BOARD.clicked_on_box(Coordinate(x, y))
            if clear_button_rect.collidepoint(x, y):
                BOARD.clear_board()
            elif mode_button_rect.collidepoint(x, y) and BOARD.current_move == "X":
                BOARD.alternate_computer_move_value = not BOARD.alternate_computer_move_value

    screen.fill((0, 0, 0))
    BOARD.draw_board(screen)

    # drawing reset button
    clear_board_button = pygame.draw.rect(screen, (255, 0, 0), clear_button_rect)
    text_reset = font.render("Reset", True, (255, 255, 255))
    text_reset_rect = text_reset.get_rect()
    text_reset_rect.center = (400, 90)
    screen.blit(text_reset, text_reset_rect)

    # rendering "current move" text
    text_move = small_font.render(f"Current move: {BOARD.current_move}", True,
                                  (255, 255, 255))  # initialize text object
    text_move_rect = text_move.get_rect()  # initialize text rectangle object
    text_move_rect.center = (100, 100)  # center rect at 100,100
    screen.blit(text_move, text_move_rect)  # add changes to the screen

    # drawing change mode button
    mode_change_button = pygame.draw.rect(screen, (0, 255, 0), mode_button_rect)
    text_change_mode = small_font.render("Change Mode", True, (255, 255, 255))
    text_change_mode_rect = text_change_mode.get_rect()
    text_change_mode_rect.center = ((575 + 575 + 175) // 2, (50 + 50 + 75) // 2)
    screen.blit(text_change_mode, text_change_mode_rect)

    # rendering "current mode" text
    status = ""
    if BOARD.alternate_computer_move_value:
        status = "Singleplayer"
    else:
        status = "Multiplayer"

    text_mode = small_font.render(f"Current Mode: {status}", True, (255, 255, 255))
    text_mode_rect = text_mode.get_rect()
    text_mode_rect.center = (400, 700)
    screen.blit(text_mode, text_mode_rect)

    # checking for a winner
    winner = BOARD.check_win()
    text_winner = small_font.render("Winner: ", True, (255, 255, 255))
    if winner is not None:
        text_winner = small_font.render(f"Winner: {winner}", True, (255, 255, 255))
    text_winner_rect = text_winner.get_rect()
    text_winner_rect.center = (100, 135)
    screen.blit(text_winner, text_winner_rect)

    if BOARD.generate_computer_moves:
        BOARD.generate_computer_move()

    # drawing markers onto the screen
    for i in range(9):
        BOARD.draw_value(screen, i)

    pygame.display.flip()
