import pygame as pg

class Character:
    def __init__(self, image_path, position : pg.Vector2):
        super().__init__()
        self.image = pg.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
