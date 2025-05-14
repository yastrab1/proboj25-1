import pygame.display
pygame.init()
_info = pygame.display.Info()
WIDTH, HEIGHT = _info.current_w, _info.current_h

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 60, 60)

COMBO_TOLERANCY = 0.4