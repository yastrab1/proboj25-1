import pygame as pg

class CharacterTextures:
    def __init__(self, default, attack_default = None, combo_fernet = None):
        self.deault = default
        self.attack_default = attack_default
        self.combo_fernet = combo_fernet
        

class Character(pg.sprite.Sprite):
    def __init__(self, textures : CharacterTextures, position : pg.Vector2, scale = 1.0):
        super().__init__()
        self.textures = textures
        self.scale = scale
        self.image = pg.transform.scale_by(pg.image.load(self.textures.deault).convert_alpha(), scale)
        self.rect = self.image.get_rect(topleft=position)

    def setTexture(self,texture):
        self.image = pg.transform.scale_by(pg.image.load(texture).convert_alpha(), self.scale)
        
    def resetTexture(self):
        self.image = pg.transform.scale_by(pg.image.load(self.textures.deault).convert_alpha(), self.scale)