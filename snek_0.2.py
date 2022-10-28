
import pygame
import random

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

snek_position = [width / 2 + 200, height / 2]
snek_body =  [[width / 2 + 200, height / 2],
              [width / 2 + 190, height / 2],
              [width / 2 + 180, height / 2],
              [width / 2 + 170, height / 2]
              ]

def play():
    
    dead = False
    direction = 'LEFT'
    change_to = direction
    fps = pygame.time.Clock()
    snek_speed = 10

    while not dead:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    change_to = 'UP'
                if event.key == pygame.K_s:
                    change_to = 'DOWN'
                if event.key == pygame.K_a:
                    change_to = 'LEFT'
                if event.key == pygame.K_d:
                    change_to = 'RIGHT'
                if event.key == pygame.K_SPACE:
                    print("PAUSE")
                    pause_game()
                    print("RESUME")

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snek_position[1] -= 10
        if direction == 'DOWN':
            snek_position[1] += 10
        if direction == 'LEFT':
            snek_position[0] -= 10
        if direction == 'RIGHT':
            snek_position[0] += 10

        if snek_position[0] < 0:
            snek_position[0] = width - 10
        elif snek_position[0] >= width:
            snek_position[0] = 0
        if snek_position[1] < 0:
            snek_position[1] = height - 10
        elif snek_position[1] >= height:
            snek_position[1] = 0

        snek_body.insert(0, list(snek_position))
        snek_body.pop()
        window.fill(black)
        
        for pos in snek_body:
            pygame.draw.rect(window, cyan, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.display.update()
        fps.tick(snek_speed)

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
