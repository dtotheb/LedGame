#!/usr/bin/python
import sys
import pygame
from pygame.locals import *
from dot import Dot


#setup pygame
pygame.init()

screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('LED GAME')
pygame.mouse.set_visible(1)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))


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


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

    #update the display
    drawEverything()
