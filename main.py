import pygame
import librosa
import numpy as np
import time
import threading

# --- Audio analysis (before starting pygame) ---
AUDIO_PATH = './songs/Fernet Cez Internet [AlGVdv7uD98].mp3'

# Load and analyze audio
y, sr = librosa.load(AUDIO_PATH)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr) + 0.1
print(beat_times)
# --- Pygame setup ---
pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beat Visualizer")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 60, 60)

# Beat line position (fixed target)
BEAT_LINE_X = WIDTH // 2
font = pygame.font.SysFont("arial", 30)  # font name, size

# Load music using pygame.mixer
pygame.mixer.init()
pygame.mixer.music.load(AUDIO_PATH)

# Shared start time variable
start_time = -1

# Start music in a thread (to avoid blocking)
def play_music():
    global start_time
    pygame.mixer.music.play()
    start_time = time.time()

threading.Thread(target=play_music).start()
points = 0
pressedBeat = False
# Main loop
running = True
while running:
    screen.fill(BLACK)
    current_time = time.time() - start_time if start_time else 0

    # Draw beat line
    pygame.draw.line(screen, WHITE, (BEAT_LINE_X, 0), (BEAT_LINE_X, HEIGHT), 2)

    # Draw upcoming beats as dots moving toward the beat line
    for beat in beat_times:
        dt = beat - current_time
        if 0 <= dt < 2:  # Show only upcoming beats within next 2 seconds
            # Linearly map dt to screen position
            x = int(BEAT_LINE_X + (dt - 1) * 300)  # dt=1 => start edge, dt=0 => beat line
            pygame.draw.circle(screen, RED, (x, HEIGHT // 2), 10)
        if pressedBeat:
            if -0.5 <dt < 0.5:
                points += 1
            pressedBeat=False
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            pressedBeat = True
            print("Pressed Beat")
    screen.blit(font.render("Points: " + str(points), True, WHITE), (WIDTH // 2, HEIGHT // 2))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
