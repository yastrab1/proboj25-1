import pygame
from numpy.ma.core import anomalies

import constants
from character import Character, CharacterTextures, TimedSprite, Player


class ComboManager:
    def __init__(self, beatTimes, combos):
        self.keysP1 = []
        self.keysP2 = []
        self.beatTimes = beatTimes
        self.allowedP1Keys = ["q","w","e","a","s","d"]
        self.allowedP2Keys = ["left","right","up","down","page down","page up"]
        self.combos = {
            'w': combos.fernet,
            's': combos.indians,
            'up': combos.indians,
            'a': combos.jarmilka,
            'left': combos.jarmilka
        }
    def registerEvent(self, keyCode: int, currentTime):
        for beat in self.beatTimes:
            if abs(beat - currentTime) < constants.COMBO_TOLERANCY / 2:
                if pygame.key.name(keyCode) in self.allowedP1Keys:
                    self.keysP1.append(keyCode)
                else:
                    self.keysP2.append(keyCode)
                self.matchCombos()
                return
        self.breakCombo(True)
        self.breakCombo(False)

    def matchCombos(self):
        keyStringP1 = "".join(list(map(pygame.key.name, self.keysP1)))
        keyStringP2 = "".join(list(map(pygame.key.name, self.keysP2)))
        print(keyStringP1)
        if keyStringP1 in self.combos.keys():
            self.combos[keyStringP1](True)
            self.breakCombo(True)
        if keyStringP2 in self.combos.keys():
            self.combos[keyStringP2](False)
            self.breakCombo(False)

    def breakCombo(self,first:bool):
        if first:
            self.keysP1 = []
        else:
            self.keysP2 = []

    def __str__(self):
        return str(list(map(pygame.key.name, self.keysP1)))


class Combos:
    def __init__(self, player1:Player,player2:Player):
        self.player1 = player1
        self.player2 = player2

    def fernet(self, isPlayer1):
        player = self.player1 if isPlayer1 else self.player2

        print("fernet")
        player.setTexture(player.textures.combo_fernet)


    def indians(self,isPlayer1):
        print("indiani")
        constants.indians.play()
        indianPos = (0 if isPlayer1 else constants.WIDTH, 500)
        indians = TimedSprite(indianPos, 1000, "assets/indiani.png",lambda x:self.animateIndians(x,isPlayer1))
        constants.SPRITES.add(indians)
        if (isPlayer1):
            self.player2.health -= 50
        else:
            self.player1.health -= 50


    def jarmilka(self, isPlayer1):
        print("jarmilka")
        constants.jarmilka_moan.play()
        jarmilkaPos = ()
        if isPlayer1:
            jarmilkaPos = pygame.Vector2(constants.WIDTH*0.3, constants.HEIGHT*0.35),
            self.player1.health += 10
        else:
            jarmilkaPos = pygame.Vector2(constants.WIDTH*0.7, constants.HEIGHT*0.35),
            self.player2.health += 10
        jarmilka = TimedSprite(jarmilkaPos, 1000, "assets/jarmilka.png",lambda x:self.aPass(), scale=0.3)
        constants.SPRITES.add(jarmilka)
        
    
    #animations
    
    def animateIndians(self,sprite:TimedSprite,isPlayer1):
        sprite.rect = sprite.rect.move(20 if isPlayer1 else -20,0)
        
    def aPass(self):
        pass