import pygame

import constants


class ComboManager:
    def __init__(self,beatTimes):
        self.keys = []
        self.beatTimes = beatTimes

    def registerEvent(self,keyCode:int,currentTime):
        for beat in self.beatTimes:
            if abs(beat - currentTime) < constants.COMBO_TOLERANCY/2:
                self.keys.append(keyCode)
                return
        self.breakCombo()

    def breakCombo(self):
        self.keys = []

    def __str__(self):
        return str(list(map(pygame.key.name,self.keys)))