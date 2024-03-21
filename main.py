import pygame
import random
from pygame import mixer #for sound

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
one_pixel = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TEAL = (150, 255, 255)
BLUE = (172, 213, 239)
my_font = pygame.font.Font("assets/Micro5-Regular.ttf", 80)
FPS = 10
clock = pygame.time.Clock()
snake_segment_nums = 3

food_x_pos = 0
food_y_pos = 0
generate_food_now = True
snake = []
snake_x_move = SCREEN_WIDTH/2 #position starts in middle of screen
snake_y_move = SCREEN_HEIGHT/2 #position starts in middle of screen
food_counter = 0
fctext_x_pos = SCREEN_WIDTH - (one_pixel*3) #fc = food counter
fctext_y_pos = one_pixel #fc = food counter
up_move = False
down_move = False
left_move = False
right_move = False

#image imports
food_img = pygame.image.load("assets/food.png")
food_img.set_colorkey(WHITE)
snake_img = pygame.image.load("assets/snake.png") #left right movement
snake_img.set_colorkey(WHITE)

#music
mixer.music.load("assets/gamemusic.mp3")
mixer.music.play(-1) #play continuously

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
running = True

while running:
    screen.fill((BLUE))
    
    #generate food position
    while generate_food_now:
        food_x_pos = random.randint(one_pixel * 2, SCREEN_WIDTH - (one_pixel * 2))
        food_y_pos = random.randint(one_pixel * 2, SCREEN_HEIGHT - (one_pixel * 2))
        if food_x_pos % one_pixel == 0 and food_y_pos % one_pixel == 0:
            generate_food_now = False
            break

     #draw food
    screen.blit(food_img, (food_x_pos ,food_y_pos))
  
    #draw snake (images)
    for i in range(snake_segment_nums):
        if up_move:
            snake.append(screen.blit(snake_img, (snake_x_move, snake_y_move + (one_pixel * i))))
        elif down_move:
            snake.append(screen.blit(snake_img, (snake_x_move, snake_y_move - (one_pixel * i), one_pixel, one_pixel)))
        elif left_move:
            snake.append(screen.blit(snake_img, (snake_x_move - (one_pixel * i), snake_y_move, one_pixel, one_pixel)))
        elif right_move:
            snake.append(screen.blit(snake_img, (snake_x_move + (one_pixel * i), snake_y_move, one_pixel, one_pixel)))
        else: #before press anything
            snake.append(screen.blit(snake_img, (snake_x_move, snake_y_move + (one_pixel * i), one_pixel, one_pixel)))


    #eat food counter
    if food_x_pos == snake_x_move and food_y_pos == snake_y_move:
        food_counter += 1
        generate_food_now = True

    #print food counter
    text_surface = my_font.render(str(food_counter), False, BLACK)
    if food_counter >= 10: fctext_x_pos = SCREEN_WIDTH - (one_pixel*4)
    if food_counter >= 100: fctext_x_pos = SCREEN_WIDTH - (one_pixel*6)
    if food_counter >= 100: fctext_x_pos = SCREEN_WIDTH - (one_pixel*7)
    screen.blit(text_surface, (fctext_x_pos, fctext_y_pos))

    #moving upon keyboard command
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                up_move = True
                down_move = False
                left_move = False
                right_move = False
                # snake_y_move -= one_pixel
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                up_move = False
                down_move = True
                left_move = False
                right_move = False
                # snake_y_move += one_pixel
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                up_move = False
                down_move = False
                left_move = False
                right_move = True
                # snake_x_move += one_pixel
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                up_move = False
                down_move = False
                left_move = True
                right_move = False
                # snake_x_move -= one_pixel
    if up_move:
        print("up")
        snake_y_move -= one_pixel
    if down_move:
        print("down")
        snake_y_move += one_pixel
    if left_move:
        print("left")
        snake_x_move -= one_pixel
    if right_move:
        print("right")
        snake_x_move += one_pixel

    #out of bounds
    if snake_y_move < -one_pixel or snake_y_move > SCREEN_HEIGHT or snake_x_move < 0 or snake_x_move > SCREEN_WIDTH:
        pygame.draw.rect(screen, BLACK, pygame.Rect(0 ,0, SCREEN_WIDTH, SCREEN_HEIGHT))
        text_surface = my_font.render("Game Over", False, WHITE)
        screen.blit(text_surface,(SCREEN_WIDTH/2 - (one_pixel*6), SCREEN_HEIGHT/2- (one_pixel*2)))
        pygame.display.update()
        pygame.time.wait(2500)
        food_x_pos = 0
        food_y_pos = 0
        generate_food_now = True
        snake_x_move = SCREEN_WIDTH/2 
        snake_y_move = SCREEN_HEIGHT/2
        food_counter = 0
        fctext_x_pos = SCREEN_WIDTH - (one_pixel*3)
        fctext_y_pos = one_pixel 
        up_move = False
        down_move = False
        left_move = False
        right_move = False

    clock.tick(FPS)
    pygame.display.update()
pygame.quit()