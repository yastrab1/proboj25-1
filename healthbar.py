import pygame

import constants
from constants import WIDTH, MAX_HEALTH, HEIGHT

firstBarStartX = 50
secondBarStartX = WIDTH - 350
barY = HEIGHT-100
barWidth = 300
barHeight = 20
texture = pygame.image.load("assets/healthBar.png")
texture = pygame.transform.scale(texture, (WIDTH, HEIGHT))
def renderHealthBar(screen,health1,health2):
    screen.blit(texture,(0,0))
    firstWidth = (health1/MAX_HEALTH)*barWidth
    secondWidth = (health2/MAX_HEALTH)*barWidth

    pygame.draw.rect(screen, constants.RED, pygame.Rect(firstBarStartX, barY, firstWidth, barHeight))
    pygame.draw.rect(screen, constants.BLUE, pygame.Rect(secondBarStartX, barY, secondWidth, barHeight))