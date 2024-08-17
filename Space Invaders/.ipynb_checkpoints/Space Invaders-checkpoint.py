import sys
import pygame
pygame.init()

size = width, height = 1600, 900
speed = [0, 0]

screen = pygame.display.set_mode(size)

ball = pygame.image.load("Rocketship.jpg")
ballrect = ball.get_rect()
pos = 700
direction = 0

def fire():
    pass

screen.blit(ball,ballrect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print('Right')
                direction = 1
                speed[0] = 1
            elif event.key == pygame.K_LEFT:
                speed[0] = -1
                print("Left")
                direction = -1
            if event.key == pygame.K_UP:
                print('FIRE!!')
                fire()
        if event.type == pygame.KEYUP:
            if direction == 1 and event.key == pygame.K_RIGHT:
                speed[0] = 0
            if direction == -1 and event.key == pygame.K_LEFT:
                speed[0] = 0
    ballrect = ballrect.move(speed)
    screen.fill((255, 255, 255))
    screen.blit(ball,ballrect)
    pygame.display.flip()
