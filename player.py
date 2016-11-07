import pygame, random 
from settings import *
from main import *

class Player(pygame.sprite.Sprite):
    def __init(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.player = pygame.image.load('player.png')
        #self.player_left = pygame.image.load('playerLeft.png')
        #self.player_right = pygame.image.load('playerRight.png')
        
        self.player_rect = self.player.get_rect()
        #self.player_left_rect = self.player_left.get_rect()
        #self.player_right_rect = self.player_right.get_rect()
        
    def update(self):
            self.x_change = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction = 'right'
                    self.x_change = SPEED
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    self.x_change = -SPEED
                    
            self.rect.x += self.x_change