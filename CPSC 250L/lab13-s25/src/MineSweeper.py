import pygame
import math
from pygame.locals import *
import random
import time

class MineSweeper:
    def __init__(self):
        self.screen_size = (600,500)


        # Initialize PyGame
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Mine Sweeper")

        #Colors
        self.lg = (46,171,108)
        self.b = (0,0,0)
        self.w = (255,255,255)
        self.dg = (46,155,108)

        self.button1_rect = pygame.Rect(20, 30, 80, 40)
        self.button2_rect = pygame.Rect(120, 30, 80, 40)

        self.running = True


    def draw_top_bar(self):
        # Draw black top bar
        pygame.draw.rect(self.screen, (32,128,64), (0, 0, self.screen_size[0], 100))

        # Draw buttons
        pygame.draw.rect(self.screen, self.w, self.button1_rect)
        pygame.draw.rect(self.screen, self.w, self.button2_rect)

        # Draw text on buttons
        font = pygame.font.SysFont(None, 24)
        label1 = font.render("Reset", True, self.b)
        label2 = font.render("Quit", True, self.b)
        self.screen.blit(label1, label1.get_rect(center=self.button1_rect.center))
        self.screen.blit(label2, label2.get_rect(center=self.button2_rect.center))

        # Title
        title_font = pygame.font.SysFont(None, 30)
        title = title_font.render("Minesweeper", True, self.w)
        self.screen.blit(title, (240, 35))

    def draw_game_board(self, board):
        rows = len(board)
        cols = len(board[0])
        cell_size = 25
        offset_y = 100  # leave space for top bar

        font = pygame.font.SysFont(None, 20)

        for row in range(rows):
            for col in range(cols):
                cell = board[row][col]
                color = cell['color']
                rect = pygame.Rect(col * cell_size, offset_y + row * cell_size, cell_size, cell_size)
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, self.b, rect, 1)  # border

                if cell['revealed'] and not cell['mine'] and cell['adjacent'] > 0:
                    text = font.render(str(cell['adjacent']), True, self.b)
                    text_rect = text.get_rect(center=rect.center)
                    self.screen.blit(text, text_rect)

    def cell(self, color):
        return {
            'og_color': color,
            'color': color,
            'mine': False, #Is/isn't a mine
            'revealed': False, #Is/isn't clicked
            'flagged': False, #Is cell flagged, if so then it cannot be clicked
            'adjacent': 0 #Num of adjacent mines
        }

    def gameboard(self):
        """
        24x16 game board with boxes
        """
        total_mines = 0
        row_mines = 0
        board = []
        temp = []
        other = 0
        for i in range(16):
            for j in range(24):
                if other%2 == 0:
                    color = self.lg
                else:
                    color = self.dg
                other += 1
                current = self.cell(color)
                row_max = random.randint(6,12)
                if total_mines <= 144 and row_mines <= row_max:
                    if row_max/2 >= row_mines:
                        rando = random.randint(0,1)
                        if rando % 2 == 0:
                            current['mine'] = True
                            print(i, j, ": Mine Location")
                            total_mines += 1
                            row_mines += 1
                temp.append(current)
            board.append(temp.copy())
            temp.clear()
            row_mines = 0
            other += 1
        for y in range(len(board)):
            for x in range(len(board[0])):
                board[y][x]['adjacent'] = self.check_adjacent(y, x, board)
        return board

    def check_adjacent(self, row, col, board):
        # Define directions once globally or inside the class
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      ( 0, -1),          ( 0, 1),
                      ( 1, -1), ( 1, 0), ( 1, 1)]

        ROWS = len(board)
        COLS = len(board[0])
        count = 0

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < ROWS and 0 <= c < COLS:
                if board[r][c]['mine']:
                    count += 1
        return count

    def reveal_connected_empty_cells(self, row, col, board):
        if not (0 <= row < len(board)) or not (0 <= col < len(board[0])):
            return  # out of bounds

        cell = board[row][col]
        if cell['revealed'] or cell['mine']:
            return  # already revealed or it's a mine

        cell['revealed'] = True
        cell['color'] = (200, 200, 200)

        if cell['adjacent'] > 0:
            return  # stop if the cell has adjacent mines

        # recurse into all 8 directions
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for dr, dc in directions:
            self.reveal_connected_empty_cells(row + dr, col + dc, board)

    def run(self):
        clock = pygame.time.Clock()
        board = self.gameboard()
        self.running = True
        x,y = pygame.mouse.get_pos()

        while self.running:
            for event in pygame.event.get():
                #Button Presses
                if self.button1_rect.collidepoint(x, y):
                    print("Reset button clicked")
                    board = self.gameboard()  # Resets the board

                elif self.button2_rect.collidepoint(x, y):
                    print("Quit button clicked")
                    self.running = False
                    pygame.quit()


                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.button)
                    if event.button == 1:
                        x, y = pygame.mouse.get_pos()
                        if y > 100:  # Ignore clicks on top bar
                            cell_size = 25
                            col = x // cell_size
                            row = (y - 100) // cell_size

                            # Check if the click is within the bounds of the board
                            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                                clicked_cell = board[row][col]
                                print(clicked_cell, " | ",  row, " | ",  col)
                                if not clicked_cell['flagged']:
                                    # clicked_cell['revealed'] = True
                                    clicked_cell['color'] = (200, 200, 200)  # change color to show it’s revealed
                                    if clicked_cell['mine']:
                                        print("💥 You clicked on a mine!")
                                        for ROW in board:
                                            for cell in ROW:
                                                if cell['mine']:
                                                    cell['color'] = self.b
                                    else:
                                        self.reveal_connected_empty_cells(row,col,board)
                    elif event.button == 3:
                        x, y = pygame.mouse.get_pos()
                        if y > 100:  # Ignore clicks on top bar
                            cell_size = 25
                            col = x // cell_size
                            row = (y - 100) // cell_size
                            clicked_cell = board[row][col]

                            if not clicked_cell['flagged']:
                                clicked_cell['flagged'] = True
                                clicked_cell['color'] = (128, 64, 64)
                            else:
                                clicked_cell['flagged'] = False
                                clicked_cell['color'] = clicked_cell['og_color']
                            print("Color Changed")


            self.screen.fill((200, 200, 200))  # clear screen
            self.draw_top_bar()
            self.draw_game_board(board)
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = MineSweeper()
    game.run()


