import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('laserGreen.png')
        self.rect = self.image.get_rect()
        
    def update(self):
        
        #Move the bullet up 5 pixels
        self.rect.y -= 5