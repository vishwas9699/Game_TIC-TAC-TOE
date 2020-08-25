import pygame,sys

pygame.init()

WIDTH=600
HEIGHT=600
LINE_WIDTH=15
RED=(255,0,0)
BACKGROUND_COLOUR=(28,170,156)
LINE_COLOR=(23,145,135)

screen=pygame.display.set_mode( (WIDTH,HEIGHT) )
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BACKGROUND_COLOUR)


def draw_lines():
    pygame.draw.line(screen,LINE_COLOR,(0,200),(600,200),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(0,400),(600,400),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(200,0),(200,600),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(400,0),(400,600),LINE_WIDTH)

draw_lines()

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()        