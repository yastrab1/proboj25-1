import pygame

import constants


class ComboManager:
    def __init__(self,beatTimes):
        self.keys = []
        self.beatTimes = beatTimes
        self.combos = {
            'fernet':lambda:print("FERNET!!")
        }

    def registerEvent(self,keyCode:int,currentTime):
        for beat in self.beatTimes:
            if abs(beat - currentTime) < constants.COMBO_TOLERANCY/2:
                self.keys.append(keyCode)
                self.matchCombos()
                return
        self.breakCombo()

    def matchCombos(self):
        keyString = "".join(list(map(pygame.key.name, self.keys)))
        if keyString in self.combos.keys():
            self.combos[keyString]()
            self.breakCombo()
            return

    def breakCombo(self):
        self.keys = []

    def __str__(self):
        return str(list(map(pygame.key.name,self.keys)))