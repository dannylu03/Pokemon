import pygame
pygame.font.init()
pygame.init()

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (40, 40, 40)
LIGHT_GREY = (211, 211, 211)
SILVER = (192, 192, 192)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
FOREST_GREEN = (34, 139, 34)
BEIGE = (253, 245, 230)
PURPLE = (128, 0, 128)
DARKER_WHITE = (230, 230, 230)
DARK_YELLOW = (197, 197, 0)
ORANGE = (255, 165, 0)

# Game Settings
display_width = 1000
display_height = 600
title = "Pokemon Remake - Final Battle"
fps = 60



small_font = pygame.font.SysFont("Consolas", 14)
font = pygame.font.SysFont("pokemon_fonts", 28)
font_moves = pygame.font.SysFont("pokemon_fonts", 34)
large_text = pygame.font.SysFont("pokemon_fonts", 52)
small_font1 = pygame.font.SysFont("Consolas", 18)