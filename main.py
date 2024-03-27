import pygame
import random

pygame.init()

score = 0
font = pygame.font.Font(None, 36)
BLACK = (0, 0, 0)

cloud_speed = 0.05 # !
cactus_speed = 0.05 # !

WIDTH, HEIGHT = 600, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))

dino_image = pygame.image.load("dino.png")
cactus_image = pygame.image.load("cactus.png")
cloud_image = pygame.image.load("cloud.png")
gameover_image = pygame.image.load("gameover.png")

button_width, button_height = gameover_image.get_width(), gameover_image.get_height()

button_x = WIDTH // 2 - button_width // 2
button_y = HEIGHT // 2 - button_height // 2

cloud_x = WIDTH
cloud_y = random.randint(0, 100)

dino_x = 20
dino_y = HEIGHT - 50
speed_y = 0
dino_jumping = False

cactus_list = []
next_cactus_time = 1 # !

def jump():
    global speed_y, dino_jumping
    if not dino_jumping:
        speed_y = -0.22 # !
        dino_jumping = True

def create_cactus():
    cactus_x = WIDTH
    cactus_y = HEIGHT - 50
    cactus_list.append([cactus_x, cactus_y])

create_cactus()

button_show = False
paused = False

def draw_button():
    if button_show:
        global paused
        screen.blit(gameover_image, (button_x, button_y))
        paused = True

def press_button():
    global paused
    global button_show
    global score
    score = 0
    while len(cactus_list) != 0:
        cactus_list.pop(0)
    paused = False
    button_show = False
    create_cactus()

button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not paused:
                jump()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos) and button_show:
                press_button()

    cloud_x -= cloud_speed
    if cloud_x + cloud_image.get_width() < 0:
        cloud_x = WIDTH
        cloud_y = random.randint(0, 100)

    if not paused:
        for i in range(len(cactus_list)):
            cactus_x, cactus_y = cactus_list[i]
            cactus_x -= cactus_speed
            if cactus_x + cactus_image.get_width() < 0:
                cactus_list.pop(i)
                break
            cactus_list[i] = (cactus_x, cactus_y)

    if cactus_list[-1][0] < 450:
        next_cactus_time -= 0.01
        if next_cactus_time <= 0:
            create_cactus()
            next_cactus_time = random.randint(1, 40)

    dino_y += speed_y
    speed_y += 0.0003 # !
    if dino_y >= HEIGHT - 50:
        dino_y = HEIGHT - 50
        speed_y = 0
        dino_jumping = False

    for cactus_x, cactus_y in cactus_list:
        if dino_x + dino_image.get_width() > cactus_x and \
                dino_x < cactus_x + cactus_image.get_width() and \
                dino_y + dino_image.get_height() > cactus_y and \
                dino_y < cactus_y + cactus_image.get_height():
            button_show = True

    screen.fill((255, 255, 255))
    screen.blit(dino_image, (dino_x, dino_y))
    screen.blit(cloud_image, (cloud_x, cloud_y))

    for cactus in cactus_list:
        screen.blit(cactus_image, (cactus[0], cactus[1]))

    if not paused:
        score += 0.001
    score_rounded = int(score)
    score_text = font.render(str(score_rounded), True, BLACK)
    screen.blit(score_text, (20, 20))

    draw_button()

    pygame.display.flip()
