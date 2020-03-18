import pygame
pygame.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Drawing Shapes')

Black = (0,0,0)
White = (255,255,255)
Blue = (0,0,255)
Green = (0,255,0)
Red = (255,0,0)
Orange = (255,165,0)

window.fill(White)
pygame.draw.rect(window, Blue, (50, 50, 100, 50))
pygame.draw.line(window, Black, (60, 70), (150, 200), 3)
pygame.draw.circle(window, Red, (290, 100), 100)
pygame.draw.ellipse(window, Green, (180, 180, 100, 200))
pygame.draw.polygon(window, Orange, [(300, 400), (390, 490), (520, 300)])

pygame.display.update()
