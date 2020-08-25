import pygame,sys
import numpy as np

pygame.init()

WIDTH=600
HEIGHT=600
LINE_WIDTH=15
BOARD_ROWS=3
BOARD_COLOUMN=3
RED=(255,0,0)
BACKGROUND_COLOUR=(28,170,156)
LINE_COLOR=(23,145,135)

screen=pygame.display.set_mode( (WIDTH,HEIGHT) )
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BACKGROUND_COLOUR)

board=np.zeros((BOARD_ROWS,BOARD_COLOUMN))

def draw_lines():
    pygame.draw.line(screen,LINE_COLOR,(0,200),(600,200),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(0,400),(600,400),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(200,0),(200,600),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(400,0),(400,600),LINE_WIDTH)

def mark_square(row,coloumn,player):
    board[row][coloumn]=player

def available_square(row,coloumn):
    if board[row][coloumn]==0:
        return True
    else:
        return False

def is_board_full():
    for row in range(BOARD_ROWS):
        for coloumn in range(BOARD_COLOUMN):
            if board[row][coloumn]==0:
                return False
    return True


draw_lines()

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type==pygame.MOUSEBUTTONDOWN:





    pygame.display.update()        