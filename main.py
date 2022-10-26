
import sys
import pygame

pygame.init()

pygame.display.set_caption("Epic Game")
height = 800
width = 1300
window = pygame.display.set_mode((width, height))
bg_menu = pygame.Surface((width, height))
bg_menu.fill(pygame.Color(255, 255, 255))
bg_play = pygame.Surface((width, height))
bg_play.fill(pygame.Color(0, 0, 255)) 

fontsmall = pygame.font.SysFont('Arial', 50)
fontbig = pygame.font.SysFont('Arial', 80)

window.blit(bg_menu, (0, 0))

running = True
start = True

while running:

    author = fontsmall.render('By tlahin' , True , (0, 0, 0))
    menu = fontbig.render('Main Menu' , True , (0, 0, 0))
    window.blit(author, (width - 250, height - 100))
    window.blit(menu, (width / 2 - 200, height / 2 - 200))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pygame.display.update()
                pygame.time.wait(240)
                print("PLAY")
                #play()
                start = False
        if event.type == pygame.QUIT:
            print("QUIT")
            running = False
    
    pygame.display.flip()
