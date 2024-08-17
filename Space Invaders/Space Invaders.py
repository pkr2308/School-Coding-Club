'''
Completed Game!!!
'''

'''Initialisation'''
import sys
import pygame
import random

pygame.init() # Initialising pygame

pygame.display.set_caption("Space Invaders") # Setting caption to Space Invaders
font = pygame.font.Font('freesansbold.ttf', 32) # Setting font size and style for text

clock = pygame.time.get_ticks()
prevclock = -3000

score = 0
accuracy = 0 

no_of_asteroids = 1
prevasteroids = 0

size = width, height = 1200, 1000 # Screen size
speed = [0, 0] # Rocketspeed
bulletspeed = -1.5
asteroidspeed = 1.2
prevscore = 0
screen = pygame.display.set_mode(size) # Starting the screen

rocket = pygame.image.load("Rocketship.png") # Setting image for rocketship
asteroids = ['Asteroid1.png','Asteroid2.png','Asteroid3.png','Asteroid4.png'] # The different images for asteroids

background = pygame.image.load('Space.jpg') # The background

poof = pygame.image.load("Poof.png")
poof_image = False # Allowing for delay later to see 'Poof'

rocket_rect = rocket.get_rect()
rocket_rect = rocket_rect.move(500,750) # Moving the rocket from (0,0) to centre of bottom
direction = 0

asteroidlist = [] # List that will contain type and positions of all asteroids
bulletlist = [] # List that will contain positions of all bullets

delay = 2200 # Delay to create consecutive bullets

green = (0, 255, 0)
black = (0, 0, 0)

gameend = False

def fire():
    if len(bulletlist)<14:
        bulletlist.append([rocket_rect[0] + 50, rocket_rect[1]-50]) # Adding the bullet position to bulletlist

while True:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        '''
        Checking for keyboard input
        '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 1
                speed[0] = 2.5
            elif event.key == pygame.K_LEFT:
                speed[0] = -2.5
                direction = -1
            if event.key == pygame.K_SPACE: # Space key to fire
                fire()

        if event.type == pygame.KEYUP:
            if direction == 1 and event.key == pygame.K_RIGHT:
                speed[0] = 0
            if direction == -1 and event.key == pygame.K_LEFT:
                speed[0] = 0
                
    '''If rocket touching edge'''            
    if rocket_rect.left < 0:
        speed[0] = 0
        rocket_rect = rocket_rect.move([-rocket_rect.left + 1,0])
    if rocket_rect.right > width:
        speed[0] = 0
        rocket_rect = rocket_rect.move([-rocket_rect.right + width - 1,0])
    # Makes the rocket stop at the edge
    
    '''
    Making asteroids
    '''
    if (clock - prevclock) > delay:
        asteroidlist.append([asteroids[random.randint(0,3)],random.randint(150,width-150), 50])
        prevclock = clock
        # Creating an asteroid
    if (score%10 == 0 and prevscore < score) and not(delay <= 700):
        delay -= 100
        asteroidspeed += 0.1
        prevscore = score
        # Increasing speed and reducing delay of asteroids
    
    for item in asteroidlist: # Updating the position and making asteroids 
        item[2] += asteroidspeed
        asteroid = pygame.image.load(item[0])
        asteroid_rect = asteroid.get_rect()
        asteroid_rect = asteroid_rect.move(item[1], item[2])
        screen.blit(asteroid, asteroid_rect)
        if item[2] > height+100: # Deleting teh asteroid if it moves out of screen
            asteroidlist.remove(item)
            no_of_asteroids += 1
            if (prevasteroids == 0): 
                no_of_asteroids-=1 
                prevasteroids=1
            accuracy = score/no_of_asteroids*100 
            print(f'\t  \t Accuracy - {accuracy}')

    '''
    Moving bullets
    '''
    for item in bulletlist:
        item[1] += bulletspeed
        bullet = pygame.image.load("Bullet.png")
        bullet_rect = bullet.get_rect()
        bullet_rect = bullet_rect.move(item[0], item[1])
        screen.blit(bullet, bullet_rect)
        if item[1] < -100:
            bulletlist.remove(item)
            
    '''
    Checking if a bullet hit an asteroid
    '''
    for x in bulletlist:
        for y in asteroidlist:
            if abs(x[0] - y[1]) < 40 and abs(x[1] - y[2]) < 40: 
                # Checking for proximity and checking for impact
                screen.blit(poof,(y[1],y[2]+20)) # Adding poof there
                asteroidlist.remove(y) # Deleting asteroid
                bulletlist.remove(x)   # Deleting bullet
                prevscore = score
                score += 1 # Increasing score
                no_of_asteroids += 1
                if (prevasteroids == 0): 
                    no_of_asteroids-=1 
                    prevasteroids=1
                poof_image = True
                accuracy = score/no_of_asteroids*100
                print(f'Score - {score} \t Accuracy - {accuracy}') # Updating accuracy
                break
    
    clock = pygame.time.get_ticks() # Updating the clock
        
    ''' Updating screen '''       
    rocket_rect = rocket_rect.move(speed)
    screen.blit(rocket,rocket_rect)
    
    ''' Displaying Score '''    
    text1 = font.render(f'Score : {score}', True, green)
    text1Rect = text1.get_rect()
    text1Rect.center = (120, 50)
    screen.blit(text1, text1Rect)
    ''' Displaying Accuracy '''
    text2 = font.render(f'Accuracy : {round(accuracy,1)}', True, green)
    text2Rect = text2.get_rect()
    text2Rect.center = (1000, 50)
    screen.blit(text2, text2Rect)
    
    pygame.display.flip() # Rendering updates
    
    if(poof_image == True): # Setting delay of 70ms if there is a 'Poof'
        poof_image = False
        pygame.time.delay(70)
    
    '''
    Checking if rocket hit the asteroid
    '''
    for x in asteroidlist:
        if abs(rocket_rect[0] - x[1] + 50) < 120 and abs(rocket_rect[1] - x[2] + 50) < 80:
            boom = pygame.image.load("BOOM.png")
            boomrect = boom.get_rect()
            boomrect = boomrect.move(rocket_rect[0]-30,rocket_rect[1])
            screen.blit(boom,boomrect)
            pygame.display.flip()
            print("The asteroid hit you!! \nBad luck you lost!!")
            pygame.time.delay(1000)
            gameend = True
            pygame.quit()
            break
    if gameend == True:
        break
    
    ''' Checking for win '''
    if (score == 99 and accuracy > 85) or (score > 49 and accuracy > 95):
        print("Congratulations you win!!😁")
        font = pygame.font.Font('freesansbold.ttf', 80)
        wintext = font.render('Congratulations you win', True, green)
        win_rect = wintext.get_rect()
        win_rect.center = (600, 500)
        
        screen.blit(background,(0,0))
        screen.blit(rocket,rocket_rect)
        screen.blit(text1, text1Rect)
        screen.blit(text2, text2Rect)
        screen.blit(wintext, win_rect)
        
        pygame.display.flip()
        pygame.time.delay(3000)
        
        pygame.quit()
        break
''' Exiting the program'''
exit()