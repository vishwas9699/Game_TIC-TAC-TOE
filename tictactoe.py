import pygame,sys

pygame.init()

WIDTH=600
HEIGHT=600
RED=(255,0,0)

screen=pygame.display.set_mode( (WIDTH,HEIGHT) )
pygame.display.set_caption('TIC TAC TOE')
screen.fill(RED)

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()        