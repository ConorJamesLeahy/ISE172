"""
    Create a display surface and caption it.

    Create some very fancy animation. You can try to make something like this
    https://static.independent.co.uk/s3fs-public/thumbnails/image/2017/10/27/09/matrix-code.jpg?w968h681
    https://preview.codepad.co/playground/preview/css-loading-animation/1
    https://media.tenor.com/images/13b9f87445e2f66ea691d011bfd6e8c4/tenor.gif

    but preferably something much much nicer and more challenging :)))

    Just try your best!
"""

#https://www.youtube.com/watch?v=FfWpgLFMI7w
#Went through this tutorial to make own aliens game


import pygame
import random
import time
import numpy as np
import math


def main():
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
    enemyX_change = 1
    enemyY_change = 0

    #bullet1
    bulletImg = pygame.image.load('bullet.png')
    bulletX = 0
    bulletY = 650
    bulletX_change = 0
    bulletY_change = 5
    bullet_state = "ready"
    #bullet cannot be seen

    #bullet2
    bullet2Img = pygame.image.load('bullet.png')
    bullet2X = 0
    bullet2Y = 650
    bullet2X_change = 0
    bullet2Y_change = 5
    bullet2_state = "ready"
    #bullet cannot be seen

    score1 = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    textX = 10
    textY = 10

    def show_score1(x, y):
        score_display1 = font.render("Score :" + str(score1), True, (255,255,255))
        screen.blit(score_display1, (x, y))


    def player(x,y):
        screen.blit(playerImg, (x, y))

    def enemy(x,y):
        screen.blit(enemyImg, (x, y))

    def fire_bullet(x,y):
        global bullet_state
        bullet_state = "fire"
        #need global to change variable outside this function
        #print(bullet_state)
        screen.blit(bulletImg, (x+16, y+10))
        #Where it appears in relation to spaceship

    def fire_bullet2(x,y):
        global bullet2_state
        bullet2_state = "fire"
        #need global to change variable outside this function
        #print(bullet2_state)
        screen.blit(bullet2Img, (x+80, y+10))
        #Where it appears in relation to spaceship

    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt((math.pow(enemyX-bulletX,2))+ (math.pow(enemyY-bulletY,2)))
        if distance < 55:
            print("Hit with 1")
            return True
        else:
            return False

    def isCollision2(enemyX, enemyY, bullet2X, bullet2Y):
        distance2 = math.sqrt((math.pow(enemyX-bullet2X,2))+ (math.pow(enemyY-bullet2Y,2)))
        if distance2 < 55:
            print("Hit with 2")
            return True
        else:
            return False
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
                    playerX_change = -4
                if event.key == pygame.K_RIGHT:
                    print("Right arrow is pressed")
                    playerX_change = 4
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        print("Space has been pressed")
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                        bullet_state = "fire"
                        fire_bullet2(bulletX, bullet2Y)
                        bullet2_state = "fire"

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

        #bullet movement
        if bulletY <= 0:
            bulletY = 650
            bullet_state = "ready"
        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change
        #bullet movement
        if bullet2Y <= 0:
            bullet2Y = 650
            bullet2_state = "ready"
        if bullet2_state is "fire":
            fire_bullet2(bulletX, bullet2Y)
            bullet2Y -= bullet2Y_change

        #isCollision
        collision = isCollision(enemyX, enemyY, bulletX, bulletY)
        collision2 = isCollision2(enemyX, enemyY, bullet2X, bullet2Y)
        if collision | collision2:
            print("reset")
            bulletY = 650
            bullet2Y = 650
            bullet_state = "ready"
            bullet2_state = "ready"
            score1 += 1
            print(score1)
            enemyX = random.randint(0,1075)
            enemyY = 0



        player(playerX, playerY)
        enemy(enemyX, enemyY)
        show_score1(textX, textY)

        pygame.display.update()


if __name__ == '__main__':
    main()
