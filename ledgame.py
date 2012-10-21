#!/usr/bin/python
import sys
import pygame
import math
from pygame.locals import *
from dot import Dot
from Adafruit_8x8 import EightByEight


#setup pygame
pygame.init()

screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('LED GAME')
pygame.mouse.set_visible(1)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((5, 5, 5))


#setup the led grid
grid = EightByEight(address=0x70)


#setup the dots
dots = []
for x in range(0, 8):
    for y in range(0, 8):
        dot = Dot(pos=(x, y))
        dots.append(dot)


def drawEverything():
    screen.blit(background, (0, 0))
    #draw the dots
    for dot in dots:
        dot.draw()

    #flip the screen
    pygame.display.flip()


def findDot(clicked_pos, dots):
    x = clicked_pos[0]
    y = clicked_pos[1]
    for dot in dots:
        if math.hypot(dot.pos_x - x, dot.pos_y - y) <= dot.radius:
            return dot
    return None

def handleClick():
    pos = pygame.mouse.get_pos()
    dot = findDot(pos, dots)
    if dot:
        dot.clicked(grid)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            grid.clear()
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            handleClick()



    #update the display
    drawEverything()
