import pygame

import constants
from constants import HEIGHT

y = HEIGHT-110
def renderTracker(screen, beatTimes, currentTime):
    BEAT_LINE_X = constants.WIDTH / 2
    for beat in beatTimes:
        dt = beat - currentTime
        if 0 <= dt < 2:
            x = int(BEAT_LINE_X + (dt - 1) * 300)  # dt=1 => start edge, dt=0 => beat line
            pygame.draw.circle(screen, constants.RED, (x, y), 10)
    pygame.draw.line(screen, constants.WHITE, (BEAT_LINE_X, 0), (BEAT_LINE_X, constants.HEIGHT), 2)
