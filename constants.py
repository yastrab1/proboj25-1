import pygame
pygame.init()
_info = pygame.display.Info()
WIDTH, HEIGHT = _info.current_w, _info.current_h

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 60, 60)
BLUE = (0, 0, 255)
PURPLE = (191, 0, 185)
COMBO_TOLERANCY = 0.4

MAX_HEALTH = 100
BULLET_DMG = 5
MACHINE_DMG = 15
BEER_HEAL = 10

TRAIN_MUSIC_THRESHOLD = 4

SPRITES = pygame.sprite.Group()

PLAYER1_POS = pygame.Vector2(WIDTH * 0.2, HEIGHT * 0.35)
PLAYER2_POS = pygame.Vector2(WIDTH * 0.8, HEIGHT * 0.35)

# Sound Effects

indians = pygame.mixer.Sound("assets/sounds/indian_attack.mp3")  # Supported formats: WAV, OGG, MP3
jarmilka_moan = pygame.mixer.Sound("assets/sounds/jarmilka.mp3")
beng = pygame.mixer.Sound("assets/sounds/beng.mp3")
bengLong = pygame.mixer.Sound("assets/sounds/bengDlhe.mp3")
firstBarStartX = 50
secondBarStartX = WIDTH - 50
barY = HEIGHT - 100
barWidth = 400
barHeight = 20

def clamp(value, min, max):
    return min if value < min else (max if value > max else (value))
