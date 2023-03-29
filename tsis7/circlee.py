import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800, 500))
x = 50
y = 50

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 20
        if pressed[pygame.K_DOWN]: y += 20
        if pressed[pygame.K_LEFT]: x -= 20
        if pressed[pygame.K_RIGHT]: x += 20
        if y <= 50: y = 50
        if y >= 450: y = 450
        if x < 50: x= 50
        if x > 750: x = 750    
        screen.fill((255,255,255))
              
        pygame.draw.circle(screen, (255,0,0), (x, y), 50)
        
        pygame.display.flip()
        #clock.tick(60)
        time.sleep(1/60)