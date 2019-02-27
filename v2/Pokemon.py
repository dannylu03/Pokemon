# https://www.youtube.com/watch?v=3UxnelT9aCo&list=PLsk-HSGFjnaGQq7ybM8Lgkh5EMxUWPm2i&index=1
# Followed the above tutorial ^^
import pygame
import sys
from os import path
from Settings import *
from Sprites import *

pygame.init()
pygame.mixer.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Sets the dimensions of the screen
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        # Allows the user to hold a key instead of repeatedly tapping them
        pygame.key.set_repeat(500, 100) # Repeats key presses at (delay in ms, the interval in ms)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def setup(self):
        # sets up the game and necessary vars
        # Creates 2 sprite groups for mass drawing so you don't have to draw each individual Sprite to the screen
        self.all_sprites = pygame.sprite.Group() # Holds all the sprites
        self.walls = pygame.sprite.Group() # Holds all the walls in the game to easily control collision and graphics
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        # Draws the tile system for player-npc interaction
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        # Draws all the graphics
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def events(self):
        # Process all events in this function
        # Ex. Movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(deltaX=-1)

                if event.key == pygame.K_RIGHT:
                    self.player.move(deltaX=1)

                if event.key == pygame.K_UP:
                    self.player.move(deltaY=-1)

                if event.key == pygame.K_DOWN:
                    self.player.move(deltaY=1)

    def intro_screen(self):
        pass

    def game_win_screen(self):
        pass

    def game_lose_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.intro_screen()
while True:
    g.setup()
    g.run()
    g.show_go_screen()
