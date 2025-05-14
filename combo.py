import random

import pygame
from numpy.ma.core import anomalies

import constants
from character import Character, CharacterTextures, TimedSprite, Player


class ComboManager:
    def __init__(self, beatTimes, combos):
        self.keysP1 = []
        self.keysP2 = []
        self.beatTimes = beatTimes
        self.allowedP1Keys = ["q", "w", "e", "a", "s", "d"]
        self.allowedP2Keys = ["left", "right", "up", "down", "page down", "page up"]
        self.comboObj = combos
        self.combos = {
            'w': combos.beer,
            'qweasdqwe':combos.train,
            'up': combos.beer,
            's': combos.indians,
            'down': combos.indians,
            'a': combos.jarmilka,
            'left': combos.jarmilka,
            'd': combos.shoot,
            'right': combos.shoot
        }

    def registerEvent(self, keyCode: int, currentTime):
        foundComboP1 = False
        foundComboP2 = False
        for beat in self.beatTimes:
            if abs(beat - currentTime) < constants.COMBO_TOLERANCY / 2:
                if pygame.key.name(keyCode) in self.allowedP1Keys:
                    foundComboP1 = True
                    self.keysP1.append(keyCode)
                else:
                    foundComboP2 = True
                    self.keysP2.append(keyCode)
                self.matchCombos()
                return
        if not foundComboP1:
            self.breakCombo(True)
        if not foundComboP2:
            self.breakCombo(False)

    def getKeyString(self, isPlayer1):
        keyList = self.keysP1 if isPlayer1 else self.keysP2
        return list(map(pygame.key.name, keyList))

    def matchCombos(self):
        keyStringP1 = "".join(list(map(pygame.key.name, self.keysP1)))
        keyStringP2 = "".join(list(map(pygame.key.name, self.keysP2)))

        self.checkTrain(keyStringP1)
        self.checkTrain(keyStringP2)
        print(keyStringP1)
        if keyStringP1 in self.combos.keys():
            self.combos[keyStringP1](True)
            self.breakCombo(True)

        if keyStringP2 in self.combos.keys():
            self.combos[keyStringP2](False)
            self.breakCombo(True)
        shouldClear1 = True
        shouldClear2 = True
        for keyCombo,_ in self.combos.items():
            if keyCombo.startswith(keyStringP1):
                shouldClear1 = False
            if keyCombo.startswith(keyStringP2):
                shouldClear2 = False
        if shouldClear1:
            self.breakCombo(True)
        if shouldClear2:
            self.breakCombo(False)


    def checkTrain(self, keyString):
        keyCombination = ""
        if len(keyString) >= constants.TRAIN_MUSIC_THRESHOLD:
            for keys, callback in self.combos.items():
                if callback == self.comboObj.train:
                    keyCombination = keys
            if keyCombination.startswith(keyString):
                if len(keyString) == constants.TRAIN_MUSIC_THRESHOLD:
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.pause()
                    pygame.mixer.music.load("./songs/Horkýže Slíže - Vlak [oficiálne audio] [EVTLWqCjgeE].mp3")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.set_volume(((len(keyString) - constants.TRAIN_MUSIC_THRESHOLD) * 40 + 10) / 100)

    def breakCombo(self, first: bool):
        if first:
            self.keysP1 = []
        else:
            self.keysP2 = []


class Combos:
    def __init__(self, player1: Player, player2: Player, bgAudioPath):
        self.player1 = player1
        self.player2 = player2
        self.bgAudioPath = bgAudioPath

    def fernet(self, isPlayer1):
        player = self.player1 if isPlayer1 else self.player2

        print("fernet")
        player.setTimedTexture(player.textures.combo_fernet, 500.0)

    def indians(self, isPlayer1):
        print("indiani")
        constants.indians.play()
        indianPos = (0 if isPlayer1 else constants.WIDTH, 500)
        indians = TimedSprite(indianPos, 1000, "assets/indiani.png", lambda x: self.moveOnScreen(x, isPlayer1))
        constants.SPRITES.add(indians)
        if (isPlayer1):
            self.player2.dealDamage(50)
        else:
            self.player1.dealDamage(50)

    def jarmilka(self, isPlayer1):
        print("jarmilka")
        constants.jarmilka_moan.play()
        jarmilkaPos = ()
        curtainPos = ()
        if isPlayer1:
            jarmilkaPos = pygame.Vector2(constants.WIDTH * 0.3, constants.HEIGHT * 0.35),
            curtainPos = constants.PLAYER1_POS
            self.player1.increaseHealth(constants.BEER_HEAL*3)
        else:
            jarmilkaPos = pygame.Vector2(constants.WIDTH * 0.7, constants.HEIGHT * 0.35),
            curtainPos = constants.PLAYER2_POS
            self.player2.increaseHealth(constants.BEER_HEAL*3)
        curtain = TimedSprite(curtainPos, 700, "assets/zaclony.png",lambda x:self.aPass(), scale=0.5)
        jarmilka = TimedSprite(jarmilkaPos, 1100, "assets/jarmilka.png",lambda x:self.aPass(), scale=0.3)
        self.player2.health += 10
        curtain = TimedSprite(curtainPos, 700, "assets/zaclony.png", lambda x: self.aPass(), scale=0.5)
        jarmilka = TimedSprite(jarmilkaPos, 1100, "assets/jarmilka.png", lambda x: self.aPass(), scale=0.3)
        constants.SPRITES.add(jarmilka)
        constants.SPRITES.add(curtain)

    def shoot(self, isPlayer1):
        print("shooting")
        if random.randint(1, 2) == 1:
            return
        player = self.player1 if isPlayer1 else self.player2
        otherPlayer = self.player2 if isPlayer1 else self.player1
        player.setTimedTexture(player.textures.shoot, 500)
        otherPlayer.dealDamage(constants.BULLET_DMG)
        # TODO animate bullet

    def snipe(self, isPlayer1):
        player = self.player1 if isPlayer1 else self.player2
        otherPlayer = self.player2 if isPlayer1 else self.player1
        player.setTexture(player.textures.shoot)
        otherPlayer.dealDamage(constants.BULLET_DMG)
        #TODO animate bullet


    def beer(self, isPlayer1):
        print("beer")
        player = self.player1 if isPlayer1 else self.player2
        player.setTimedTexture(player.textures.beer, 200)
        player.increaseHealth(constants.BEER_HEAL)
        print(player.health)

    def machineGun(self, isPlayer1):
        print("machine gun")
        player = self.player1 if isPlayer1 else self.player2
        otherPlayer = self.player2 if isPlayer1 else self.player1

        player.setTimedTexture(player.textures.machineGun,1000)
        otherPlayer.health -= constants.MACHINE_DMG

    def smoke(self, isPlayer1):
        print("smoke")
        player = self.player1 if isPlayer1 else self.player2
        player.shortTermDMGScale = 0.8

    def train(self, isPlayer1):
        print("train")
        player = self.player1 if isPlayer1 else self.player2
        otherPlayer = self.player2 if isPlayer1 else self.player1

        indianPos = (0 if isPlayer1 else constants.WIDTH, 500)
        indians = TimedSprite(indianPos, 1000, "assets/train.png", lambda x: self.moveOnScreen(x, isPlayer1))
        constants.SPRITES.add(indians)
        if (isPlayer1):
            self.player2.dealDamage(constants.MAX_HEALTH)
        else:
            self.player1.dealDamage(constants.MAX_HEALTH)
        pygame.mixer.stop()
        pygame.mixer.music.load(self.bgAudioPath)
        pygame.mixer.music.play()

    # animations
    def moveOnScreen(self, sprite: TimedSprite, isPlayer1):
        sprite.rect = sprite.rect.move(20 if isPlayer1 else -20, 0)

    def aPass(self):
        pass
