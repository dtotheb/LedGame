#!/usr/bin/python
import sys
import pygame
import math
from pygame.locals import *
from dot import Dot
from Adafruit_8x8 import EightByEight
from Button import Button


#setup pygame
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((440, 500), 0, 32)
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

#setup the button
buttons = []
printButton = Button('Print', pos=(40, 450))
buttons.append(printButton)



def drawEverything():
    """
    draws Everything
    """
    screen.blit(background, (0, 0))
    #draw the dots
    for dot in dots:
        dot.draw()

    #draw the buttons
    for button in buttons:
        button.draw(screen)

    #flip the screen
    pygame.display.flip()


def findDot(clicked_pos, dots):
    """
    Looks through the list of dots
    and checks if pos is in one of them
    """
    x = clicked_pos[0]
    y = clicked_pos[1]
    for dot in dots:
        if math.hypot(dot.pos_x - x, dot.pos_y - y) <= dot.radius:
            return dot
    return None


def handleClick():
    """
    handles the Mouse click
    """
    pos = pygame.mouse.get_pos()
    dot = findDot(pos, dots)
    if dot:
        dot.clicked(grid)
    for butt in buttons:
        if butt.rect.collidepoint(pos):
            printDotPoints(dots)


def printDotPoints(dots):
    """
    Prints out the points for all the lit dots
    """
    points = []
    for dot in dots:
        if dot.lit:
            points.append(dot.pos)
    print points

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            grid.clear()
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                printDotPoints(dots)

        if event.type == MOUSEBUTTONDOWN:
            handleClick()

    #update the display
    drawEverything()
