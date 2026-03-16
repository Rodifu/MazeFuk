import pygame

# === COLORS ===
C_WALL   = (120, 67, 21)    # brown — wall collision color
C_PATH   = (37, 177, 76)    # green — walkable color
C_WHITE  = (255, 255, 255)
C_YELLOW = (255, 220, 0)
C_BLACK  = (0, 0, 0)
C_ORANGE = (255, 128, 0)
C_RED    = (200, 30, 30)

#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

# === COLORS ===
C_WALL   = (120, 67, 21)    # brown — wall collision color
C_PATH   = (37, 177, 76)    # green — walkable color
C_WHITE  = (255, 255, 255)
C_YELLOW = (255, 220, 0)
C_BLACK  = (0, 0, 0)
C_ORANGE = (255, 128, 0)
C_RED    = (200, 30, 30)

# === WINDOW ===
WIN_WIDTH  = 616
WIN_HEIGHT = 510

# === PLAYER ===
PLAYER_SPEED = 2

PLAYER_KEY_UP    = pygame.K_UP
PLAYER_KEY_DOWN  = pygame.K_DOWN
PLAYER_KEY_LEFT  = pygame.K_LEFT
PLAYER_KEY_RIGHT = pygame.K_RIGHT

# === MENU OPTIONS ===
MENU_OPTION = (
    'START GAME',
    'RULES',
    'EXIT',
)

# === LEVELS ===
LEVEL_ORDER = ['Level1', 'Level2', 'Level3']

# === EXIT ZONES per level — multiple rects to cover the full exit area ===
LEVEL_EXITS = {
    'Level1': [
    pygame.Rect(610, 215, 11, 9),
    pygame.Rect(610, 235, 11, 9),
    pygame.Rect(610, 255, 11, 9),
    pygame.Rect(610, 275, 11, 9),
    pygame.Rect(610, 295, 11, 9),
    ],
    'Level2': [
    pygame.Rect(215, 504, 11, 9),
    pygame.Rect(235, 504, 11, 9),
    pygame.Rect(255, 504, 11, 9),
    pygame.Rect(275, 504, 11, 9),
    pygame.Rect(295, 504, 11, 9),
    ],
    'Level3': [
    pygame.Rect(0, 45, 11, 9),
    pygame.Rect(0, 55, 11, 9),
    pygame.Rect(0, 65, 11, 9),
    pygame.Rect(0, 75, 11, 9),
    pygame.Rect(0, 85, 11, 9),
    ],
}

# === PLAYER START POSITION per level ===
PLAYER_START = {
    'Level1': (590, 60),
    'Level2': (40,  65),
    'Level3': (590, 460),
}

# === LEVEL IMAGE FILES ===
LEVEL_BG = {
    'Level1': 'lvl1',
    'Level2': 'lvl2',
    'Level3': 'lvl3',
}

# === SONGS ===
MENU_SONG = './asset/menu_song.wav'
LEVEL_SONG = {
    'Level1': './asset/lvl1_song.wav',
    'Level2': './asset/lvl2_song.wav',
    'Level3': './asset/lvl3_song.mp3',
}

# === COLLISION MARGIN (pixels sampled around player edges) ===
COLLISION_MARGIN = 2