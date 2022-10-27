
import time
import sys
import pygame

pygame.init()

#colours
cyan = (51, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 128, 255)
red = (255, 0, 0)

pygame.display.set_caption("Epic Game")
height = 800
width = 1300
window = pygame.display.set_mode((width, height))
bg_menu = pygame.Surface((width, height))
bg_menu.fill(pygame.Color(white))
bg_play = pygame.Surface((width, height))
bg_play.fill(pygame.Color(black))

start_img = pygame.image.load("./resources/start_button.png").convert_alpha()
start_img = pygame.transform.scale(start_img, (150, 50))
quit_img = pygame.image.load("./resources/quit_button.png").convert_alpha()
quit_img = pygame.transform.scale(quit_img, (150, 50))

fontsmall = pygame.font.SysFont('Arial', 50)
fontbig = pygame.font.SysFont('Arial', 80)

class button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        mouse_action = False
        mouse_pos = pygame.mouse.get_pos()
        surface.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                mouse_action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            return mouse_action

start_button = button(width / 2 - 150 / 2, height / 2, start_img)
quit_button = button(width / 2 - 150 / 2, height / 2 + 55, quit_img)

def pause_game():

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                    return False
    return True

def play():
    
    paused = False
    dead = False
    cube_size = 25
    x = width / 2
    y = height / 2
    direction = 1
    clock = pygame.time.Clock()
    speed = 10

    while not dead:

        window.blit(bg_play, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    # 1 == up
                    direction = 1
                elif event.key == pygame.K_s:
                    # 2 == down
                    direction = 2
                elif event.key == pygame.K_a:
                    # 3 == left
                    direction = 3
                elif event.key == pygame.K_d:
                    # 4 == right
                    direction = 4
                if event.key == pygame.K_SPACE:
                    print("PAUSED")
                    if pause_game() == 1:
                        dead = True
                    print("RESUME")
                    
        if direction == 1:
            y -= cube_size
        elif direction == 2:
            y += cube_size
        elif direction == 3:
            x -= cube_size
        elif direction == 4:
            x += cube_size

        if x < 0:
            x = width - cube_size
        elif x >= width:
            x = 0
        if y < 0:
            y = height - cube_size
        elif y >= height:
            y = 0

        pygame.draw.rect(window, cyan, [x, y, cube_size, cube_size])
        pygame.display.update()
        clock.tick(speed)

running = True
start = True

print("RUNNING")

while running:

    window.blit(bg_menu, (0, 0))

    menu = fontbig.render('Main Menu' , True , (black))
    window.blit(menu, (width / 2 - 200, height / 2 - 200))

    if start_button.draw(window):
        print("START")
        play()
    if quit_button.draw(window):
        print("QUIT")
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("EXIT")
            running = False
    
    pygame.display.flip()
