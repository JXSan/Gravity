import pygame, time
from settings import *

pygame.init
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

done = False

while not done:
    # --- Handle Events --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.mouse.get_pressed():
            print(pygame.mouse.get_pos)
    
    
    # --- Handle Logic --- #
    
    
    # --- Handle Drawing to the Screen --- #
    background = pygame.image.load('Background/backgroundColor.png')
    
    #Scale background image to 600, 600
    background = pygame.transform.scale(background, (600,600))
    screen.blit(background, [0,0])
    

    
    
    # --- Handle Updating the Screen --- #
    pygame.display.update()
    
# --- Quit Game --- #
pygame.quit()
