import pygame
from pygame import *

pygame.init()

#Create a displace surface object
screen = pygame.display.set_mode((700, 400), RESIZABLE)

mainLoop = True
while mainLoop:
    screen.fill('blue')

    widght, hight = pygame.display.get_surface().get_size()
    pygame.draw.rect(screen, 'green', 
                 (widght / 3, hight / 3, widght / 3, hight / 3))

    

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            mainLoop = False
    pygame.display.update()

pygame.quit()