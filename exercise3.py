"""
    Create a display surface and caption it.

	Create 10 balls, each at different location and with different radius.
	Let each 1 second the radius of ball shrink a little bit.
	Once the radius is below certain threshold, the ball will disappear and
	a new ball will appear at a new random location.

	Make following or similar features:
	1. As the radius is shrinking, the ball is fading to black. Imagine that
	  the balls represent starts and they are fading into darkness ;)))
	2. Each ball should be moving into different direction. Once they hit the
	  boundary of screen, you can send it into different "random" direction.
	3. Add some additional cool functionality.
"""

import pygame
import random

def main():
    # Write your pygame code (the "while" loop) in this "main" function.
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
            elif ballY >= 290:
                ballY = 290
                ballY_change = -(random.randint(1,10))

            ball(ballX, ballY)



            ballX += ballX_change
            if ballX >= 590:
                ballX = 590
                ballX_change = -(random.randint(1,10))
            elif ballX <= 20:
                ballX = 20
                ballX_change = random.randint(1,10)


            ball(ballX, ballY)

            ######### BALL2

            ball2Y += ball2Y_change
            if ball2Y <= 20:
                ball2Y = 20
                ball2Y_change = random.randint(1,5)
            elif ball2Y >= 290:
                ball2Y = 290
                ball2Y_change = -(random.randint(1,5))

            ball2(ball2X, ball2Y)



            ball2X += ball2X_change
            if ball2X >= 590:
                ball2X = 590
                ball2X_change = -(random.randint(1,5))
            elif ball2X <= 20:
                ball2X = 20
                ball2X_change = random.randint(1,5)


            ball2(ball2X, ball2Y)

            pygame.display.update()



if __name__ == '__main__':
    main()
