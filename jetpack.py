import pygame
from pygame import image

# Initialize pygame
pygame.init()

# Intialize screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set for background
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Draw background
bg_x_1 = 0
bg_x_2 = background.get_width()
bg_y = 0

# Setting up the girlgun
girlgun_x = 500
girlgun_y = 500

girlgun = pygame.image.load('girlgun.png')
girlgun = pygame.transform.scale(girlgun, (200,200))
girlgun_x = 100
girlgun_y = SCREEN_HEIGHT / 2.5 

print(girlgun.get_width())
print(girlgun.get_height())

# Manage fps
clock = pygame.time.Clock()
fps = 60

# Speed of background
speed = 1.5
game_loop = True

# Setting up bullets
bullets = []
bullet = []
bullet_image = pygame.image.load('greenbullet.png')
bullet_image = pygame.transform.scale(bullet_image, (30, 30))

while game_loop:
    clock.tick(fps)

    # Animate
    bg_x_1 = bg_x_1 - speed
    bg_x_2 = bg_x_2 - speed

    # Reset position kapag yung x ay lagpas
    if bg_x_1 < background.get_width() * -1:
        bg_x_1 = background.get_width()
    if bg_x_2 < background.get_width() * -1:
        bg_x_2 = background.get_width()
    screen.blit(background, (bg_x_1, bg_y))
    screen.blit(background, (bg_x_2, bg_y))
    screen.blit(girlgun, (girlgun_x, girlgun_y))


  #bullets
    for bullet in bullets:
        screen.blit(bullet_image, pygame.Rect(bullet[0], bullet[1], bullet_image.get_width(), bullet_image.get_height()))

    for b in range(len(bullets)):
        bullets[b][0] += 5

    for bullet in bullets[:]:
        if bullet[1] < 0:
            bullets.remove(bullet)
    
#Controls for girlgun
    movement_speed = 5
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        girlgun_y = girlgun_y - movement_speed
    if keys[pygame.K_DOWN]:
        girlgun_y = girlgun_y + movement_speed
    if keys[pygame.K_LEFT]:
        girlgun_x = girlgun_x - movement_speed
    if keys[pygame.K_RIGHT]:
        girlgun_x = girlgun_x + movement_speed
    if keys[pygame.K_SPACE]:
        bullets.append([girlgun_x + girlgun.get_width(), girlgun_y + girlgun.get_height() -110])
    
    for event in pygame.event.get():
        # User presses QUIT-button.
        if event.type == pygame.QUIT:
            game_loop = False 
        elif event.type == pygame.KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == pygame.K_ESCAPE:
                game_loop = False

    pygame.display.update()