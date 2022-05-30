import pygame
import sys
import random
from random import randint

pygame.init()
pygame.font.init()
pygame.display.init()
width = 1600
height = 800
keys = pygame.key.get_pressed()
clock = pygame.time.Clock()

bruh = randint(0, 1400)

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("BRUH")

the_Fucking_image = pygame.image.load("epic.png")
Fucking_image_rect = pygame.Rect(bruh,bruh, the_Fucking_image.get_width(), the_Fucking_image.get_height())

bounceX = 1
bounceY = 1

velocityY = 5
velocityX = 5

while True:
    Fucking_image_rect.x += velocityX
    Fucking_image_rect.y += velocityY   
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0 ,255) 
 
    if Fucking_image_rect.y >= 700:       
        velocityY += 3      
        Fucking_image_rect.y -= velocityY
        
        print("1")

    if Fucking_image_rect.y <= 0:
        velocityY =+ 3       
        Fucking_image_rect.y += velocityY              
        print("2")
  
    if Fucking_image_rect.x >= 1400:       
        velocityX += 3
        Fucking_image_rect.x -= velocityX       
        print("3")

    if Fucking_image_rect.x <= 0:       
        velocityX =+ 3
        Fucking_image_rect.x += velocityX      
        print("4")
    
    win.fill((R,G,B))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
    
    win.blit(the_Fucking_image, Fucking_image_rect) 
    
    pygame.display.update()
    clock.tick(144)