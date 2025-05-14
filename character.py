import pygame as pg

class CharacterTextures:
    def __init__(self, default, attack_default = None):
        self.deault = default
        self.attack_default = attack_default
        

class Character(pg.sprite.Sprite):
    def __init__(self, textures : CharacterTextures, position : pg.Vector2, scale = 1.0):
        super().__init__()
        self.image = pg.transform.scale_by(pg.image.load(textures.deault).convert_alpha(), scale)
        self.rect = self.image.get_rect(topleft=position)
        
    
