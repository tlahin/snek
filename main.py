
from cgitb import reset
from locale import resetlocale
import sys
import pygame

pygame.init()

pygame.display.set_caption("Filler visualiser")
height = 800
width = 1300
window = pygame.display.set_mode((width, height))
bg_menu = pygame.Surface((width, height))
bg_menu.fill(pygame.Color(255, 255, 255))
bg_play = pygame.Surface((width, height))
bg_play.fill(pygame.Color(0, 0, 0)) 

def play():
    window.blit(bg_play, (0, 0))
    pygame.draw.rect(window, (255, 0, 00), pygame.Rect(150, 150, 60, 60), 2)
    print("play")

running = True
start = True

while running:

    window.blit(bg_menu, (0, 0))
    if start and pygame.time.wait(500):
        pygame.display.update()
        pygame.time.wait(240)
        play()
        start = False
    if not start:
        font = pygame.font.SysFont('Arial', 45)
        text = font.render('By tlahin' , True , (0, 255, 255))
        window.blit(text, (width / 2, height / 2))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and start:
                pygame.display.update()
                pygame.time.wait(240)
                print("PLAY")
                play()
                start = False
            if event.key == pygame.K_ESCAPE:
                is_running = False
        if event.type == pygame.QUIT:
            is_running = False
    
    pygame.display.flip()
