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

status = 'MENU'
mainLoop = True
while mainLoop:
    widght, hight = pygame.display.get_surface().get_size()
    mouse = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    screen.fill('blue')

    if status == 'GAME':
        if aim_hight >= widght/15:
            aim_down = False
        elif aim_hight <= 0:
            aim_down = True

        if aim_down == False:
            aim_hight -= 1.5*(hight/400)
        else:
            aim_hight += 1.5*(hight/400)

        bg = pygame.transform.scale(pygame.image.load(path + 'images/fon/pixil-frame-0 (61).png'), (widght, hight))
        tree = pygame.transform.scale(pygame.image.load(path + 'images/tree/pixil-frame-0 (60).png'), (widght/3, hight/5*4))
        aim = pygame.transform.scale(pygame.image.load(path + 'images/aim/pixil-frame-0 (59).png'), (widght/22, hight/10))

        screen.blit(bg, (0, 0))
        screen.blit(tree, (widght/3*2, hight/5))
        screen.blit(aim, (widght/5*3.9, (hight/3*2) + aim_hight))

    elif status == 'MENU':
        bg = pygame.transform.scale(pygame.image.load(path + 'images/gray/pixil-frame-0 (61) (1).png'), (widght, hight))
        tree = pygame.transform.scale(pygame.image.load(path + 'images/gray/pixil-frame-0 (60) (1).png'), (widght/3, hight/5*4))
        aim = pygame.transform.scale(pygame.image.load(path + 'images/gray/pixil-frame-0 (59) (1).png'), (widght/22, hight/10))
        main_menu = pygame.transform.scale(pygame.image.load(path + 'images/buttons/pixil-frame-0 (86).png'), (widght/5, hight/5.5))
        continue_the_game = pygame.transform.scale(pygame.image.load(path + 'images/buttons/pixil-frame-0 (88).png'), (widght/5, hight/5.5))
        continue_the_game_rect = continue_the_game.get_rect(topleft=(widght/5*2, hight/4*2))


        screen.blit(bg, (0, 0))
        screen.blit(tree, (widght/3*2, hight/5))
        screen.blit(aim, (widght/5*3.9, (hight/3*2) + aim_hight))
        screen.blit(main_menu, (widght/5*2, hight/4))
        screen.blit(continue_the_game, continue_the_game_rect)

        if continue_the_game_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            status = 'GAME'

    elif status == 'MAIN_MENU':
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            mainLoop = False
        elif keys[pygame.K_LEFT]:
            status = 'MENU'
        elif keys[pygame.K_RIGHT]:
            status = 'GAME'
    pygame.display.update() 

pygame.quit()
