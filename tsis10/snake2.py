import pygame
import time
import random
import datetime
 
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(0, 255, 0)

pygame.init()
pygame.display.set_caption('Snake game')
game_window = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]

foods = []

direction = 'RIGHT'
change_to = direction

score = 0



def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Foods : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)
def show_score1(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('speed : ' + str(snake_speed), True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (660,5)
    game_window.blit(score_surface, score_rect)
def show_score2(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('level : ' + str(level), True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (300,5)
    game_window.blit(score_surface, score_rect)
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render("Game over", True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (360, 120)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

while True:
    snake_speed = 8
    level = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
    snake_body.insert(0, list(snake_position))
    
    # check if snake has collided with a food
    for food in foods:
        if snake_position[0] == food[0][0] and snake_position[1] == food[0][1]:
            score += food_size
            foods.remove(food)
            break
    else:
        snake_body.pop()

    # spawn new food if there are fewer than 5 on the screen
    while len(foods) < 5 :
        food_position = [random.randrange(1, (720//10)) * 10,
                          random.randrange(1, (480//10)) * 10]
        food_size = random.randint(5, 15)
        food_color = random.choice([red, blue, white])
        new_food = (food_position, food_size, food_color, time.time())
        if new_food not in foods:
            foods.append(new_food)
        
        
    scores = range(score)
    for i in scores:
        if (i % 8 == 0 and i != 0):
            snake_speed += 0.5
            level += 1
    
    game_window.fill(black)

    # draw all the food on the screen
    c = datetime.datetime.now()
    f = foods.copy()
    for food in f:
        x = c.strftime("%S")
        if int(x) % 5 == 0 and food_size >= 10:
            foods.remove(food)
            continue
        pygame.draw.rect(game_window, food[2], pygame.Rect(food[0][0], food[0][1], food[1], food[1]))
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > 710:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > 470:
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    # displaying score countinuously
    show_score(1, white, 'times new roman', 20)
    show_score1(1, white, 'times new roman', 20)
    show_score2(1, white, 'times new roman', 20)
    
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    clock.tick(snake_speed)
