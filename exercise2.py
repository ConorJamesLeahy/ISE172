"""
    Create a display surface and caption it. Download an image of a small ball and
    import that image into your program.
    Create a wall of some thickness all around the display surface, i.e., a
    perimeter along the display surface with a different color than your background.
    Make the initial position of the ball random, i.e., the ball's initial position
    should vary every time your code is run.

    Write code such that the ball keeps bouncing between these four walls either
    logically or arbitrarily.

    Also, write a code that counts the number of bounces on "each" wall, displays
    this count at a corner of your surface, and keeps updating the count as the
    ball keeps bouncing.

    Bonus-1: Attempt the same with multiple balls at a time on the surface.
    Bonus-2: Add other cool functionalities such as varying speed after a bounce, etc.

    Note: Try to play around with colors as well. Also play with the frame speed.
    Hint: Recall that any action can be performed by writing code for various events.
            How to code a ball that bounces off of all four walls?
"""

import pygame
import random

def main():
    # Write your pygame code (the "while" loop) in this "main" function.
    #Write your pygame code (the "while" loop) in this "main" function.
    #initializa the pygagme
    pygame.init()

    #create the screen
    screen = pygame.display.set_mode((800,500))

    #Title and Icon
    pygame.display.set_caption("Ball Bounce")
    icon= pygame.image.load('invader.png')
    pygame.display.set_icon(icon) #Not sure if this works for macs :(

    #player
    ballImg = pygame.image.load('ball.png')
    ballX = random.randint(20, 590)
    ballY = random.randint(20, 290)
    ballY_change = random.randint(1,5)
    ballX_change = random.randint(1,5)

    #player2
    ball2Img = pygame.image.load('ball.png')
    ball2X = random.randint(20, 590)
    ball2Y = random.randint(20, 290)
    ball2Y_change = random.randint(1,5)
    ball2X_change = random.randint(1,5)

    orange = (255, 140 , 0)
    score1 = 0
    score2 = 0
    font = pygame.font.Font('freesansbold.ttf', 32)

    textX = 10
    textY = 10
    textY2 = 40

    def show_score1(x, y):
        score_display1 = font.render("Score1 :" + str(score1), True, (0,0,0))
        screen.blit(score_display1, (x, y))

    def show_score2(x, y):
        score_display2 = font.render("Score2 :" + str(score2), True, (0,0,0))
        screen.blit(score_display2, (x, y))


    def ball(x,y):
        screen.blit(ballImg, (x, y))
    def ball2(z,t):
        screen.blit(ball2Img, (z, t))

    #Game Loop
    running = True
    while running:

        # Needs to be called after screen fill because it would overwrite
        screen.fill((255, 255, 255))
        #Arguments are red, green, blue


        pygame.draw.rect(screen, orange, [0, 0, 20, 600], 0) #left side
        pygame.draw.rect(screen, orange, [0, 0, 800, 20], 0)  #ceiling
        pygame.draw.rect(screen, orange, [0, 480, 800, 20], 0)  #ground
        pygame.draw.rect(screen, orange, [780, 0, 20, 1000], 0) # right side

        for event in pygame.event.get():

            #print(event)
            if event.type == pygame.QUIT:
                running = False


        ballY += ballY_change
        if ballY <= 20:
            ballY = 20
            ballY_change = random.randint(1,10)
            score1 += 1
        elif ballY >= 290:
            ballY = 290
            ballY_change = -(random.randint(1,10))
            score1 += 1

        ball(ballX, ballY)



        ballX += ballX_change
        if ballX >= 590:
            ballX = 590
            ballX_change = -(random.randint(1,10))
            score1 += 1
            print(score1)
        elif ballX <= 20:
            ballX = 20
            ballX_change = random.randint(1,10)
            score1 += 1
            print(score1)


        ball(ballX, ballY)

        ######### BALL2

        ball2Y += ball2Y_change
        if ball2Y <= 20:
            ball2Y = 20
            ball2Y_change = random.randint(1,5)
            score2 += 1
            print(score2)
        elif ball2Y >= 290:
            ball2Y = 290
            ball2Y_change = -(random.randint(1,5))
            score2 += 1
            print(score2)

        ball2(ball2X, ball2Y)



        ball2X += ball2X_change
        if ball2X >= 590:
            ball2X = 590
            ball2X_change = -(random.randint(1,5))
            score2 += 1
        elif ball2X <= 20:
            ball2X = 20
            ball2X_change = random.randint(1,5)
            score2 += 1


        ball2(ball2X, ball2Y)
        show_score1(textX, textY)
        show_score2(textX, textY2)

        pygame.display.update()


if __name__ == '__main__':
    main()
