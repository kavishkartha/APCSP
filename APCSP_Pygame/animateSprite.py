import pygame
pygame.init()

screenWidth = 500
screenHeight = 480
gameWindow = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('animateSprite.py')

x = 50
y = 50
width = 64
height = 64
vel = 5

left = False
right = False
up = False
down = False

sprite = pygame.image.load('L1.png')
background = pygame.image.load('bg.jpg')

def drawFunction():
    gameWindow.blit(background, (0,0))
    if left == True:
        gameWindow.blit(sprite, (x,y))
    if right == True:
        gameWindow.blit(sprite, (x,y))
    if up == True:
        gameWindow.blit(sprite, (x,y))
    if down == True:
        gameWindow.blit(sprite, (x,y))
    else:
        gameWindow.blit(sprite, (x,y))
    pygame.display.update()
        
run = True
while run:
    FPS = 30

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
        right = True
    if keys[pygame.K_UP] and y > vel:
        y -= vel
        up = True
    if keys[pygame.K_DOWN] and y < screenHeight - height - vel:
        y += vel
        down = True
    drawFunction()

pygame.quit()
