import pygame
from pygame import *

clock = pygame.time.Clock()

# path = 'c:/Users/VLAD/OneDrive/Documents/Sashas_PyGame/'
path = ''

pygame.init()

#Create a displace surface object
screen = pygame.display.set_mode((800, 400), RESIZABLE)

aim_hight = 0
aim_down = True

mainLoop = True
while mainLoop:
    widght, hight = pygame.display.get_surface().get_size()
    mouse = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    screen.fill('blue')

    if aim_hight >= 48:
        aim_down = False
    elif aim_hight <= 0:
        aim_down = True

    if aim_down == False:
        aim_hight -= 4
    else:
        aim_hight += 4

    bg = pygame.transform.scale(pygame.image.load(path + 'images/fon/pixil-frame-0 (61).png'), (widght, hight))
    tree = pygame.transform.scale(pygame.image.load(path + 'images/tree/pixil-frame-0 (60).png'), (widght/3, hight/5*4))
    aim = pygame.transform.scale(pygame.image.load(path + 'images/aim/pixil-frame-0 (59).png'), (widght/22, hight/10))

    screen.blit(bg, (0, 0))
    screen.blit(tree, (widght/3*2, hight/5))
    screen.blit(aim, (widght/5*3.9, (hight/3*2) + aim_hight))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            mainLoop = False
    pygame.display.update()
    clock.tick(5)

pygame.quit()
