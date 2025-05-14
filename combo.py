import pygame

import constants
from character import Character


class ComboManager:
    def __init__(self, beatTimes, combos):
        self.keys = []
        self.beatTimes = beatTimes
        self.combos = {
            'f': combos.fernet,
            'b': combos.normal,
        }

    def registerEvent(self, keyCode: int, currentTime):
        for beat in self.beatTimes:
            if abs(beat - currentTime) < constants.COMBO_TOLERANCY / 2:
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
        return str(list(map(pygame.key.name, self.keys)))


class Combos:
    def __init__(self, character: Character):
        self.character = character

    def fernet(self):
        print("fernet")
        self.character.setTexture(self.character.textures.combo_fernet)
        
    def indians(self):
        print("indiani")
        

    def normal(self):
        self.character.setTexture(self.character.textures.deault)
