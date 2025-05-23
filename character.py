import pygame as pg
import pygame.image

import constants
from constants import clamp, MAX_HEALTH, BARREL1Pos, BARREL2Pos


class CharacterTextures:
    def __init__(self, default, attack_default = None, combo_fernet = None, shoot = None, machineGun = None,snipe = None,beer=None,trainManager=None):
        self.deault = default
        self.attack_default = attack_default
        self.shoot=shoot
        self.machineGun=machineGun
        self.snipe=snipe
        self.beer=beer
        self.trainManager=trainManager
        

class Character(pg.sprite.Sprite):
    def __init__(self, textures : CharacterTextures, position : pg.Vector2, scale = 1.0):
        super().__init__()
        self.textures = textures
        self.changeTime = 0
        self.scale = scale
        self.hasSetTimedTexture = False
        self.textureResetTime = 0
        self.image = pg.transform.scale_by(pg.image.load(self.textures.deault).convert_alpha(), scale)
        self.rect = self.image.get_rect(center=position)

    def setTexture(self,texture):
        self.image = pg.transform.scale_by(pg.image.load(texture).convert_alpha(), self.scale)
        
    def resetTexture(self):
        self.image = pg.transform.scale_by(pg.image.load(self.textures.deault).convert_alpha(), self.scale)
        self.hasSetTimedTexture = True

    def setTimedTexture(self, texture, time=1.0):
        print(texture)
        self.image = pg.transform.scale_by(pg.image.load(texture).convert_alpha(), self.scale)
        self.hasSetTimedTexture = True
        self.changeTime = time
        self.textureResetTime = pg.time.get_ticks()


    def update(self):
        current_time = pg.time.get_ticks()
        if current_time - self.textureResetTime >= self.changeTime and self.hasSetTimedTexture:
            self.resetTexture()


class Player(Character):
    def __init__(self, textures : CharacterTextures,position:pg.Vector2,scale = 1.0,first:bool = True):
        super().__init__(textures,position,scale)
        self.barrelObj = None
        self.health=100
        self.shortTermDMGScale = 1
        self.barrel = False
        self.first = first

    def addBarrel(self):
        if self.barrel:
            return
        self.barrelObj = Barrel(self.first)
        self.barrelObj.add(constants.SPRITES)
        self.barrel = True
    def removeBarrel(self):
        self.barrelObj.kill()
        self.barrel = False

    def dealDamage(self, damage):
        if self.barrel:
            self.barrel = False
            self.removeBarrel()
            return
        self.health = clamp(self.health - damage*self.shortTermDMGScale, 0, MAX_HEALTH)
        self.shortTermDMGScale = 1
        
    def increaseHealth(self, amount):
        self.health = clamp(self.health + amount, 0, MAX_HEALTH)
        
class TimedSprite(pg.sprite.Sprite):
    def __init__(self, position, lifetime_ms, image,func, scale =1.0):
        super().__init__()
        self.image = pg.transform.scale_by(pg.image.load(image).convert_alpha(), scale)
        self.rect = self.image.get_rect(center=position)
        self.spawn_time = pg.time.get_ticks()
        self.lifetime = lifetime_ms
        self.func = func

    def update(self):
        current_time = pg.time.get_ticks()
        self.func(self)
        if current_time - self.spawn_time >= self.lifetime:
            self.kill()  # Remove the sprite from all groups

class Barrel(pg.sprite.Sprite):
    def __init__(self,isPlayer1):
        super().__init__()
        self.image = pygame.image.load("assets/barrel.png")
        self.rect = self.image.get_rect(center=BARREL1Pos if isPlayer1 else BARREL2Pos)