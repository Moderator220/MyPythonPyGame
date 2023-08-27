import pygame
from pygame import *
import time
# import win32gui
# import win32con

clock = pygame.time.Clock()

path = ''

pygame.init()

#Create a displace surface object
screen = pygame.display.set_mode((800, 400), RESIZABLE, )
# win32gui.SetWindowPos(win32gui.GetForegroundWindow(), win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE)

aim_hight = 0
aim_down = True

stikman_name = 'b'

# fps
start_time = time.time()
time_int = 1
counter = 0
fps = ''

status = 'MAIN_MENU'
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
        stop = pygame.transform.scale(pygame.image.load(path + 'images/buttons/pixil-frame-0 (97).png'), (widght/20, hight/10))
        
        stop_rect = stop.get_rect(topleft=(0, 0))

        screen.blit(bg, (0, 0))
        screen.blit(tree, (widght/3*2, hight/5))
        screen.blit(aim, (widght/5*3.9, (hight/3*2) + aim_hight))
        screen.blit(stop, stop_rect)

        if stop_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            status = 'MENU'

    elif status == 'MENU':
        bg = pygame.transform.scale(pygame.image.load(path + 'images/gray/pixil-frame-0 (61) (1).png'), (widght, hight))
        tree = pygame.transform.scale(pygame.image.load(path + 'images/gray/pixil-frame-0 (60) (1).png'), (widght/3, hight/5*4))
        aim = pygame.transform.scale(pygame.image.load(path + 'images/gray/pixil-frame-0 (59) (1).png'), (widght/22, hight/10))
        main_menu = pygame.transform.scale(pygame.image.load(path + 'images/buttons/pixil-frame-0 (86).png'), (widght/5, hight/5.5))
        continue_the_game = pygame.transform.scale(pygame.image.load(path + 'images/buttons/pixil-frame-0 (88).png'), (widght/5, hight/5.5))

        continue_the_game_rect = continue_the_game.get_rect(topleft=(widght/5*2, hight/4*2))
        main_menu_rect = main_menu.get_rect(topleft=(widght/5*2, hight/4))

        screen.blit(bg, (0, 0))
        screen.blit(tree, (widght/3*2, hight/5))
        screen.blit(aim, (widght/5*3.9, (hight/3*2) + aim_hight))
        screen.blit(main_menu, main_menu_rect)
        screen.blit(continue_the_game, continue_the_game_rect)

        if continue_the_game_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            status = 'GAME'

        if main_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            status = 'MAIN_MENU'

    elif status == 'MAIN_MENU':
        bg = pygame.transform.scale(pygame.image.load(path + 'images/fon/pixil-frame-0 (92).png'), (widght, hight))
        capsuls = pygame.transform.scale(pygame.image.load(path + 'images/buttons/pixil-frame-0 (89).png'), (widght/10, hight/7))
        baby = pygame.transform.scale(pygame.image.load(path + 'images/buttons/pixil-frame-0 (90).png'), (widght/10, hight/7))
        super_market = pygame.transform.scale(pygame.image.load(path + 'images/buttons/pixil-frame-0 (91).png'), (widght/10, hight/7))
        play = pygame.transform.scale(pygame.image.load(path + 'images/buttons/pixil-frame-0 (93).png'), (widght/8, hight/7))
        stikman = pygame.transform.scale(pygame.image.load(path + f'images/sticmans/{stikman_name}.png'), (widght/8, hight/2))

        play_rect = play.get_rect(topleft=(widght-widght/8, hight-hight/7))
        capsuls_rect = capsuls.get_rect(topleft=(0, hight/5))
        baby_rect = baby.get_rect(topleft=(0, hight/5*2))
        super_market_rect = super_market.get_rect(topleft=(0, hight/5*3))
        stikman_rect = stikman.get_rect(topleft=(widght/2, hight/5*2))

        screen.blit(bg, (0, 0))
        screen.blit(capsuls, capsuls_rect)
        screen.blit(baby, baby_rect)
        screen.blit(super_market, super_market_rect)
        screen.blit(play, play_rect)
        screen.blit(stikman, stikman_rect)

        if play_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            status = 'GAME'

        if capsuls_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            status = 'CAPSULS'
        
        if baby_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            status = 'BABY'

        if super_market_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            status = 'SUPER_MARKET'

    elif status == 'CAPSULS':
        capsuls = pygame.transform.scale(pygame.image.load(path + 'images/three tabs/cap.png'), (widght/5, hight/3))
        bg_cap = pygame.transform.scale(pygame.image.load(path + 'images/three tabs/bg_cap.png'), (widght, hight))
        back = pygame.transform.scale(pygame.image.load(path + 'images/buttons/back.png'), (widght/7, hight/7))

        back_rect = back.get_rect(topleft=(widght-widght/7, 0))

        screen.blit(bg_cap, (0, 0))
        screen.blit(capsuls, (widght/5*2, hight/10))
        screen.blit(back, back_rect)

        if back_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            status = 'MAIN_MENU'

    elif status == 'BABY':
        bg_st = pygame.transform.scale(pygame.image.load(path + 'images/three tabs/bg_st.png'), (widght, hight))
        back = pygame.transform.scale(pygame.image.load(path + 'images/buttons/back.png'), (widght/7, hight/7))
        blek = pygame.transform.scale(pygame.image.load(path + 'images/sticmans/b.png'), (widght/7, hight/3))
        red = pygame.transform.scale(pygame.image.load(path + 'images/sticmans/r.png'), (widght/7, hight/3))

        back_rect = back.get_rect(topleft=(widght-widght/7, 0))
        blek_rect = blek.get_rect(topleft=(widght/16, 0))
        red_rect = red.get_rect(topleft=(widght/4, 0))


        screen.blit(bg_st, (0, 0))
        screen.blit(back, back_rect)
        screen.blit(blek, blek_rect)
        screen.blit(red, red_rect)

        if back_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            status = 'MAIN_MENU'

        if blek_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            status = 'MAIN_MENU'
            stikman_name = 'b'

        if red_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            status = 'MAIN_MENU'
            stikman_name = 'r'

    elif status == 'SUPER_MARKET':
        frg = pygame.transform.scale(pygame.image.load(path + 'images/three tabs/frg.png'), (widght, hight))
        back = pygame.transform.scale(pygame.image.load(path + 'images/buttons/back.png'), (widght/7, hight/7))
        l_blek = pygame.transform.scale(pygame.image.load(path + 'images/bow/l_b.png'), (widght/8, hight/4))
        l_red = pygame.transform.scale(pygame.image.load(path + 'images/bow/l_r.png'), (widght/8, hight/4))

        
        back_rect = back.get_rect(topleft=(widght-widght/7, 0))
        l_blek_rect = l_blek.get_rect(topleft=(widght/16, 10))
        l_red_rect = l_red.get_rect(topleft=(widght/4, 10))
                
        screen.blit(frg, (0, 0))
        screen.blit(back, back_rect)
        screen.blit(l_blek, l_blek_rect)
        screen.blit(l_red, l_red_rect)
        
        if back_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            status = 'MAIN_MENU'

        if l_blek_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            status = 'MAIN_MENU'

        if l_red_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            status = 'MAIN_MENU'

    # fps
    font = pygame.font.Font(None, 20)

    counter += 1
    if (time.time() - start_time) > time_int:
        fps = "FPS: " + str(int(counter / (time.time() - start_time)))
        counter = 0
        start_time = time.time()

    screen.blit(font.render(fps, True, (180, 0, 0)), (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            mainLoop = False
        elif keys[pygame.K_LEFT]:
            status = 'MENU'
        elif keys[pygame.K_RIGHT]:
            status = 'GAME'
    pygame.display.update() 

pygame.quit()
