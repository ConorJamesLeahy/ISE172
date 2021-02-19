"""
    Create a display surface and caption it.

    Create some very fancy animation. You can try to make something like this
    https://static.independent.co.uk/s3fs-public/thumbnails/image/2017/10/27/09/matrix-code.jpg?w968h681
    https://preview.codepad.co/playground/preview/css-loading-animation/1
    https://media.tenor.com/images/13b9f87445e2f66ea691d011bfd6e8c4/tenor.gif

    but preferably something much much nicer and more challenging :)))

    Just try your best!
"""

import pygame
import random
import time
import numpy as np


def main():
    # Write your pygame code (the "while" loop) in this "main" function.
    #initializa the pygagme
    pygame.init()

    #create the screen
    screen = pygame.display.set_mode((900,500))

    #Background
    background = pygame.image.load('background.jpg')

    #Title and Icon
    pygame.display.set_caption("Mega Man")
    icon= pygame.image.load('mega.png')
    pygame.display.set_icon(icon) #Not sure if this works for macs :(

    #player
    player = pygame.image.load('megaman.png')
    newpic = pygame.transform.scale(player, (64, 64))
    playerImg = newpic
    playerX = 100
    playerY = 300
    playerY_change = 0
    playerX_change = 0

    #Jumping variables
    v = 100
    m = 1
    isJump = False
    # #enemy
    # enemy = pygame.image.load('invader.png')
    # newpicture = pygame.transform.scale(enemy, (64, 64))
    # enemyImg = newpicture
    # enemyX = 850
    # enemyY = 305
    # enemyX_change = -1
    # enemyY_change = 0


    def player(x,y):
        screen.blit(playerImg, (x, y))

    #def enemy(x,y):
        #screen.blit(enemyImg, (x, y))
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
                    player =  pygame.image.load('run.png')
                    PlayerImg = pygame.transform.scale(player, (64, 64))
                if event.key == pygame.K_RIGHT:
                    print("Right arrow is pressed")
                    playerX_change = 6
                    player =  pygame.image.load('run.png')
                    PlayerImg = pygame.transform.scale(player, (64, 64))
                if isJump == False:
                    if event.key == pygame.K_SPACE:
                        print("SPACE is pressed")
                        isJump  == True
                        start_time = time.time()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                    print("Keystroke has been released")
                    playerX_change = 0.0


        playerX += playerX_change

        if playerX <= 0:
            playerX = 0
        elif playerX >= 836:
            playerX = 836

        # if isJump:
        #     #calculate force
        #     F = (1/2)*m*(v**2)
        #     #change the Y coordinate
        #     playerY_change = -F
        #
        #     #Decreasing going up and increasing negative on way down
        #     v = v-1
        #
        #     #when object is at max height
        #     if v<0:
        #         #negative sign to switch velocity
        #         m = -1
        #     #Object reaches its original state
        #     if playerY == 300:
        #         isJump = False
        #
        #         v = 20
        #         m = 1
        #     playerY += playerY_change


        # # elif playerY <= 250 & playerY_change < 0 :
        #      playerY_change = -.5
        # elif playerY <= 220 & playerY_change < 0 :
        #      playerY_change = -.25
        # elif playerY <= 200 & playerY_change < 0 :
        #      playerY_change = .25
        # elif playerY >= 220 & playerY_change > 0 :
        #      playerY_change = .5
        # elif playerY >= 270 & playerY_change > 0 :
        #      playerY_change = 1
        # elif playerY >= 300 & playerY_change > 0 :
        #      playerY_change = 0
        #      playerY = 300


        # enemyX += enemyX_change
        # if enemyX <= 0:
        #     enemyX = 0
        #     enemyX_change = -110/100*(enemyX_change)
        #     enemyY += 60
        # elif enemyX >= 1075:
        #     enemyX = 1075
        #     enemyX_change = -110/100*(enemyX_change)
        #     enemyY += 60

        player(playerX, playerY)
        #enemy(enemyX, enemyY)
        pygame.display.update()


if __name__ == '__main__':
    main()
