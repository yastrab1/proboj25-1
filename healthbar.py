import pygame

import constants
from constants import WIDTH, MAX_HEALTH, HEIGHT

firstBarStartX = 0
secondBarStartX = WIDTH - 400
barY = HEIGHT-100
barWidth = 300
barHeight = 20
def renderHealthBar(screen,health1,health2):
    firstWidth = (health1/MAX_HEALTH)*barWidth
    secondWidth = (health2/MAX_HEALTH)*barWidth

    pygame.draw.rect(screen, constants.RED, pygame.Rect(firstBarStartX, barY, firstWidth, barHeight))
    pygame.draw.rect(screen, constants.BLUE, pygame.Rect(secondBarStartX, barY, secondWidth, barHeight))