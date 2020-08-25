import pygame,sys
import numpy as np

pygame.init()

WIDTH=600
HEIGHT=600
LINE_WIDTH=15
BOARD_ROWS=3
BOARD_COLOUMN=3
CIRCLE_RADIUS=60
CIRCLE_WIDTH=15
CROSS_WIDTH=25
SPACE=55
RED=(255,0,0)
CREAM=(239,231,200)
BLACK=(0,0,0)
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

def darw_figures():
    for row in range(BOARD_ROWS):
        for coloumn in range(BOARD_COLOUMN):
            if board[row][coloumn]==1:
                pygame.draw.circle(screen,CREAM,(int(coloumn*200+100),int(row*200+100)),CIRCLE_RADIUS,CIRCLE_WIDTH )
            elif board[row][coloumn]==2:
                pygame.draw.line(screen,BLACK,(coloumn*200+SPACE,row*200+200-SPACE),(coloumn*200+200-SPACE,row*200+SPACE),CROSS_WIDTH)
                pygame.draw.line(screen,BLACK,(coloumn*200+SPACE,row*200+SPACE),(coloumn*200+200-SPACE,row*200+200-SPACE),CROSS_WIDTH)



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

def check_win(player):
    for coloumn in range(BOARD_COLOUMN):
        if board[0][coloumn]==player and board[1][coloumn]==player and board[2][coloumn]==player:
            draw_vertical_winning_line(coloumn,player)
            return True
    for row in range(BOARD_ROWS):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            draw_horizantal_winning_line(row,player)
            return True    
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        draw_asscending_diagonol(player)
        return True
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        darw_decending_diagonol(player)
        return True
    return False

def draw_vertical_winning_line(coloumn,player):
    posX=coloumn*200+100
    if player==1:
        colour=CREAM
    elif player==2:
        colour=BLACK

    pygame.draw.line(screen,colour,(posX,15),(posX,HEIGHT-15),15)

def draw_horizantal_winning_line(row,player):
    posY=row*200+100
    if player==1:
        colour=CREAM
    elif player==2:
        colour=BLACK

    pygame.draw.line(screen,colour,(15,posY),(WIDTH-15,posY),15)

def draw_asscending_diagonol(player):
    if player==1:
        colour=CREAM
    elif player==2:
        colour=BLACK

    pygame.draw.line(screen,colour,(15,HEIGHT-15),(WIDTH-15,15),15)
    

def darw_decending_diagonol(player):
    if player==1:
        colour=CREAM
    elif player==2:
        colour=BLACK

    pygame.draw.line(screen,colour,(15,15),(WIDTH-15,HEIGHT-15),15)

def restart():
    screen.fill(BACKGROUND_COLOUR)
    draw_lines()
    player=1
    for row in range(BOARD_ROWS):
        for coloumn in range(BOARD_COLOUMN):
            board[row][coloumn]=0



draw_lines()

player=1
game_over=False

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX=event.pos[0]
            mouseY=event.pos[1]

            clicked_row=int(mouseY//200)
            clicked_coloumn=int(mouseX//200)

            if available_square(clicked_row,clicked_coloumn):
                if player ==1:
                    mark_square(clicked_row,clicked_coloumn,1)
                    if check_win(player):
                        game_over=True
                    player =2
                elif player ==2:
                    mark_square(clicked_row,clicked_coloumn,2)
                    if check_win(player):
                        game_over=True
                    player =1

                darw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over=False

    pygame.display.update()        