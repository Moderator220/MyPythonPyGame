import pygame
from pygame import *

pygame.init()

#Create a displace surface object
screen = pygame.display.set_mode((700, 400), RESIZABLE)

mainLoop = True
while mainLoop:

    widght, hight = pygame.display.get_surface().get_size()

    screen.fill('green')
    pygame.draw.rect(screen, (255, 255, 255), 
                 ((widght / 4), (hight / 4), (widght / 2), (hight / 2)))

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            mainLoop = False
    pygame.display.update()

pygame.quit()