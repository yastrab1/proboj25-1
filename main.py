import pygame
import time
import threading

from pygame import Vector2

import character as ch
import constants
from beat import extractBeats
from beatTracker import renderTracker
from combo import ComboManager, Combos
from healthbar import renderHealthBar

# --- Audio analysis (before starting pygame) ---
AUDIO_PATH = './songs/Fernet Cez Internet [AlGVdv7uD98].mp3'

beatTimes = extractBeats(AUDIO_PATH)

pygame.init()
WIDTH, HEIGHT, SPRITES = constants.WIDTH, constants.HEIGHT, constants.SPRITES

screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("./assets/bg.png").convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
pygame.display.set_caption("Beat Visualizer")
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 30)  # font name, size

pygame.mixer.init()
pygame.mixer.music.load(AUDIO_PATH)

start_time = -1


def play_music():
    global start_time
    pygame.mixer.music.play()
    start_time = time.time()


threading.Thread(target=play_music).start()
points = 0
pressedBeat = -100

all_sprites = pygame.sprite.Group()

playerTexturesBlue = ch.CharacterTextures(
    default="assets/player1.png",
    combo_fernet="assets/fernet.png"
)
playerTexturesRed = ch.CharacterTextures(
    default="assets/player2.png",
    combo_fernet="assets/fernet.png"
)

player1 = ch.Character(
    textures=playerTexturesBlue,
    position=Vector2(0, 0),
    scale=0.4
)

player2 = ch.Character(
    textures=playerTexturesRed,
    position=Vector2(WIDTH-500, 0),
    scale=0.4
)

SPRITES.add(player1)
SPRITES.add(player2)

# Main loop
running = True

combo = ComboManager(beatTimes,Combos(player1))

while running:
    screen.blit(bg, (0, 0))
    current_time = time.time() - start_time if start_time else 0

    renderTracker(screen,beatTimes,current_time)
    renderHealthBar(screen,100,50)
    SPRITES.update()
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            combo.registerEvent(event.key, current_time)

    SPRITES.draw(screen)

    screen.blit(font.render("combo: " + str(combo), True, constants.WHITE), (WIDTH // 2, HEIGHT // 2))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
