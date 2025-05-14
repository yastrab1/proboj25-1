import pygame

import constants
from constants import WIDTH, MAX_HEALTH, HEIGHT, firstBarStartX, secondBarStartX, barY, barWidth, barHeight

texture = pygame.image.load("assets/healthBar.png")
texture = pygame.transform.scale(texture, (WIDTH, HEIGHT))
def renderHealthBar(screen,health1,health2):
    screen.blit(texture,(0,0))
    firstWidth = (health1/MAX_HEALTH) * barWidth
    secondWidth = (health2/MAX_HEALTH) * barWidth

    pygame.draw.rect(screen, constants.RED, pygame.Rect(firstBarStartX, barY, firstWidth, barHeight))
    pygame.draw.rect(screen, constants.BLUE, pygame.Rect(secondBarStartX, barY, secondWidth, barHeight))