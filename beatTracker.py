import math

import pygame

import constants
from constants import HEIGHT

import math

import math

def beat_pulse_scale(closeness, max_scale=2, min_scale=0.8, sharpness=50):
    """
    Returns a scale factor for a dot based on its closeness to the next beat.

    Parameters:
    - closeness: float, where 0 means perfectly on the beat.
    - max_scale: float, the maximum scale when closeness is 0.
    - min_scale: float, the minimum scale value (far from beat).
    - sharpness: float, controls how fast the scale falls off from the peak.

    Returns:
    - scale: float
    """
    # Use a Gaussian-like falloff centered at 0
    scale = 1
    return scale


y = HEIGHT-110
lineTop = y-100
def renderTracker(screen, beatTimes, currentTime,bpm):
    BEAT_LINE_X = constants.WIDTH / 2
    closestBeat = calculateClosest(beatTimes,currentTime)
    scale = beat_pulse_scale(closestBeat)*20
    for beat in beatTimes:
        dt = beat - currentTime
        if 0 <= dt < 2:
            x = int(BEAT_LINE_X + (dt - 1) * 300)  # dt=1 => start edge, dt=0 => beat line
            pygame.draw.circle(screen, constants.PURPLE, (x, y), scale)
    pygame.draw.line(screen, constants.WHITE, (BEAT_LINE_X, lineTop), (BEAT_LINE_X, constants.HEIGHT), 2)
def calculateClosest(beatTimes,currentTime):
    beatOffset = list(filter(lambda x:x>=0,map(lambda beat: beat - currentTime, beatTimes)))
    return min(beatOffset)