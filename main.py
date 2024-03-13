import pygame
import random

cloud_speed = 0.05 # !
cactus_speed = 0.05 # !

WIDTH, HEIGHT = 600, 200
screen = pygame.display.set_mode((WIDTH,HEIGHT))

dino_image = pygame.image.load("dino.png")
cactus_image = pygame.image.load("cactus.png")
cloud_image = pygame.image.load("cloud.png")
gameover_image = pygame.image.load("gameover.png")

cloud_x = WIDTH
cloud_y = random.randint(0,100)

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

run = True
while run:
    for event in pygame.event.get:
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()

                cloud_x -= cloud_speed
                if cloud_x + cloud_image.get_width() < 0:
                    cloud_x = WIDTH
                    cloud_y = random.randint(0,100)
                for i in range(len(cactus_list)):
                    cactus_list[i][0] -= cactus_speed
                    if cactus_list[i][0] + cactus_image.get_width() < 0:
                        cactus_list.pop(i)

                if cactus_list[-1][0] < 450:
                    next_cactus_time -= 0.01
                    if next_cactus_time <= 0:
                        create_cactus()
                        next_cactus_time = random.randint(1, 40)



                dino_y += speed_y
                speed_y += 0.0003 # !
                if dino_y >= HEIGHT - 50
                    dino_y = HEIGHT - 50
                    speed_y = 0
                    dino_jumping = False

                for cactus_x, cactus_y in cactus_list:
                    if dino_x + dino_image.get_width() > cactus_x and \
                            dino_x < cactus_x + cactus_image.get_width() and \
                            dino_y + dino_image.get_height() > cactus_y and \
                            dino_y < cactus_y + cactus_image.get_height():
                        run = False

                screen.fill((225,225,225))
                screen.blit(dino_image,(dino_x,dino_y))
                screen.blit(cloud_image, (cloud_x, cloud_y))

                for cactus in cactus_list:
                    screen.blit(cactus_image,(cactus[0],cactus[1]))

                pygame.display.flip()