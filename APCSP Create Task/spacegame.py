# Pygame:
import random
import time
import pygame
pygame.init()

# Game Window
gameWindowWidth = 500
gameWindowHeight = 500
gameWindow = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))
background = pygame.image.load("galaxy.jpg")
pygame.display.set_caption("Game Window")

def gameLoop():
    # Characters and Objects:
    class playerSpaceShip():
        def __init__(self, x, y):
            self.playerSpaceShipx = x
            self.playerSpaceShipy = y
            self.playerSpaceShipWidth = 64
            self.playerSpaceShipHeight = 64
            self.playerSpaceShipSpeed = 7
            self.playerSpaceShipSprite = pygame.image.load("spaceship.png") 
        def drawSpaceShip(self):
            gameWindow.blit(self.playerSpaceShipSprite, (self.playerSpaceShipx, self.playerSpaceShipy))

    class bulletClass():
        def __init__(self, x, y):
            self.bulletx = x
            self.bullety = y
            self.bulletWidth = 3
            self.bulletHeight = 7
            self.bulletSpeed = 8
            self.bulletColor = (255, 0, 0)
        def playBulletSoundEffect(self):
            pygame.mixer.music.load("bulletsoundeffect.wav")
            pygame.mixer.music.play()
        def bulletCollision(self):
            bulletList.pop(bulletList.index(bullet))
        def drawBullet(self):
            pygame.draw.rect(gameWindow, self.bulletColor, (self.bulletx, self.bullety, self.bulletWidth, self.bulletHeight))

    class fireballClass():
        def __init__(self, x, y):
            self.fireballx = x
            self.firebally = y
            self.fireballWidth = 29
            self.fireballHeight = 65   
            self.fireballSpeed = 4
            self.fireballRandNum = random.randint(0, 1)
            self.fireballPlus = False
            self.fireballMinus = False
            self.fireballSprite = pygame.image.load("fireball.png")
        def fireballCollision(self):
            fireballList.pop(fireballList.index(fireball))
        def drawFireball(self):
            gameWindow.blit(self.fireballSprite, (self.fireballx, self.firebally))

    # Draw Characters and Objects:      
    def drawGameWindow():
        gameWindow.blit(background, (0, 0))
        spaceship.drawSpaceShip()
        for bullet in bulletList:
            bullet.drawBullet()
        for fireball in fireballList:
            fireball.drawFireball()
        gameWindow.blit(playerScore, (430, 20))
        pygame.display.update()

    # Main Loop:
    spaceship = playerSpaceShip(215, 400)
    bulletList = []
    fireballList = []
    bulletTimer = 0
    score = 0
    gameRunning = True
    while gameRunning == True:
        gameClock = pygame.time.Clock()
        gameClock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False

        # Bullets:
        for bullet in bulletList:
            if bullet.bullety < gameWindowHeight and bullet.bullety > 0:
                bullet.bullety -= bullet.bulletSpeed
            else:
                bulletList.pop(bulletList.index(bullet))
        
        # Fireballs:
        for fireball in fireballList:
            if fireball.firebally < gameWindowHeight and fireball.firebally > 0:
                fireball.firebally += fireball.fireballSpeed
            else:
                fireballList.pop(fireballList.index(fireball))
            if fireball.fireballRandNum == 1:
                fireball.fireballSprite = pygame.image.load('fireball2.png')
                fireball.fireballPlus = False
            else:
                fireball.fireballSprite = pygame.image.load('fireball.png')
                fireball.fireballPlus = True
        if len(fireballList) < 2:
            fireballList.append(fireballClass(random.randrange((spaceship.playerSpaceShipWidth // 2), (gameWindowWidth - (spaceship.playerSpaceShipWidth))), 1))
        
        # Text:
        red = (255, 0, 0)
        def textDisplay(text, color, font, fontSize):
            textFont = pygame.font.Font(font, fontSize)
            displayText = textFont.render(text, True, color)
            return displayText

        # Game Over:
        gameOverText = "Game Over"
        gameOverColor = red
        gameOverFont = "freesansbold.ttf"
        gameOverFontSize = 50
        gameOver = textDisplay(gameOverText, gameOverColor, gameOverFont, gameOverFontSize)
        gameOverRect = gameOver.get_rect()
        gameOverRect.center = ((gameWindowWidth//2), (gameWindowHeight//2)) 
        def gameOverMethod():
            gameWindow.blit(gameOver, gameOverRect)
            pygame.display.update()
            time.sleep(2)
            gameLoop()

        # You Win:
        youWinText = "You Win!"
        youWinColor = red
        youWinFont = "freesansbold.ttf"
        youWinFontSize = 50
        youWin = textDisplay(youWinText, youWinColor, youWinFont, youWinFontSize)
        youWinRect = youWin.get_rect()
        youWinRect.center = ((gameWindowWidth//2), (gameWindowHeight//2))
        def youWinMethod():
            gameWindow.blit(youWin, youWinRect)
            pygame.display.update()
            time.sleep(4)
            gameLoop()

        # Scoring:
        scoreText = "Score: " + str(score)
        scoreColor = red
        scoreFont = "freesansbold.ttf"
        scoreFontSize = 15
        playerScore = textDisplay(scoreText, scoreColor, scoreFont, scoreFontSize)

        # Hitbox-Based Collisions:
        def bulletCollision(x1, y1, width1, height1, x2, y2, width2, height2):
            if x2 <= x1 <= x2 + width2 and y2 <= y1 <= y2 + height2:
                return True
            elif x2 <= x1 + width1 <= x2 + width2 and y2 <= y1 <= y2 + height2:
                return True
            else:
                return False
        
        def spaceshipCollision(x1, y1, width1, height1, x2, y2, width2, height2):
            if x2 <= x1 <= x2 + width2 and y2 <= y1 <= y2 + height2:
                return True
            elif x2 <= x1 + width1 <= x2 + width2 and y2 <= y1 <= y2 + height2:
                return True
            elif x2 <= x1 + width1 <= x2 + width2 and y2 <= y1 + height1 <= y2 + height2:
                return True
            elif x2 <= x1 + width1 <= x2 + width2 and y2 <= y1 + height1 <= y2 + height2:
                return True
            elif x2 <= x1 + (width1//2) <= x2 + width2 and y2 <= y1 <= y2 + height2:
                return True
            else:
                return False
        
        for bullet in bulletList:
            for fireball in fireballList:
                collision = bulletCollision(bullet.bulletx, bullet.bullety, bullet.bulletWidth, bullet.bulletHeight, fireball.fireballx, fireball.firebally, fireball.fireballWidth, fireball.fireballHeight)
                if collision == True:
                    fireball.fireballCollision()
                    bullet.bulletCollision()
                    if fireball.fireballPlus == True:
                        score += 1
                    elif fireball.fireballPlus == False and score == 0:
                        gameOverMethod()
                    elif score == 10:
                        youWinMethod()
                    else:
                        score -= 1
        
        for fireball in fireballList:
            crash = spaceshipCollision(spaceship.playerSpaceShipx, spaceship.playerSpaceShipy, spaceship.playerSpaceShipWidth, spaceship.playerSpaceShipHeight, fireball.fireballx, fireball.firebally, fireball.fireballWidth, fireball.fireballHeight)
            if crash == True:
                gameOverMethod()

        # Key Presses:
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_LEFT] == True and spaceship.playerSpaceShipx >= spaceship.playerSpaceShipSpeed:
            spaceship.playerSpaceShipx -= spaceship.playerSpaceShipSpeed
        if keyPressed[pygame.K_RIGHT] == True and spaceship.playerSpaceShipx < gameWindowWidth - spaceship.playerSpaceShipWidth - spaceship.playerSpaceShipSpeed:
            spaceship.playerSpaceShipx += spaceship.playerSpaceShipSpeed
        if keyPressed[pygame.K_UP] == True and spaceship.playerSpaceShipy >= spaceship.playerSpaceShipSpeed:
            spaceship.playerSpaceShipy -= spaceship.playerSpaceShipSpeed
        if keyPressed[pygame.K_DOWN] == True and spaceship.playerSpaceShipy < gameWindowHeight - spaceship.playerSpaceShipHeight - spaceship.playerSpaceShipSpeed:
            spaceship.playerSpaceShipy += spaceship.playerSpaceShipSpeed
        if keyPressed[pygame.K_SPACE] == True:
            for bullet in bulletList:
                bullet.playBulletSoundEffect()
            if len(bulletList) < 10:
                bulletList.append(bulletClass(round(spaceship.playerSpaceShipx + spaceship.playerSpaceShipWidth // 2), spaceship.playerSpaceShipy))
        drawGameWindow()
    pygame.quit()
gameLoop()