import pygame
from pygame import *

pygame.init()

#Create a displace surface object
screen = pygame.display.set_mode((800, 400), RESIZABLE)

mainLoop = True
while mainLoop:
    widght, hight = pygame.display.get_surface().get_size()

    screen.fill('blue')

    # sqr:

    pygame.draw.rect(screen, 'green', 
                 (widght / 3, hight / 3, widght / 3, hight / 3))

    # font:

    label = pygame.font.Font('font.ttf', int(hight / 3))

    next_label = label.render('при', True, 'red')

    next_label_x = widght / 3
    next_label_y = hight / 3
    next_label_rect = next_label.get_rect(topleft=(next_label_x, next_label_y))

    # blit font:

    screen.blit(next_label, next_label_rect)

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            mainLoop = False
    pygame.display.update()

pygame.quit()