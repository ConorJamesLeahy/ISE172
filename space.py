# tutorial on pygame:  https://www.youtube.com/watch?v=FfWpgLFMI7w
import pygame
import random
#initializa the pygagme
pygame.init()

#create the screen
screen = pygame.display.set_mode((1200,800))

#Background
background = pygame.image.load('space.jpg')

#Title and Icon
pygame.display.set_caption("Space Invader")
icon= pygame.image.load('invader.png')
pygame.display.set_icon(icon) #Not sure if this works for macs :(

#player
playerImg = pygame.image.load('ship.png')
playerX = 500
playerY = 650
playerX_change = 0

#enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0,1075)
enemyY = 0
enemyX_change = 2
enemyY_change = 0


def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))

#Game Loop
running = True
while running:

    # Needs to be called after screen fill because it would overwrite
    screen.fill((0, 70, 65))
    #Arguments are red, green, blue

    #Background
    screen.blit(background, (0, 0))

    #playerX -= 0.2 #constantly moving in one direction

    for event in pygame.event.get():

        #print(event)
        if event.type == pygame.QUIT:
            running = False

            #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
                playerX_change = -6
            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
                playerX_change = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released")
                playerX_change = 0.0


    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1075:
        playerX = 1075

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX = 0
        enemyX_change = -110/100*(enemyX_change)
        enemyY += 60
    elif enemyX >= 1075:
        enemyX = 1075
        enemyX_change = -110/100*(enemyX_change)
        enemyY += 60

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
