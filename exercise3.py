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
import time
import numpy as np

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
        ballImg = []
        ballX = []
        ballY = []
        rad = []
        ballX_change = []
        ballY_change = []
        num_of_balls = 10
        XR = []
        YR = []

        for i in range(num_of_balls):
            ballpic = pygame.image.load('ball.png')
            R = random.randint(30, 100)
            radi = R
            ballpic = pygame.transform.scale(ballpic, (radi, radi))
            rad.append(radi)
            ballImg.append(ballpic)

            Xb = (random.randint(40, 500))
            Yb = (random.randint(40, 300))
            ballX.append(Xb)
            ballY.append(Yb)
            XR.append((radi+Xb))
            YR.append((radi+Yb))
            ballY_change.append(random.randint(-5,5))
            ballX_change.append(random.randint(-5,5))

        # ballImgArray = np.array(ballImg)
        xInts = [int(ballX[i]) for i in range(0, (num_of_balls - 1))]
        yInts = [int(ballY[i]) for i in range(0, (num_of_balls - 1))]
        radInts = [int(rad[i]) for i in range(0, (num_of_balls - 1))]
        # ballX_changeArray = np.array(ballX_change)
        # ballY_changeArray = np.array(ballY_change)
        # num_of_balls = 10




        #print(rad)
        orange = (255, 140 , 0)

        def ball(x,y):
            screen.blit(ballImg[i], (x, y))

        def ball2(z,t):
                screen.blit(ball2Img, (z, t))

        start_time = time.time()
        #Game Loop
        running = True
        while running:


            # print(start_time)
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

            for i in range(0, num_of_balls-1):
                #Y changes
                yInts[i] += ballY_change[i]
                YR[i] += ballY_change[i]
                if (yInts[i]) <= 20:
                    yInts[i] = 20
                    ballY_change[i] = random.randint(1,10)
                elif (YR[i]) >= 480:
                    radii = radInts[i]
                    adjust = 480 - radii
                    yInts[i] = adjust
                    YR[i] = 480
                    ballY_change[i] = -(random.randint(1,10))
                ball(xInts[i], yInts[i])

                #X changes
                xInts[i] += ballX_change[i]
                XR[i] += ballX_change[i]
                if (XR[i]) >= 780:
                    radii = radInts[i]
                    adjust = 780 - radii
                    xInts[i] = adjust
                    XR[i] = 780
                    ballX_change[i] = -(random.randint(1,3))
                elif (xInts[i]) <= 20:
                    xInts[i] = 20
                    ballX_change[i] = random.randint(1,3)
                ball(xInts[i], yInts[i])

                #RADIUS CHANGES
                newTime = time.time()
                timer = newTime - start_time
                print(timer)
                if timer >= 1/30:
                    print('here')
                    radInts[i] -= 1
                    if radInts[i] <= 10:
                        print("Here2")
                        radInts[i] = random.randint(30,100)
                        yInts[i] = (random.randint(40, 500))
                        xInts[i] = (random.randint(40, 300))
                        YR[i] = yInts[i] + radInts[i]
                        XR[i] = xInts[i] + radInts[i]
                    newpic = pygame.transform.scale(ballpic, (radInts[i], radInts[i]))
                    ballImg[i] = newpic
                    start_time = time.time()
                ball(xInts[i], yInts[i])
            pygame.display.update()



if __name__ == '__main__':
    main()
