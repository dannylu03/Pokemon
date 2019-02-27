import pygame
from Settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, deltaX=0, deltaY=0):
        # If the player is going to collide with a wall, set deltaX and deltaY to 0 (Prevents Movement)
        if not self.collide_with_walls(deltaX, deltaY):
            self.x += deltaX
            self.y += deltaY

    def collide_with_walls(self, deltaX=0, deltaY=0):
        for wall in self.game.walls:
            # If the x coord == the player's x cord + 1 (deltaX) and likewise for the y cords, then return True
            if wall.x == self.x + deltaX and wall.y == self.y + deltaY:
                return True
        return False # If there's no wall blocking the player, return False for collision with wall

    def update(self):
        # Sets the player size to exactly ONE tile
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
