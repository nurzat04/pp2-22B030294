import pygame
from datetime import datetime

pygame.init()
window = pygame.display.set_mode((800,500))
pygame.display.set_caption('mickey clock')
clock = pygame.time.Clock()
img = pygame.image.load("clock.jpg")
min = pygame.image.load("min.jpeg")
sec = pygame.image.load("sec.jpeg")
#window.blit(img, (0,1))
font = pygame.font.SysFont('Verdana', 50)

def rotate(surface, image, right_pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topright = right_pos).center)
    
    surface.blit(rotated_image,new_rect)
    
    
pygame.display.update()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.blit(img, (0,1))
    t = datetime.now()
    angle_min = 360 - t.minute * 6
    angle_sec = 360 - t.second * 6
    rotate(window,sec,(420,205),angle_sec)
    rotate(window,min,(430,180),angle_min)
    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('white'), pygame.Color('orange'))
    window.blit(time_render, (10, 20))
    pygame.display.flip()
pygame.quit()