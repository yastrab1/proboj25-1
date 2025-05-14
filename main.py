import pygame
import time
import threading
import platform

from pygame import Vector2
import tkinter as tk
import character as ch
import constants
from beat import extractBeats, downloadYTMusic
from beatTracker import renderTracker
from character import TimedSprite
from combo import ComboManager, Combos
from healthbar import renderHealthBar
from linkDialog import SimpleApp

# Usage
os_name = platform.system()
path = ""
app = {}

if os_name == "Windows":
    app = SimpleApp()
    path = app.run()
elif os_name == "Darwin":
    path = "./songs/Fernet Cez Internet [AlGVdv7uD98].mp3"

beatTimes,bpm = extractBeats(path)

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT, SPRITES, PLAYER1_POS, PLAYER2_POS = constants.WIDTH, constants.HEIGHT, constants.SPRITES, constants.PLAYER1_POS, constants.PLAYER2_POS

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED)

bg = pygame.image.load("./assets/bg.png").convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
pygame.display.set_caption("OBOH")
clock = pygame.time.Clock()

font = pygame.font.Font("./assets/Carnevalee Freakshow.ttf", 30)  # font name, size
bigFont = pygame.font.Font("./assets/Carnevalee Freakshow.ttf", 100)  # font name, size

pygame.mixer.init()
pygame.mixer.music.load(path)

start_time = -1

def play_music():
    global start_time
    pygame.mixer.music.play()
    start_time = time.time()


threading.Thread(target=play_music).start()
points = 0
pressedBeat = -100

bountyBoard = pygame.image.load("./assets/gameEnd.png")

playerTexturesBlue = ch.CharacterTextures(
    default= "assets/player1.png",
    combo_fernet= "assets/fernet.png",
    shoot= "assets/shoot/player1.png",
    machineGun= "assets/machineGun/player1.png",
    snipe= "assets/snipe/player1.png",
    beer= "assets/beer/player1.png",
    trainManager="assets/trainManager/player1.png"
)
playerTexturesRed = ch.CharacterTextures(
    default= "assets/player2.png",
    combo_fernet= "assets/fernet.png",
    shoot= "assets/shoot/player2.png",
    machineGun= "assets/machineGun/player2.png",
    snipe= "assets/snipe/player2.png",
    beer= "assets/beer/player2.png",
    trainManager="assets/trainManager/player2.png"
)

player1 = ch.Player(
    textures=playerTexturesBlue,
    position=PLAYER1_POS,
    scale=0.4,
    first=True
)

player2 = ch.Player(
    textures=playerTexturesRed,
    position=PLAYER2_POS,
    scale=0.4,
    first=False
)

SPRITES.add(player1)
SPRITES.add(player2)

running = True
combos = Combos(player1, player2,path)
combo = ComboManager(beatTimes, combos)
combos.comboManager = combo


def showResult():
    screen.blit(bountyBoard, bountyBoard.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
    text = "Player 1 won!" if player2.health == 0 else "Player 2 won!"
    textSurface = bigFont.render(text, True, (255, 255, 255))
    screen.blit(textSurface, textSurface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
    quitSurface = font.render("Press 'q' to quit", True, (255, 255, 255))
    screen.blit(quitSurface, quitSurface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                exit(0)

def mainGame():
    screen.blit(bg, (0, 0))
    if player1.health <= 0 or player2.health <= 0:
        showResult()
        return True
    current_time = time.time() - start_time if start_time else 0
    renderHealthBar(screen, player1.health, player2.health)
    SPRITES.update()
    renderTracker(screen, beatTimes, current_time,bpm)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYUP:
            combo.registerEvent(event.key, current_time)
    SPRITES.draw(screen)
    combo1Surf = font.render("combo p1: " + "".join(combo.getKeyString(True)), True, constants.WHITE)
    combo2Surf = font.render("combo p2: " + "".join(combo.getKeyString(False)), True, constants.WHITE)
    screen.blit(combo1Surf, (constants.firstBarStartX+200, constants.barY-50))
    screen.blit(combo2Surf, (constants.secondBarStartX-500, constants.barY-50))
    return True


while running:
    running = mainGame()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
