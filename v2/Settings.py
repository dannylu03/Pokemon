import pygame
import random

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
CYAN = (0, 255, 255)

# Game settings
WIDTH = 1024 # 16 * 64
HEIGHT = 768 # 16 * 48
FPS = 60
TITLE = 'Pokemon Remake'
BACKGROUND_COLOUR = BROWN

TILESIZE = 64
GRID_WIDTH = WIDTH / TILESIZE
GRID_HEIGHT = HEIGHT / TILESIZE

# Pokemon settings
PLAYER_SPEED = 280
CHARIZARD_HEALTH = 400
PIKACHU_HEALTH = 300

#Charizard_Moves
charizard_move_choice = random.randint(1, 5)
