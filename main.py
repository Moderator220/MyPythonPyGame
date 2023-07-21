import pygame
from pygame import *

pygame.init()

#Create a displace surface object
screen = pygame.display.set_mode((400, 400), RESIZABLE)

mainLoop = True
while mainLoop:

    widght, hight = pygame.display.get_surface().get_size()

    screen.fill('green')
    pygame.draw.rect(screen, (255, 255, 255), 
                 ((widght / 4), (hight / 4), (widght / 2), (hight / 2)))
    
    label = pygame.font.Font('C:/Users/VLAD/PycharmProjects/Mars protaction/fonts/planet_font.ttf', int(hight / 2))

    next_label = label.render('дальше', True, 'black')

    next_label_x = widght / 4
    next_label_y = hight / 4
    next_label_rect = next_label.get_rect(topleft=(next_label_x, next_label_y))

    screen.blit(next_label, next_label_rect)

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            mainLoop = False
    pygame.display.update()

pygame.quit()