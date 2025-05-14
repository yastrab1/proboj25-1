import pygame
import time
import threading
import character as ch
import constants
from beat import extractBeats
from beatTracker import renderTracker
from combo import ComboManager

# --- Audio analysis (before starting pygame) ---
AUDIO_PATH = './songs/Fernet Cez Internet [AlGVdv7uD98].mp3'

beatTimes = extractBeats(AUDIO_PATH)

pygame.init()
WIDTH, HEIGHT = constants.WIDTH, constants.HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
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

playerTextures = ch.CharacterTextures(
    default="assets/img.png"
)

player = ch.Character(playerTextures, (0, 0))
all_sprites.add(player)

# Main loop
running = True

combo = ComboManager(beatTimes)

while running:
    screen.fill(constants.BLACK)
    current_time = time.time() - start_time if start_time else 0

    renderTracker(screen,beatTimes,current_time)
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            combo.registerEvent(event.key, current_time)

    all_sprites.draw(screen)

    screen.blit(font.render("combo: " + str(combo), True, constants.WHITE), (WIDTH // 2, HEIGHT // 2))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
