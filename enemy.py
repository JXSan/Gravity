import pygame, random
from settings import *

class Enemy(pygame.sprite.Sprite):
    ''' This class represents the Enemy Space Ship '''
    def __init__(self):
        # --- Call the Sprite constructor --- #
        super().__init__()
        # --- Load enemy image --- #
        self.image = pygame.image.load('enemyShip.png')
        # --- Get rectangle dimensions of the image --- #
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH-100)
        self.rect.y = random.randrange(-250, -150)
        
    def update(self):
        self.rect.y += ENEMY_SPEED
        
        if self.rect.top > WIDTH + 10:
                #Set a random location for the enemy 
                self.rect.x = random.randrange(0, WIDTH-100)
                self.rect.y = random.randrange(-250, -150)
