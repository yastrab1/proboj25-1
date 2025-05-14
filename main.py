import pygame
import librosa
import numpy as np
import time
import threading
import character as ch
import constants
from beat import extractBeats

# --- Audio analysis (before starting pygame) ---
AUDIO_PATH = './songs/Fernet Cez Internet [AlGVdv7uD98].mp3'

beatTimes = extractBeats(AUDIO_PATH)

pygame.init()
WIDTH,HEIGHT = constants.WIDTH,constants.HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beat Visualizer")
clock = pygame.time.Clock()

BEAT_LINE_X = WIDTH // 2
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

playerTextures = ch.CharacterTextures(
    default="assets/img.png"
)

player = ch.Character(
    textures=playerTextures,
    position=(0, 0),
    scale=0.4
)

all_sprites.add(player)



# Main loop
running = True


def renderTracker(lastPressedBeat):

    for beat in beatTimes:
        dt = beat - current_time
        if 0 <= dt < 2:
            x = int(BEAT_LINE_X + (dt - 1) * 300)  # dt=1 => start edge, dt=0 => beat line
            pygame.draw.circle(screen, constants.RED, (x, HEIGHT // 2), 10)
        if -0.2 < lastPressedBeat - beat < 0.2:
            return True

    return False


while running:
    screen.fill(constants.BLACK)
    current_time = time.time() - start_time if start_time else 0

    # Draw beat line
    pygame.draw.line(screen, constants.WHITE, (BEAT_LINE_X, 0), (BEAT_LINE_X, HEIGHT), 2)

    # Draw upcoming beats as dots moving toward the beat line
    addPoints = renderTracker(pressedBeat)
    if addPoints:
        points+=1
        pressedBeat = -100
    if pressedBeat - current_time > 0.4:
        pressedBeat = -100
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            pressedBeat = current_time
            print("Pressed Beat")

    all_sprites.draw(screen)

    screen.blit(font.render("Points: " + str(points), True, constants.WHITE), (WIDTH // 2, HEIGHT // 2))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
