import pygame
import time
from pygame.locals import *
import random
pygame.init()
speed = 5
score = 0
coins = 0
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (0,0,0))
img = pygame.image.load("AnimatedStreet.png")
window = pygame.display.set_mode((400,600))
window.fill((255,255,255))
pygame.display.set_caption('racer')
clock = pygame.time.Clock()
class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,360), 0)
    def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30,370),0)

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < 400:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)
class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img = pygame.image.load("coin.png")
        n_img = pygame.transform.scale(img, (30,30))
        self.image = n_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,360),0)
    def move(self):
        self.rect.move_ip(0, speed)
        if(self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40,360),0)
    def reset(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40,360),0)

p1 = player()
e1 = enemy()
c1 = coin()
c2 = coin()

enemies = pygame.sprite.Group()
enemies.add(e1)
coinss = pygame.sprite.Group()
coinss.add(c1)
coinss.add(c2)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)
all_sprites.add(c1)
all_sprites.add(c2)

inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

pygame.mixer.Sound("background.wav").play(-1)
pygame.mixer.music.load("point.mp3")
#done = False
while True:
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += 0.5
        #if event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE:
            #done = True
        if event.type == pygame.QUIT:
            exit()
    window.blit(img,(0,0))
    scores = font_small.render(str(score), True, (0,0,0))
    window.blit(scores, (10,10))
    coinstext = font_small.render(str(coins), True, (0,0,0))
    window.blit(coinstext, (370,10))
    for entity in all_sprites:
        window.blit(entity.image, entity.rect)
        entity.move()
    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.stop()
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)
        window.fill((255,0,0))
        window.blit(game_over, (30,250))
                      
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        exit()
    elif pygame.sprite.spritecollideany(p1,coinss):
        pygame.mixer.music.play()
        coins += 1
        for coin in coinss:
            coin.reset()
    pygame.display.update()
    clock.tick(60)