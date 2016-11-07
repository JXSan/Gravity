import pygame, random
from settings import *
from enemy import Enemy
# --- Classes --- #
        
class Player(pygame.sprite.Sprite):
    ''' This class represents the Player '''
    def __init__(self):
        # --- Call the Sprite constructor --- #
        super().__init__()
        # --- Load player image --- #
        self.image = pygame.image.load('player.png')
        # --- Get rectangle dimensions of the image --- #
        self.rect = self.image.get_rect()
        
    def update(self):
        pass

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # --- Load Laser image --- #
        self.image = pygame.image.load('laserGreen.png')
        # --- Get rectangle dimensions of the image --- #
        self.rect = self.image.get_rect()
        
        # When bullet hits enemy 
        self.hit = pygame.image.load('laserGreenShot.png')
        self.hit_rect = self.hit.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 30        
# --- Create the window --- #
 
# Initialize PyGame
pygame.init()
 
# Set the height and width of the screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
 
# --- Sprite lists --- #
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
enemy_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()

# Player List 
player_list = pygame.sprite.Group()

# --- Font --- #

font = pygame.font.SysFont(None, 30) #Font Size 25

# --- Enemy Properties --- #

enemySpawnCount = 0

# --- Create the Sprites --- #

# Spawn (4) enemies
e1 = Enemy()
all_sprites_list.add(e1)
enemy_list.add(e1)

e2 = Enemy()
all_sprites_list.add(e2)
enemy_list.add(e2)

e3 = Enemy()
all_sprites_list.add(e3)
enemy_list.add(e3)

e4 = Enemy()
all_sprites_list.add(e4)
enemy_list.add(e4)
 
# Create a Player
player = Player()
player_list.add(player)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
player.rect.y = 500

# --- Handle Player Movement --- #
x_change = 0
y_change = 0
# --- Handle Score and Lives --- #
score = 0
lives = 3

# --- Spawn Background Function --- #
def spawn_background():
    
    #Background Properties
    background = pygame.image.load('Background/backgroundColor.png')
    nebula = pygame.image.load('Background/nebula.png')
    starBackground = pygame.image.load('Background/starBackground.png')
    
    #Scale background image to 600, 600
    background = pygame.transform.scale(background, (600,600))
    screen.blit(background, [0,0])
    
    #Add Nebula Cloud
    screen.blit(nebula, [50, 100])
    screen.blit(nebula, [400, 50])
    
    #Add Star Background
    starBackground = pygame.transform.scale(starBackground, (600,600))
    screen.blit(starBackground, [0, 0])
    
# --- Spawn Enemy --- #
def spawnEnemy():
    # This represents an enemy 
    enemy = Enemy()
    
    #Set a random location for the enemy 
    enemy.rect.x = random.randrange(WIDTH-100)
    enemy.rect.y = random.randrange(-300, -100)
    
    #Add the enemy to the list of objects 
    enemy_list.add(enemy)
    all_sprites_list.add(enemy)
    
# --- Keeps score --- #
def hud(msg):
    # --- Display Score --- #
    screen_text = font.render(msg, True, WHITE)
    screen.blit(screen_text, [150, 10])
# -------- Main Program Loop ----------- #
while not done:
    # --- Event Processing - #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_change = SPEED
            if event.key == pygame.K_LEFT:
                x_change = -SPEED
            if event.key == pygame.K_UP:
                y_change = -SPEED
            if event.key == pygame.K_DOWN:
                y_change = SPEED
            if event.key == pygame.K_s:
                #Fire a bullet if the user clicks s
                bullet = Bullet()
                #Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x + 45
                bullet.rect.y = player.rect.y - 20
                #Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x_change = 0   
                y_change = 0
 
    # --- Game logic --- #
    
    # Update Player Movement
    player.rect.x += x_change
    player.rect.y += y_change
    
    # Determine if enemy hit player
    for enemy in enemy_list:
        
        # See if the enemy hit the player
        hit_player = pygame.sprite.spritecollide(player, enemy_list, False)
        
        # For every enemy that hits the player, remove from Sprite Group and lose a life
        for e in hit_player:
            enemy_list.remove(e)
            all_sprites_list.remove(e)
            # Remove one life 
            lives -= 1
            
        # If the ship goes off the screen, minus a life 
        if enemy.rect.top > HEIGHT:
            lives -= 1
 
    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit a block
        enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
 
        # For each block hit, remove the bullet, add to the score, and spawn another enemy
        for block in enemy_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            enemySpawnCount -= 1
            score += 1
            
            # For event bullet that hits a ship, spawn another  
            spawnEnemy()
            
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            
    # Call the update() method on all the sprites
    all_sprites_list.update()
            
 
    # --- Draw a frame --- #
 
    # Draw Background
    spawn_background()
 
    # Draw all the spites
    all_sprites_list.draw(screen)
    
    # Update Score 
    hud('Score: ' + str(score))
    
    # Draw amount of lives on screen 
    life = pygame.image.load('life.png')
    if lives == 3:
        screen.blit(life, [0,0])
        screen.blit(life, [45,0])
        screen.blit(life, [90,0])
    if lives == 2:
        screen.blit(life, [0, 0])
        screen.blit(life, [45,0])
    if lives == 1:
        screen.blit(life, [0,0])
    if lives == 0:
        done = True
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(60)
 
pygame.quit()