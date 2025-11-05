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

BOARD = Board()
clear_button_rect = pygame.Rect(300, 50, 200, 75)
mode_button_rect = pygame.Rect(575, 50, 175, 75)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))
    BOARD.draw_board(screen)

    # drawing reset button
    clear_board_button = pygame.draw.rect(screen, (255, 0, 0), clear_button_rect)
    text_reset = font.render("Reset", True, (255, 255, 255))
    text_reset_rect = text_reset.get_rect()
    text_reset_rect.center = (400, 90)
    screen.blit(text_reset, text_reset_rect)

    pygame.display.flip()