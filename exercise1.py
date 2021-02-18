"""
    Create a display surface and caption it. Download an image of a small ball and
    import that image into your program.
    Create a horizontal ground of some thickness (something similar to what we saw
    in the aliens game). Let the initial position of this ball be on this ground.

    Write code such that the ball bounces between this ground and the top boundary
    of your display surface. That is, the ball keeps bouncing up and down and up and
    down and (you guessed it ;-))

    Note: Try to play around with colors as well. Also play with the frame speed.
    Hint: Recall that any action can be performed by writing code for various events.
            How to bounce the ball once it hits the ground or the boundary?
"""

import pygame


def main():
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
    ballX = 300
    ballY = 100
    ballY_change = 5

    orange = (255, 140 , 0)

    def ball(x,y):
        screen.blit(ballImg, (x, y))

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
            ballY_change = 5
        elif ballY >= 290:
            ballY = 290
            ballY_change = -5


        ball(ballX, ballY)



        pygame.display.update()

if __name__ == '__main__':
   main()
