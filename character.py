import pygame as pg

class CharacterTextures:
    def __init__(self):
        self.deault = ""
        

class Character(pg.sprite.Sprite):
    def __init__(self, textures : CharacterTextures, position : pg.Vector2):
        super().__init__()
        self.image = pg.image.load(textures.deault).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        
    
