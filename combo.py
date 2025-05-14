import pygame
from numpy.ma.core import anomalies

import constants
from character import Character, CharacterTextures, TimedSprite


class ComboManager:
    def __init__(self, beatTimes, combos):
        self.keys = []
        self.beatTimes = beatTimes
        self.combos = {
            'f': combos.fernet(True),
            'b': combos.indians(True),
            'l': combos.indians(False)
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
    def __init__(self, player1,player2):
        self.player1 = player1
        self.player2 = player2

    def fernet(self, isPlayer1):
        player = self.player1 if isPlayer1 else self.player2
        def internal():
            print("fernet")
            player.setTexture(player.textures.combo_fernet)
        return internal


    def indians(self,isPlayer1):
        def internal():
            print("indiani")
            constants.indians.play()
            prechod = pygame.sprite.Sprite()
            indianPos = (0 if isPlayer1 else constants.WIDTH, 500)
            indians = TimedSprite(indianPos, 1000, "assets/indiani.png",lambda x:self.animateIndians(x,isPlayer1))
            indiansSpawnTime = pygame.time.get_ticks()
            constants.SPRITES.add(indians)
        return internal

    def animateIndians(self,sprite:TimedSprite,isPlayer1):
        sprite.rect = sprite.rect.move(20 if isPlayer1 else -20,0)