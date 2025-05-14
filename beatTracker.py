import math

import pygame

import constants
from constants import HEIGHT

import math

def pulse_scale(current_time, bpm, base_scale=1.0, pop_scale=1.5, sharpness=20):
    beat_interval = 60 / bpm
    time_since_last_beat = current_time % beat_interval

    # Center time around the beat
    time_from_beat = time_since_last_beat - beat_interval / 2

    # Gaussian pulse centered at 0 (the beat)
    pulse = math.exp(-sharpness * time_from_beat ** 2)

    return base_scale + (pop_scale - base_scale) * pulse



y = HEIGHT-110
lineTop = y-100
def renderTracker(screen, beatTimes, currentTime,bpm):
    BEAT_LINE_X = constants.WIDTH / 2
    closestBeat = calculateClosest(beatTimes,currentTime)
    print(closestBeat)
    scale = pulse_scale(currentTime, bpm)*20
    for beat in beatTimes:
        dt = beat - currentTime
        if 0 <= dt < 2:
            x = int(BEAT_LINE_X + (dt - 1) * 300)  # dt=1 => start edge, dt=0 => beat line
            pygame.draw.circle(screen, constants.PURPLE, (x, y), scale)
    pygame.draw.line(screen, constants.WHITE, (BEAT_LINE_X, lineTop), (BEAT_LINE_X, constants.HEIGHT), 2)
def calculateClosest(beatTimes,currentTime):
    beatOffset = list(map(lambda beat: abs(beat - currentTime), beatTimes))
    return min(beatOffset)